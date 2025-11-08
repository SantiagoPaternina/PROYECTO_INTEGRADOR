# Proyecto Integrador - Monitoreo del Estado Emocional de Jóvenes

Este proyecto busca **monitorear el estado emocional y mental de jóvenes en contextos vulnerables**, usando encuestas simples y análisis de datos en Python.  
La idea es identificar patrones, dar alertas tempranas y ofrecer recursos de apoyo.

---

## 📌 Funcionalidad Principal
- Registro de usuarios y su perfil emocional.  
- Encuestas periódicas sobre estado de ánimo y hábitos.  
- Almacenamiento de datos en archivos `.json` y `.csv`.  
- Panel básico de visualización con gráficos.  
- Recomendaciones y alertas según los resultados.  

---

## 🛠️ Estructura del Proyecto
MOMENTO 2/
│── data/
│ ├── usuarios.csv # Base de datos en formato CSV
│ ├── usuarios.json # Registro de usuarios en JSON
│
│── informes/
│ ├── informe_tecnico.md # Documento explicativo del proceso
│ ├── planeacion_proyecto.md
│
│── src/
│ ├── almacenamiento.py # Manejo de archivos JSON y CSV
│ ├── encuesta.py # Simulación de encuestas
│ ├── analisis.py # Limpieza, análisis y visualización de datos
│ ├── main.py # Punto de inicio del sistema

---

## 🚀 Proceso del Proyecto

1. **Planeación:**  
   Se definió el objetivo, el alcance y las funcionalidades principales.

2. **Encuestas y Registro:**  
   Se desarrolló un módulo que permite registrar usuarios y realizar encuestas básicas sobre emociones y hábitos.

3. **Almacenamiento de datos:**  
   Los datos se guardan en `usuarios.json` y se exportan a `usuarios.csv` para análisis más sencillo.

4. **Análisis de datos (Python + Pandas):**  
   - Lectura de datos desde CSV.  
   - Estadísticas simples (promedios, correlaciones).  
   - Detección de patrones básicos.  

5. **Visualización (Matplotlib + Seaborn):**  
   - Gráficos de barras y líneas para mostrar tendencias.  
   - Evolución del bienestar en el tiempo.  
   - Alertas de riesgo según puntajes emocionales.

---

## 📊 Ejemplo de Resultados
- Estado emocional promedio por grupo.  
- Tendencias de ánimo según las encuestas.  
- Alertas cuando un usuario presenta valores críticos.  

---

## ⚙️ Instalación y Ejecución

1. Clonar el repositorio.  
2. Instalar dependencias:

```bash
pip install -r requirements.txt

python src/main.py
python src/analisis.py
Conclusión
Este proyecto demuestra cómo usar Python para recolectar, almacenar y analizar información emocional, de manera sencilla pero útil.
Aunque es un prototipo, sirve como base para crear herramientas más completas en el futuro.

# 📌 Cómo Usar el Proyecto

1. **Ejecutar encuestas y registrar usuarios**  
   - Abre la terminal en la carpeta del proyecto.  
   - Ejecuta:  
     ```bash
     python src/main.py
     ```  
   - Ingresa los datos solicitados:  
     - Nombre (solo letras).  
     - Edad (1 a 100).  
     - Estado emocional (escala de 1 a 5).  
   - El sistema validará los datos y guardará la información.

---

2. **Elegir formato de guardado**  
   Al final del registro puedes decidir:  
   - Guardar en **CSV**.  
   - Guardar en **JSON**.  
   - Guardar en **ambos formatos**.  

Los archivos se almacenan automáticamente en la carpeta `/data`.

---

3. **Analizar los datos registrados**  
   - Ejecuta el análisis con:  
     ```bash
     python src/analisis.py
     ```  
   - Se mostrará en consola un **resumen de los datos**.  
   - Además, se generarán **gráficos de tendencias** y alertas según los puntajes.

---

4. **Revisar los informes**  
   En la carpeta `/informes` encontrarás:  
   - `informe_tecnico.md` → explicación del proceso.  
   - `planeacion_proyecto.md` → planificación inicial del proyecto.

---

✅ Con esto podrás **registrar, almacenar y analizar encuestas emocionales** de manera rápida y sencilla.
