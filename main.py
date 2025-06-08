# main.py
from chatgpt import ask_chatgpt

def main():
    print("🔍 OSINT Arena | Powered by Configuramos x GPT x Grok")
    prompt = input("Escribe tu pregunta para ChatGPT: ")
    api_key = input("🔑 Introduce tu API Key de OpenAI: ").strip()
    response = ask_chatgpt(prompt, api_key)
    print("\n📎 Respuesta:\n", response)

if __name__ == "__main__":
    main()
