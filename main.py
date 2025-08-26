import json
import asyncio
from connection import model, config, external_client  

chat_history = []

async def translator():
    print("Welcome to Translator Agent")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter text and target language (e.g. 'Hello -> Urdu'): ")

        if user_input.lower() == "exit":
            break

        chat_history.append({"role": "user", "content": f"Translate only into {user_input} and give only the translated text. No explanations, no roman script."})

        try:
            response = await external_client.chat.completions.create(
                model=model.model,
                messages=chat_history
            )

            translated_text = response.choices[0].message.content.strip()
            print(f"\n Translation:\n{translated_text}\n")

            chat_history.append({"role": "assistant", "content": translated_text})

        except Exception as e:
            print(f" Error: {str(e)}")

    with open("translator_history.json", "w", encoding="utf-8") as f:
        json.dump(chat_history, f, indent=2, ensure_ascii=False)

    print("Chat history saved successfully!")

if __name__ == "__main__":
    asyncio.run(translator())
