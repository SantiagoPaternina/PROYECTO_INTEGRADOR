import requests

def analizar_estado(respuestas):
    """
    Analiza las respuestas del usuario y determina un estado emocional general.
    Retorna una etiqueta: 'positivo', 'neutral' o 'negativo'.
    """
    # Palabras clave de ánimo
    positivo = ["feliz", "motivado", "excelente", "bueno"]
    negativo = ["triste", "ansioso", "bajo", "mal", "cansado"]

    score = 0
    for r in respuestas.values():
        r = str(r).lower()
        if any(p in r for p in positivo):
            score += 1
        elif any(n in r for n in negativo):
            score -= 1

    if score > 1:
        return "positivo"
    elif score < 0:
        return "negativo"
    else:
        return "neutral"


def generar_consejo_contextual(respuestas):
    """
    Genera un consejo de bienestar personalizado basado en el estado emocional.
    Utiliza Hugging Face Inference API (sin clave, gratis).
    """
    estado_general = analizar_estado(respuestas)
    emociones = respuestas.get("¿Cómo te sientes hoy?", "neutro")

    # Prompts diferentes según el tipo de ánimo
    if estado_general == "positivo":
        prompt = (
            f"Un joven se siente {emociones}. Escríbele un consejo breve en español para mantener su bienestar emocional, "
            "agradeciendo lo positivo que vive y reforzando hábitos sanos."
        )
    elif estado_general == "negativo":
        prompt = (
            f"Un joven se siente {emociones}. Dale un consejo breve, empático y realista en español, "
            "ofreciendo apoyo emocional, esperanza y una acción pequeña para mejorar su día."
        )
    else:
        prompt = (
            f"Un joven se siente {emociones}. Escribe un consejo equilibrado, motivador y positivo en español "
            "para mantener la calma y fortalecer su salud mental."
        )

    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2",
            headers={"Content-Type": "application/json"},
            json={"inputs": prompt},
            timeout=20
        )

        if response.status_code == 200:
            output = response.json()
            if isinstance(output, list) and "generated_text" in output[0]:
                return output[0]["generated_text"].strip()
        # fallback
        if estado_general == "positivo":
            return "¡Qué bueno verte tan bien! Mantén tus hábitos positivos y comparte tu energía con quienes te rodean 💪"
        elif estado_general == "negativo":
            return "No estás solo. Hablar con alguien de confianza y darte un descanso puede ayudarte más de lo que crees ❤️"
        else:
            return "Cada día es una nueva oportunidad para sentirte mejor. Cuida tu descanso y rodéate de cosas que te inspiren 🌱"
    except Exception:
        if estado_general == "positivo":
            return "Sigue disfrutando las pequeñas cosas que te hacen sonreír 😊"
        elif estado_general == "negativo":
            return "Recuerda que pedir ayuda también es una muestra de fortaleza. Tómate un respiro 💛"
        else:
            return "Un paso a la vez. Mantén el equilibrio y celebra tus logros 🕊️"