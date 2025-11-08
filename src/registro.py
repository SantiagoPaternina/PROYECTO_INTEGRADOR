import streamlit as st

def login_admin():
    st.subheader("🔐 Inicio de Sesión (Solo Admin)")
    user = st.text_input("Usuario")
    pwd = st.text_input("Contraseña", type="password")

    if st.button("Iniciar Sesión"):
        if user == "admin" and pwd == "1234":
            st.success("Acceso concedido ✅")
            return True
        else:
            st.error("Usuario o contraseña incorrectos ❌")
    return False

