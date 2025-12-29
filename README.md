# Simple AI Agent

Un agente de IA simple que utiliza la API de OpenRouter para interactuar con modelos de lenguaje.

## Descripción

Este proyecto es un ejemplo básico de cómo crear un agente de IA utilizando Python y la API de OpenRouter. El script envía un mensaje a un modelo de IA y muestra la respuesta en la consola.

## Características

- Comunicación con modelos de IA a través de OpenRouter
- Uso de variables de entorno para gestión segura de API keys
- Implementación simple y fácil de entender
- Utiliza el modelo gratuito Mistral Devstral 2512

## Requisitos

- Python 3.x
- Biblioteca `requests`

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/AmOrFeU86/simple-ai-agent.git
cd simple-ai-agent
```

2. Instala las dependencias:
```bash
pip install requests
```

3. Configura tu API key de OpenRouter:
   - Opción 1: Configura una variable de entorno:
     ```bash
     export OPENROUTER_API_KEY="tu_api_key_aqui"
     ```
   - Opción 2: Edita el archivo `hello.py` y reemplaza `TU_API_KEY_AQUI` con tu API key

## Uso

Ejecuta el script:
```bash
python hello.py
```

El script enviará el mensaje "buenas" al modelo de IA y mostrará la respuesta.

## Configuración

Puedes modificar los siguientes parámetros en `hello.py`:

- **Modelo**: Cambia el valor de `model` en el objeto `data` para usar diferentes modelos disponibles en OpenRouter
- **Mensaje**: Modifica el contenido del mensaje en `messages` para cambiar lo que le preguntas al agente

## Obtener una API Key

Para obtener tu API key de OpenRouter:
1. Visita [OpenRouter.ai](https://openrouter.ai/)
2. Crea una cuenta o inicia sesión
3. Genera tu API key en el panel de control

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y personal.
