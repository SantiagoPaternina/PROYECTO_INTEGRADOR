import os
import csv
import json

def guardar_csv(ruta, datos):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=datos.keys())
        if archivo.tell() == 0:
            escritor.writeheader()
        escritor.writerow(datos)
    print("✅ Datos guardados en CSV")

def guardar_json(ruta, datos):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lista = json.load(archivo)
    except:
        lista = []

    lista.append(datos)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4)
    print("✅ Datos guardados en JSON")
