from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'brak zmiennej')

client = genai.Client()

while True:
    prompt = input("Prompt: ")
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    print(f"GenAI: {response.text}")
