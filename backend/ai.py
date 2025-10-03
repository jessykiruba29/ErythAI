import google.generativeai as genai
from config import model

def get_explanation(query:str,context:str="",value:str=None)->str:
    prompt=f"""
You are a medical AI assisstant. Explain the following medical term in simple words to someone who doesnt know any medical term.
Term: {query}

if context from lab report is given, and if the user wants to know summary of the report, read whole pdf and summarize in simple words....ELSE if they ask for a specific term from pdf include patient's value from pdf and explain what it means in simple words
Patient report:{context}

Detected value: {value if value else 'N/A'}

Your response should be concise, beginner-friendly, and medically accurate.
"""
    response=model.generate_content(prompt)
    return response.text.strip()
