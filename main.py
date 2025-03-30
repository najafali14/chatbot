from fastapi import FastAPI
from google import genai
from google.genai import types
import pathlib
import httpx
app = FastAPI()

@app.post("/")
def Chatbot(prompt):
    client = genai.Client(api_key="AIzaSyBo2b6UyVbCepoxQwEgP91FFHx_v-bOAKI")

# Retrieve the PDF
    file_path = pathlib.Path('nazim.pdf')

# Upload the PDF using the File API
    sample_file = client.files.upload(
  file=file_path,
)

    # prompt="Summarize this document"

    response = client.models.generate_content(
  model="gemini-1.5-flash",
  contents=[sample_file, f"""You are Nazim, an expert marketing assistant for Shopify brands, developed by Najaf Ali (github.com/najafali14).  
Your role is to provide clear, human-like responses to marketing and business-related queries.  

- Always give an accurate and precise answer to: '{prompt}'.  
- Think critically and respond as a human expert would.  
- Ensure the response is relevant, insightful, and valuable.  
- Avoid unnecessary explanations; focus on delivering the best possible answer."""  
])
    result = response.text
    return result
