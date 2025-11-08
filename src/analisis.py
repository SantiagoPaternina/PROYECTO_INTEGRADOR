import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def mostrar_dashboard(encuestas_df):
    if encuestas_df.empty:
        st.warning("⚠️ No hay datos disponibles aún.")
        return

    st.subheader("📊 Análisis General del Bienestar Emocional")

    st.write("### Resumen de datos")
    st.dataframe(encuestas_df.tail())

    # Gráfico 1 - Conteo por estado emocional
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.countplot(x="¿Cómo te sientes hoy?", data=encuestas_df, ax=ax)
    ax.set_title("Distribución del estado emocional")
    st.pyplot(fig)

    # Gráfico 2 - Tendencia de edad y ánimo
    st.write("### Promedio de ánimo por edad")
    if "¿Cómo calificarías tu ánimo general?" in encuestas_df.columns:
        mapping = {"Excelente": 4, "Bueno": 3, "Regular": 2, "Bajo": 1}
        encuestas_df["puntaje_animo"] = encuestas_df["¿Cómo calificarías tu ánimo general?"].map(mapping)
        promedio = encuestas_df.groupby("edad")["puntaje_animo"].mean().reset_index()

        fig2, ax2 = plt.subplots(figsize=(6, 3))
        sns.lineplot(x="edad", y="puntaje_animo", data=promedio, ax=ax2, marker="o", color="#4a90e2")
        ax2.set_title("Tendencia de ánimo promedio por edad")
        st.pyplot(fig2)
