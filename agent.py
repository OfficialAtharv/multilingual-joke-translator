import os
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Load model (free tier friendly)
model = genai.GenerativeModel("gemini-2.5-flash")

SYSTEM_PROMPT = """
You are a multilingual AI assistant.

The user will give a joke in English.
Translate the joke into:

1. French
2. Spanish
3. Arabic

Rules:
- Preserve humor and meaning
- Do NOT explain the joke
- Do NOT add extra text

Return the output EXACTLY in this format:

French:
<translation>

Spanish:
<translation>

Arabic:
<translation>
"""


def translate_joke(joke: str) -> str:
    response = model.generate_content(
        SYSTEM_PROMPT + "\n\nJoke:\n" + joke
    )
    return response.text


def main():
    print("🎭 Joke Translator (English → French / Spanish / Arabic)")
    print("Type 'exit' to quit\n")

    while True:
        joke = input("Joke: ")

        if joke.lower() == "exit":
            break

        result = translate_joke(joke)
        print("\nTranslation:\n")
        print(result)
        print("-" * 40)


if __name__ == "__main__":
    main()
