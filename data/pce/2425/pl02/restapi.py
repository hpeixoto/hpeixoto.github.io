import time
import requests
import psycopg2

DB_CONFIG = {
    "dbname": "pce",
    "user": "nextgen_user",
    "password": "nextgen_password",
    "host": "localhost",
    "port": "5432"
}

def connect_db():
    return psycopg2.connect(**DB_CONFIG)

def fetch_sensor_data(sensor_id):
    url = f"http://nosql.hpeixoto.me/api/sensor/{sensor_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao obter dados do sensor {sensor_id}: {response.status_code}")
    
def get_current_episode(patientid):
    try:
        conn = connect_db()
        cur = conn.cursor()

        query = """
            SELECT episodio FROM public.internamento
            WHERE id_paciente = %s AND data_alta IS NULL
            ORDER BY data_admissao DESC
            LIMIT 1;
        """

        cur.execute(query, (patientid,))
        result = cur.fetchone()

        cur.close()
        conn.close()

        if result:
            return result[0]
        else:
            print(f"No active internment found for patient {patientid}")
            return None

    except Exception as e:
        print(f"Error fetching episode for patient {patientid}: {e}")
        return None

def insert_data_into_db(data):
    try:

        conn = connect_db()
        cur = conn.cursor()

        patientid = data["patient"]["patientid"]
        episodio = get_current_episode(data["patient"]["patientid"])
        bodytemp = data["bodytemp"]
        systolic = data["bloodpress"]["systolic"]
        diastolic = data["bloodpress"]["diastolic"]
        bpm = data["bpm"]
        sato2 = data["sato2"]
        sensorid = data["sensorid"]
        data_medicao = data["timestamp"]

        if (data["type_of_sensor"] == 'blood'):
            ferritina = data["blood"]["ferritine"]
            hemoglobina = data["blood"]["hemoglobine"]
            measurements = [
                ("bodytemp", bodytemp),
                ("systolic", systolic),
                ("diastolic", diastolic),
                ("bpm", bpm),
                ("sato2", sato2),
                ("ferritina", ferritina),
                ("hemoglobina", hemoglobina),
            ]

        else:
            measurements = [
                ("bodytemp", bodytemp),
                ("systolic", systolic),
                ("diastolic", diastolic),
                ("bpm", bpm),
                ("sato2", sato2),
                ]
   
        for measure, value in measurements:
            cur.execute("""
                INSERT INTO public.medicoes (id_paciente, data_medicao, sensor_id, tipo_medicao, valor, episodio)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (id_medicao) DO NOTHING;
            """, (patientid, data_medicao, sensorid, measure, str(value), episodio))

        conn.commit()

        cur.close()
        conn.close()

        #print(f"Dados do sensor {sensorid} inseridos com sucesso!")

    except Exception as e:
        print(f"Erro ao inserir na base de dados: {e}")

sensor_list = [3001, 3002, 3003, 3004, 3005, 4001, 4002, 4003, 4004, 4005]
while True:
    print("Executing...")
    for sensor_id in sensor_list:
        try:
            data = fetch_sensor_data(sensor_id)
            insert_data_into_db(data)
        except Exception as e:
            print(f"Erro ao processar sensor {sensor_id}: {e}")
    print("Waiting 20 seconds before next execution...")
    
    time.sleep(20) 