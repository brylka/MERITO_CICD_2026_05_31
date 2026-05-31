from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'brak zmiennej')

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Cześć, co słychać?"
)

print(response.text)