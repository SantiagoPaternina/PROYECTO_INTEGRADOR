import streamlit as st
from almacenamiento import guardar_usuario, guardar_encuesta, cargar_encuestas
from encuesta import mostrar_encuesta
from analisis import mostrar_dashboard
from agente import generar_consejo_contextual

st.set_page_config(
    page_title="Bienestar Juvenil",
    page_icon="💬",
    layout="wide",
)

def set_background(image_url: str):
    st.markdown(
        f"""
        <style>
        /* Fondo de la app */
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
                        url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: orange;  /* color general del texto */
        }}
        /* Títulos y textos importantes */
        .stTitle, .stHeader, .stText, .stMarkdown {{
            color: orange !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    set_background("https://image.tmdb.org/t/p/original/p5ozvmdgsmbWe0H8Xk7Rc8SCwAB.jpg")

    st.title("💬 Plataforma de Bienestar Emocional Juvenil")
    st.caption("Proyecto Integrador – Nuevas Tecnologías")

    menu = ["Usuario", "Administrador"]
    opcion = st.sidebar.selectbox("Selecciona tu rol:", menu)

    if opcion == "Usuario":
        st.header("🧠 Formulario de Bienestar para Jóvenes")
        resultado = mostrar_encuesta()
        if resultado:
            if not resultado["nombre"]:
                st.error("Por favor ingresa tu nombre completo.")
            elif resultado["edad"] < 15 or resultado["edad"] > 25:
                st.error("La edad debe estar entre 15 y 25 años.")
            else:
                guardar_usuario({"nombre": resultado["nombre"], "edad": resultado["edad"]})
                guardar_encuesta(resultado)
                consejo = generar_consejo_contextual(resultado)
                st.success("✅ Encuesta enviada correctamente.")
                st.info(f"💡 Consejo personalizado: {consejo}")

    elif opcion == "Administrador":
        st.header("🔐 Panel de Administración")
        user = st.text_input("Usuario:")
        password = st.text_input("Contraseña:", type="password")
        if st.button("Ingresar"):
            if user == "admin" and password == "1234":
                encuestas_df = cargar_encuestas()
                mostrar_dashboard(encuestas_df)
            else:
                st.error("Usuario o contraseña incorrectos.")

if __name__ == "__main__":
    main()
