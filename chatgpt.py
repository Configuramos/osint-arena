# chatgpt.py

import openai
import os

class ChatGPT:
    def __init__(self, api_key=None, model="gpt-4"):
        """
        Inicializa la clase ChatGPT con una clave API y modelo por defecto (gpt-4).
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        openai.api_key = self.api_key

    def ask(self, prompt, temperature=0.7, max_tokens=1000):
        """
        Envía un prompt al modelo y devuelve la respuesta generada.

        :param prompt: Texto de entrada.
        :param temperature: Grado de aleatoriedad (0.0 a 1.0).
        :param max_tokens: Límite de tokens de respuesta.
        :return: Respuesta generada por ChatGPT.
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message["content"].strip()
        except Exception as e:
            return f"[ERROR] {str(e)}"
