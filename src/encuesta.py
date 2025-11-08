def realizar_encuesta():
    print("\n--- Datos del Usuario ---")

    # Validar nombre (solo letras y espacios)
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("❌ El nombre solo puede tener letras y espacios.")

    # Validar edad (1 a 100)
    while True:
        try:
            edad = int(input("Ingrese su edad (15-25): "))
            if 15 <= edad <= 25:
                break
            else:
                print("❌ La edad debe estar entre 15 y 25.")
        except:
            print("❌ Ingrese solo números enteros.")

    # Preguntas de la encuesta
    felicidad = validar_escala("Del 1 al 5, ¿qué tan feliz estás hoy? ")
    estres = validar_escala("Del 1 al 5, ¿qué tan estresado estás hoy? ")
    motivacion = validar_escala("Del 1 al 5, ¿qué tan motivado estás hoy? ")

    return {
        "nombre": nombre,
        "edad": edad,
        "felicidad": felicidad,
        "estres": estres,
        "motivacion": motivacion
    }

def validar_escala(pregunta):
    while True:
        try:
            valor = int(input(pregunta))
            if 1 <= valor <= 5:
                return valor
            else:
                print("❌ Debe estar entre 1 y 5.")
        except:
            print("❌ Solo números.")
