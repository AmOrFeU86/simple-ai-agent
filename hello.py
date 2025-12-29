import requests
import os

# Coloca tu API key aquí o mejor como variable de entorno
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") or "TU_API_KEY_AQUI"

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    # Opcionales pero recomendados por OpenRouter
    "HTTP-Referer": "http://localhost",
    "X-Title": "hello-example"
}

data = {
    "model": "mistralai/devstral-2512:free",  # puedes cambiar el modelo
    "messages": [
        {"role": "user", "content": "buenas"}
    ]
}

response = requests.post(url, headers=headers, json=data)

result = response.json()

# Imprime la respuesta del modelo
print(result["choices"][0]["message"]["content"])
