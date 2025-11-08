import streamlit as st
from almacenamiento import init_db, guardar_usuario, guardar_encuesta, cargar_encuestas
from encuesta import mostrar_encuesta
from analisis import mostrar_dashboard
from agente import generar_consejo_contextual
import plotly.express as px

# ✅ Inicializar la BD
init_db()

st.set_page_config(
    page_title="Bienestar Juvenil",
    page_icon="💬",
    layout="wide",
)

# -----------------------------------
# ✅ Fondo y color naranja global
# -----------------------------------
def set_background(image_url: str):
    st.markdown(
        f"""
        <style>
            .stApp {{
                background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                            url("{image_url}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: orange !important;
            }}

            h1, h2, h3, h4, h5, h6, p, span, div, label {{
                color: orange !important;
            }}

            .stTextInput > div > div > input,
            .stNumberInput > div > div > input {{
                color: orange !important;
            }}

            .stRadio > label, .stCheckbox > label {{
                color: orange !important;
            }}

            .stSidebar {{
                background-color: rgba(0,0,0,0.4) !important;
            }}

            .stSidebar * {{
                color: orange !important;
            }}

            .stButton > button {{
                background-color: #ff8c00 !important;
                color: black !important;
            }}

            .stButton > button:hover {{
                background-color: #ffa733 !important;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# -----------------------------------
# ✅ Interfaz principal
# -----------------------------------
def main():
    set_background("https://image.tmdb.org/t/p/original/p5ozvmdgsmbWe0H8Xk7Rc8SCwAB.jpg")

    st.title("💬 Plataforma de Bienestar Emocional Juvenil")
    st.caption("Proyecto Integrador – Nuevas Tecnologías")

    menu = ["Usuario", "Administrador"]
    opcion = st.sidebar.selectbox("Selecciona tu rol:", menu)

    # ======================================
    # ✅ Vista Usuario
    # ======================================
    if opcion == "Usuario":
        st.header("🧠 Formulario de Bienestar para Jóvenes")
        resultado = mostrar_encuesta()

        if resultado:
            if not resultado["nombre"]:
                st.error("⚠️ Por favor ingresa tu nombre completo.")
            else:
                usuario_id = guardar_usuario({
                    "nombre": resultado["nombre"],
                    "edad": resultado["edad"]
                })

                guardar_encuesta(usuario_id, resultado)

                consejo = generar_consejo_contextual(resultado)

                st.success("✅ Encuesta enviada correctamente.")
                st.info(f"💡 Consejo personalizado: {consejo}")

    # ======================================
    # ✅ Vista Administrador
    # ======================================
    elif opcion == "Administrador":
        st.header("🔐 Panel de Administración")

        if "admin_logged" not in st.session_state:
            st.session_state.admin_logged = False

        if not st.session_state.admin_logged:
            user = st.text_input("Usuario:")
            password = st.text_input("Contraseña:", type="password")

            if st.button("Ingresar"):
                if user == "admin" and password == "1234":
                    st.session_state.admin_logged = True
                    st.success("✅ Acceso concedido")
                else:
                    st.error("❌ Usuario o contraseña incorrectos.")
            return  # Evita mostrar dashboard antes del login

        # ✅ Ya logueado → mostrar dashboard
        encuestas_df = cargar_encuestas()

        if not encuestas_df.empty:
            st.subheader("📊 Análisis de Encuestas")

            # -------------------------
            # Gráfico Bienestar Emocional
            # -------------------------
            
        mostrar_dashboard(encuestas_df)

# -----------------------------------
# ✅ Ejecutar app
# -----------------------------------
if __name__ == "__main__":
    main()
