import pandas as pd
import matplotlib.pyplot as plt
import json

def analizar_datos(df, fuente="CSV"):
    print(f"\n=== Análisis de Datos desde {fuente} ===\n")
    print(df.head())

    if {"edad", "nombre", "felicidad", "estres", "motivacion"}.issubset(df.columns):
        promedio_edad = df["edad"].mean()
        promedio_felicidad = df["felicidad"].mean()
        promedio_estres = df["estres"].mean()
        promedio_motivacion = df["motivacion"].mean()

        print(f"\n📌 Promedio de edades: {promedio_edad:.2f}")
        print(f"📌 Promedio de felicidad: {promedio_felicidad:.2f}")
        print(f"📌 Promedio de estrés: {promedio_estres:.2f}")
        print(f"📌 Promedio de motivación: {promedio_motivacion:.2f}")

        # Crear figura con 2x2 subplots
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))

        # -------- Gráfico 1: Edades --------
        axs[0, 0].scatter(range(len(df["edad"])), df["edad"], color="blue", label="Edades")
        for i, fila in df.iterrows():
            axs[0, 0].text(i, fila["edad"] + 0.2, fila["nombre"], fontsize=7, ha="center", rotation=30)

        axs[0, 0].axhline(promedio_edad, color="red", linestyle="--", label=f"Promedio ({promedio_edad:.2f})")

        # Círculo verde englobando
        x_min, x_max = 0, len(df["edad"])
        y_min, y_max = df["edad"].min(), df["edad"].max()
        centro_x = (x_max - x_min) / 2
        centro_y = (y_max + y_min) / 2
        radio = max((x_max - x_min) / 2, (y_max - y_min) / 2) + 1
        circulo = plt.Circle((centro_x, centro_y), radio, color="green", fill=False, linewidth=2, linestyle="--")
        axs[0, 0].add_patch(circulo)

        axs[0, 0].set_title("Edades de los usuarios")
        axs[0, 0].set_xlabel("Usuario (índice)")
        axs[0, 0].set_ylabel("Edad")
        axs[0, 0].legend()

        # -------- Gráfico 2: Promedio felicidad --------
        axs[0, 1].bar(["Felicidad"], [promedio_felicidad], color="orange")
        axs[0, 1].set_ylim(0, 5)
        axs[0, 1].set_title("Promedio de Felicidad")

        # -------- Gráfico 3: Promedio estrés --------
        axs[1, 0].bar(["Estrés"], [promedio_estres], color="red")
        axs[1, 0].set_ylim(0, 5)
        axs[1, 0].set_title("Promedio de Estrés")

        # -------- Gráfico 4: Promedio motivación --------
        axs[1, 1].bar(["Motivación"], [promedio_motivacion], color="green")
        axs[1, 1].set_ylim(0, 5)
        axs[1, 1].set_title("Promedio de Motivación")

        # Mostrar todo el dashboard
        plt.tight_layout()
        plt.show()


def analizar_csv():
    try:
        datos = pd.read_csv("./data/usuarios.csv")
        analizar_datos(datos, "CSV")
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo usuarios.csv")


def analizar_json():
    try:
        with open("./data/usuarios.json", "r", encoding="utf-8") as f:
            datos_json = json.load(f)
        df = pd.DataFrame(datos_json)
        analizar_datos(df, "JSON")
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo usuarios.json")


if __name__ == "__main__":
    print("¿Qué archivo deseas analizar?")
    print("1. usuarios.csv")
    print("2. usuarios.json")
    print("3. Ambos formatos")

    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == "1":
        analizar_csv()
    elif opcion == "2":
        analizar_json()
    elif opcion == "3":
        analizar_csv()
        analizar_json()
    else:
        print("⚠️ Opción no válida")
