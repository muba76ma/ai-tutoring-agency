import requests

# Adresse du proxy local (cliproxy)
PROXY_URL = "http://localhost:8317/v1/chat/completions"

def call_llm(messages: list) -> str:
    payload = {
        "model": "gpt-4o",          # ou "gemini-2.5-pro"
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 500
    }

    response = requests.post(PROXY_URL, json=payload, timeout=30)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
