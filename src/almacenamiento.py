import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
USUARIOS_FILE = os.path.join(DATA_DIR, "usuarios.csv")
ENCUESTAS_FILE = os.path.join(DATA_DIR, "encuestas.csv")

os.makedirs(DATA_DIR, exist_ok=True)

def _leer_seguro(path):
    """Lee un CSV de forma segura, evitando errores si está vacío o dañado."""
    if not os.path.exists(path) or os.stat(path).st_size == 0:
        return pd.DataFrame()
    try:
        df = pd.read_csv(path)
        return df
    except Exception:
        # Si el archivo existe pero está corrupto o vacío
        return pd.DataFrame()

def guardar_usuario(usuario):
    """Guarda la información del usuario en usuarios.csv"""
    df_exist = _leer_seguro(USUARIOS_FILE)
    df_nuevo = pd.DataFrame([usuario])
    df_final = pd.concat([df_exist, df_nuevo], ignore_index=True)
    df_final.to_csv(USUARIOS_FILE, index=False)

def guardar_encuesta(encuesta):
    """Guarda las respuestas de la encuesta en encuestas.csv"""
    df_exist = _leer_seguro(ENCUESTAS_FILE)
    df_nuevo = pd.DataFrame([encuesta])
    df_final = pd.concat([df_exist, df_nuevo], ignore_index=True)
    df_final.to_csv(ENCUESTAS_FILE, index=False)

def cargar_encuestas():
    """Carga las encuestas, o devuelve DataFrame vacío si no existen."""
    return _leer_seguro(ENCUESTAS_FILE)
