import sqlite3
import json
import pandas as pd
import os

# Ruta donde se guardará la base de datos
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
os.makedirs(DATA_DIR, exist_ok=True)

DB_PATH = os.path.join(DATA_DIR, "database.db")


# -----------------------------------
# ✅ Conexión a la base de datos
# -----------------------------------
def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


# -----------------------------------
# ✅ Crear tablas si no existen
# -----------------------------------
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS encuestas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            respuestas_json TEXT NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        );
    """)

    conn.commit()
    conn.close()


# -----------------------------------
# ✅ Guardar usuario
# -----------------------------------
def guardar_usuario(usuario):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nombre, edad)
        VALUES (?, ?)
    """, (usuario["nombre"], usuario["edad"]))

    conn.commit()
    user_id = cursor.lastrowid
    conn.close()

    return user_id


# -----------------------------------
# ✅ Guardar encuesta
# -----------------------------------
def guardar_encuesta(usuario_id, respuestas):
    conn = get_connection()
    cursor = conn.cursor()

    respuestas_json = json.dumps(respuestas, ensure_ascii=False)

    cursor.execute("""
        INSERT INTO encuestas (usuario_id, respuestas_json)
        VALUES (?, ?)
    """, (usuario_id, respuestas_json))

    conn.commit()
    conn.close()


# -----------------------------------
# ✅ Cargar encuestas (JSON expandido sin duplicados)
# -----------------------------------
def cargar_encuestas():
    conn = get_connection()

    df = pd.read_sql_query("""
        SELECT 
            encuestas.id AS encuesta_id,
            usuarios.nombre AS nombre_usuario,
            usuarios.edad AS edad_usuario,
            encuestas.fecha,
            encuestas.respuestas_json
        FROM encuestas
        JOIN usuarios ON usuarios.id = encuestas.usuario_id
        ORDER BY encuestas.fecha DESC
    """, conn)

    conn.close()

    if df.empty:
        return df

    # Expandir JSON → columnas
    respuestas = df["respuestas_json"].apply(json.loads).apply(pd.Series)

    # Prefijo limpio para evitar duplicados
    respuestas = respuestas.rename(columns=lambda c: f"resp_{c}")

    df = df.drop(columns=["respuestas_json"])
    df = pd.concat([df, respuestas], axis=1)

    return df
