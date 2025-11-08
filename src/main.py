from encuesta import realizar_encuesta
from almacenamiento import guardar_csv, guardar_json

def main():
    print("=== ENCUESTA DE USUARIOS ===")

    usuario = realizar_encuesta()

    print("\n¿En qué formato deseas guardar la información?")
    print("1. CSV")
    print("2. JSON")
    print("3. Ambos")

    opcion = input("Elige una opción (1-3): ")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        guardar_csv("data/usuarios.csv", usuario)
        print("✅ Archivo guardado en formato CSV.")
    elif opcion == "2":
        guardar_json("data/usuarios.json", usuario)
        print("✅ Archivo guardado en formato JSON.")
    elif opcion == "3":
        guardar_csv("data/usuarios.csv", usuario)
        guardar_json("data/usuarios.json", usuario)
        print("✅ Archivo guardado en ambos formatos: CSV y JSON.")
    else:
        print("❌ Opción no válida. Debes elegir entre 1, 2 o 3.")

if __name__ == "__main__":
    main()
