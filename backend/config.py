from dotenv import load_dotenv
import os
import json
import google.generativeai as genai


load_dotenv()
gemini_api_key=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)
model=genai.GenerativeModel("gemini-1.5-flash")

