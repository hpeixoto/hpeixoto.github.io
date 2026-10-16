require('dotenv').config();
const express = require('express');
const { Pool } = require('pg');
const axios = require('axios');

const app = express();
const port = process.env.PORT || 3000;

// Configuração do PostgreSQL
const pool = new Pool({
   connectionString: process.env.DATABASE_URL,
});

// Função para obter o episódio atual (substitui isto com a tua lógica real)
const getCurrentEpisode = async (patientId) => {
    // Simulação de lógica para obter o episódio atual do paciente
    return `episodio_${patientId}`;
};

// Rota para obter os dados do sensor e armazená-los no banco de dados
app.get('/api/sensor/:sensor_id', async (req, res) => {
    const { sensor_id } = req.params;
    const url = `http://nosql.hpeixoto.me/api/sensor/${sensor_id}`;

    try {
        // Obter os dados do sensor da API externa
        const response = await axios.get(url);
        const data = response.data;

        // Parse dos dados
        const patientid = data["patient"]["patientid"];
        const bodytemp = data["bodytemp"];
        const systolic = data["bloodpress"]["systolic"];
        const diastolic = data["bloodpress"]["diastolic"];
        const bpm = data["bpm"];
        const sato2 = data["sato2"];
        const sensorid = data["sensorid"];
        const data_medicao = data["timestamp"];

        let measurements = [
            ["bodytemp", bodytemp],
            ["systolic", systolic],
            ["diastolic", diastolic],
            ["bpm", bpm],
            ["sato2", sato2]
        ];

        if (data["type_of_sensor"] === "blood") {
            const ferritina = data["blood"]["ferritine"];
            const hemoglobina = data["blood"]["hemoglobine"];
            measurements.push(["ferritina", ferritina], ["hemoglobina", hemoglobina]);
        }

        // Inserir os dados na base de dados
        const client = await pool.connect();
        try {
            for (let [measure, value] of measurements) {
                await client.query(
                    `INSERT INTO public.medicoes (id_paciente, data_medicao, sensor_id, tipo_medicao, valor, episodio)
                     VALUES ($1, $2, $3, $4, $5, $6)
                     ON CONFLICT (id_medicao) DO NOTHING;`,
                    [patientid, data_medicao, sensorid, measure, String(value), 10000000]
                );
            }
        } finally {
            client.release();
        }

        res.json({ message: "Dados armazenados com sucesso!" });
    } catch (error) {
        console.error("Erro ao buscar ou armazenar dados:", error);
        res.status(500).json({ error: "Erro ao processar os dados" });
    }
});

// Iniciar o servidor
app.listen(port, () => {
    console.log(`Servidor a correr em http://localhost:${port}`);
});