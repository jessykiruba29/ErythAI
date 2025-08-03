from fastapi import FastAPI,UploadFile,File,Form
from fastapi.middleware.cors import CORSMiddleware
from ai import get_explanation
from pdf_reader import extract_text, find_term_value
from ai import model

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/explain")
async def eryth_ai(
    query:str=Form(...),
    file:UploadFile=File(None)
):
    pdf_text=""
    value=None
    if file:
        pdf_text=await extract_text(file)
        value=find_term_value(pdf_text,query)

    explanation=get_explanation(query=query,context=pdf_text,value=value)

    formatted = format_user_response(query, explanation)

    return {
        "term": query,
        "value_in_report": value,
        "explanation": explanation.strip(),     
        "formatted_response": formatted           
    }




def format_user_response(query: str, explanation: str) -> str:
    prompt = f"""
You are a calm, friendly medical assistant.

The user asked:
"{query}"

Here's a raw explanation:
"{explanation}"

Now rephrase it in simple, clear, and non-scary language.
Be reassuring. Avoid panic-inducing terms. Make it sound kind and warm.
and make it SHORT. 
"""

    response = model.generate_content(prompt)
    return response.text.strip()


@app.post("/format")
async def format_reply(
    query: str = Form(...),
    explanation: str = Form(...)
):
    formatted = format_user_response(query, explanation)
    return {
        "formatted_response": formatted
    }








