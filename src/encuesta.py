import streamlit as st

def mostrar_encuesta():
    st.header("🧠 Encuesta de Bienestar Emocional")

    nombre = st.text_input("Nombre:")
    edad = st.number_input("Edad (15 a 25 años)", min_value=15, max_value=25)
    if not nombre:
        st.warning("Por favor, escribe tu nombre.")
        return None

    preguntas = {
        "¿Cómo te sientes hoy?": ["Feliz 😊", "Triste 😔", "Ansioso 😰", "Motivado 💪", "Cansado 😴"],
        "¿Cómo ha estado tu sueño últimamente?": ["Muy bien", "Regular", "Mal"],
        "¿Qué tanto disfrutas tus actividades diarias?": ["Mucho", "Poco", "Nada"],
        "¿Sientes apoyo de tus amigos o familia?": ["Sí", "A veces", "No"],
        "¿Has sentido estrés últimamente?": ["Sí", "No"],
        "¿Tienes energía para tus estudios o trabajo?": ["Sí", "Algo", "No"],
        "¿Cuántas horas duermes al día?": [">8", "6-8", "<6"],
        "¿Con qué frecuencia haces ejercicio?": ["Diario", "Ocasional", "Nunca"],
        "¿Cómo calificarías tu ánimo general?": ["Excelente", "Bueno", "Regular", "Bajo"],
        "¿Te gustaría recibir recursos o apoyo emocional?": ["Sí", "Tal vez", "No"]
    }

    respuestas = {p: st.radio(p, opciones) for p, opciones in preguntas.items()}

    if st.button("Enviar encuesta"):
        return {"nombre": nombre, "edad": edad, **respuestas}

    return None
