from speech_to_text import speech_to_text
from llm import generate_response
from text_to_speech import text_to_speech

print("===================================")
print(" Voice-to-Voice AI Assistant")
print(" Say 'exit' to quit")
print("===================================")

while True:

    text = speech_to_text()

    print(f"\nYou: {text}")

    text = text.strip().lower()

    exit_words = [
        "exit",
        "quit",
        "bye",
        "goodbye",
        "باي",
        "مع السلامة",
        "وداعا",
        "وداعاً"
    ]

    if any(word in text for word in exit_words):
        print("Goodbye!")
        break

    reply = generate_response(text)

    print(f"\nAssistant: {reply}")

    text_to_speech(reply)