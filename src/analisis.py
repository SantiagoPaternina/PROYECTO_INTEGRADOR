import streamlit as st
import pandas as pd
import plotly.express as px

COLOR_NARANJA = "#ff8c00"

def mostrar_dashboard(encuestas_df):

    st.markdown("## 🌗 Gráfico Unificado – SUNBURST de Bienestar Emocional")

    if encuestas_df.empty:
        st.warning("⚠️ No hay datos suficientes para analizar.")
        return

    # ---------------------------
    # ✅ Columnas importantes
    # ---------------------------
    col_emocion = "resp_¿Cómo te sientes hoy?"
    col_sueno = "resp_¿Cómo ha estado tu sueño últimamente?"
    col_estres = "resp_¿Has sentido estrés últimamente?"
    col_apoyo = "resp_¿Sientes apoyo de tus amigos o familia?"
    col_animo = "resp_¿Cómo calificarías tu ánimo general?"

    # ---------------------------
    # ✅ Nivel general de bienestar
    # ---------------------------
    mapping_animo = {"Excelente": 4, "Bueno": 3, "Regular": 2, "Bajo": 1}
    encuestas_df["puntaje_animo"] = encuestas_df[col_animo].map(mapping_animo)

    bienestar_promedio = encuestas_df["puntaje_animo"].mean()

    if bienestar_promedio >= 3.5:
        nivel = "Bienestar Alto"
    elif bienestar_promedio >= 2.5:
        nivel = "Bienestar Medio"
    else:
        nivel = "Bienestar Bajo"

    # ---------------------------
    # ✅ DataFrame Sunburst
    # ---------------------------
    sunburst_df = pd.DataFrame()

    # Círculo central – Bienestar general
    sunburst_df = pd.concat([
        sunburst_df,
        pd.DataFrame({
            "nivel": ["Bienestar General"],
            "categoria": [nivel],
            "subcategoria": [None],
            "valor": [1]
        })
    ])

    # Función para agregar niveles al sunburst
    def agregar_categoria(nombre_categoria, columna_respuestas):
        conteo = encuestas_df[columna_respuestas].value_counts().reset_index()
        conteo.columns = ["respuesta", "cantidad"]

        conteo["nivel"] = "Bienestar General"
        conteo["categoria"] = nombre_categoria
        conteo["subcategoria"] = conteo["respuesta"]
        conteo["valor"] = conteo["cantidad"]

        return conteo[["nivel", "categoria", "subcategoria", "valor"]]

    # Agregar dimensiones importantes
    sunburst_df = pd.concat([
        sunburst_df,
        agregar_categoria("Emoción del Día", col_emocion),
        agregar_categoria("Sueño", col_sueno),
        agregar_categoria("Estrés", col_estres),
        agregar_categoria("Apoyo Social", col_apoyo)
    ])

    # ---------------------------
    # ✅ Gráfico Sunburst Final
    # ---------------------------
    fig = px.sunburst(
        sunburst_df,
        path=["nivel", "categoria", "subcategoria"],
        values="valor",
        color="valor",
        color_continuous_scale=["#ffb766", "#ff8c00", "#cc6e00"],
        title="🌗 Bienestar Emocional – Preguntas Clave",
        width=900,
        height=900
    )

    fig.update_layout(
        title_font_color=COLOR_NARANJA,
        font_color=COLOR_NARANJA,
        plot_bgcolor="#0c0c0c",
        paper_bgcolor="#0c0c0c"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📋 Datos completos analizados")
    st.dataframe(encuestas_df)
