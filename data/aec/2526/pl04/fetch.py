#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
import mysql.connector
from datetime import datetime
from typing import Optional

# -----------------------------
# Config MySQL (ajusta se preciso)
# -----------------------------
DB_CONFIG = dict(
    host="localhost",
    user="root",
    password="SENHA",
    database="aec",  # schema já criado
)

# -----------------------------
# URLs dos datasets
# -----------------------------
URL_DOENTES = "https://hpeixoto.me/doentes.json"
URL_COD_POSTAL = "https://hpeixoto.me/cod_postal.json"
URL_REGISTOS = "https://hpeixoto.me/registos.json"

# -----------------------------
# Helpers
# -----------------------------
CP_RE = re.compile(r"^\d{4}-\d{3}$")

def clean_cod_postal(value: Optional[str]) -> Optional[str]:
    """
    Normaliza código postal para 'NNNN-NNN'.
    - Aceita CP4 como 'NNNN-000'
    - Ignora lixo (letras, espaços, etc.)
    """
    if not value:
        return None
    v = str(value).strip().upper()
    # Fica só com dígitos
    digits = re.sub(r"\D", "", v)
    if len(digits) == 7:
        v = f"{digits[:4]}-{digits[4:]}"
        return v if CP_RE.match(v) else None
    if len(digits) == 4:
        return f"{digits}-000"
    # Se já veio formatado e válido
    if CP_RE.match(v):
        return v
    return None

def to_mysql_date(iso_date: Optional[str]):
    """
    Converte 'YYYY-MM-DD' ou ISO com 'T'/'Z' para DATE MySQL.
    Devolve None se inválida.
    """
    if not iso_date:
        return None
    s = str(iso_date).strip()
    try:
        # aceita 'YYYY-MM-DD' e 'YYYY-MM-DDTHH:MM:SS[.fff]Z?'
        s = s.replace("Z", "").replace("T", " ")
        return datetime.fromisoformat(s).date()
    except ValueError:
        return None

def ensure_cod_postal_exists(cursor, cod_postal: Optional[str], localidade: Optional[str] = None) -> Optional[str]:
    """
    Garante que o CP existe na tabela cod_postal (após normalizar).
    Devolve o CP normalizado ou None.
    """
    cp = clean_cod_postal(cod_postal)
    if not cp:
        return None
    cursor.execute("SELECT 1 FROM cod_postal WHERE cod_postal = %s", (cp,))
    if cursor.fetchone() is None:
        cursor.execute(
            """
            INSERT INTO cod_postal (cod_postal, localidade)
            VALUES (%s, %s)
            """,
            (cp, localidade or "Desconhecida"),
        )
    return cp

# -----------------------------
# Main
# -----------------------------
def main():
    # Conexão
    db = mysql.connector.connect(**DB_CONFIG)
    cursor = db.cursor()

    # --- Esquema limpo (drop & create)
    cursor.execute("DROP TABLE IF EXISTS registos;")
    cursor.execute("DROP TABLE IF EXISTS doentes;")
    cursor.execute("DROP TABLE IF EXISTS cod_postal;")

    cursor.execute("""
    CREATE TABLE cod_postal (
        cod_postal VARCHAR(10) PRIMARY KEY,
        localidade VARCHAR(100)
    );
    """)

    cursor.execute("""
    CREATE TABLE doentes (
        id_paciente INT PRIMARY KEY,
        nome VARCHAR(100),
        data_nascimento DATE,
        sexo VARCHAR(10),
        cod_postal VARCHAR(10),
        FOREIGN KEY (cod_postal) REFERENCES cod_postal(cod_postal)
    );
    """)

    cursor.execute("""
    CREATE TABLE registos (
        id_registo INT PRIMARY KEY AUTO_INCREMENT,
        id_paciente INT,
        data_registo DATE,
        temperatura VARCHAR(30),
        dor_cabeca VARCHAR(30),
        dor_muscular VARCHAR(30),
        tosse VARCHAR(30),
        diarreia VARCHAR(30),
        olfato_paladar VARCHAR(30),
        avaliacao_global VARCHAR(30),
        FOREIGN KEY (id_paciente) REFERENCES doentes(id_paciente)
    );
    """)

    db.commit()

    # --- Fetch de dados
    def fetch_json(url):
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        return resp.json()

    cod_postais = fetch_json(URL_COD_POSTAL)
    doentes = fetch_json(URL_DOENTES)
    registos = fetch_json(URL_REGISTOS)

    # --- Inserção dos códigos postais (idempotente)
    cp_inseridos = 0
    for c in cod_postais:
        cp_norm = clean_cod_postal(c.get("cod_postal"))
        if not cp_norm:
            continue
        localidade = (c.get("localidade") or "Desconhecida").strip()
        cursor.execute(
            """
            INSERT INTO cod_postal (cod_postal, localidade)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE localidade = VALUES(localidade)
            """,
            (cp_norm, localidade),
        )
        cp_inseridos += 1
    db.commit()

    # --- Inserção dos doentes (garantindo FK do CP)
    doentes_ok = 0
    for d in doentes:
        cp = ensure_cod_postal_exists(cursor, d.get("cod_postal"))
        cursor.execute(
            """
            INSERT INTO doentes (id_paciente, nome, data_nascimento, sexo, cod_postal)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                nome = VALUES(nome),
                data_nascimento = VALUES(data_nascimento),
                sexo = VALUES(sexo),
                cod_postal = VALUES(cod_postal)
            """,
            (
                d.get("id_paciente"),
                d.get("nome"),
                to_mysql_date(d.get("data_nascimento")),
                d.get("genero"),
                cp,
            ),
        )
        doentes_ok += 1
    db.commit()

    # --- Inserção dos registos clínicos
    registos_ok = 0
    for r in registos:
        numseq = r.get("NUMSEQ")
        if not numseq:
            continue
        try:
            id_paciente = int(numseq)
        except (TypeError, ValueError):
            continue

        # Só insere se existir o doente
        cursor.execute("SELECT 1 FROM doentes WHERE id_paciente = %s", (id_paciente,))
        if cursor.fetchone() is None:
            continue

        cursor.execute(
            """
            INSERT INTO registos (
                id_paciente, data_registo, temperatura, dor_cabeca,
                dor_muscular, tosse, diarreia, olfato_paladar, avaliacao_global
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                id_paciente,
                to_mysql_date(r.get("DATAREGISTO")),
                r.get("TEMPERATURA"),
                r.get("DOR_CABECA"),
                r.get("DOR_MUSCULAR"),
                r.get("TOSSE"),
                r.get("DIARREIA"),
                r.get("OLFATO_PALADAR"),
                r.get("AVALIACAO_GLOBAL"),
            ),
        )
        registos_ok += 1

    db.commit()

    cursor.close()
    db.close()
    print("Dados importados com sucesso!")

if __name__ == "__main__":
    try:
        main()
    except requests.HTTPError as e:
        print(f"Erro HTTP ao obter dados: {e}")
        raise
    except mysql.connector.IntegrityError as e:
        print(f"Erro de integridade MySQL: {e}")
        raise
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise
