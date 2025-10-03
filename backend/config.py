import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("ERYTH_API_KEY"))

# Use the correct Gemini model ID
model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Hello Gemini!")
print(response.text)
