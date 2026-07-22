import os
import cohere
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def generate_response(prompt):
    prompt = f"Answer in one short sentence only:\n{prompt}"
    response = co.chat(
        model="command-a-03-2025",
        message=prompt
    )

    return response.text