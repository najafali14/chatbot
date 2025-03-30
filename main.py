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
Your role is to provide clear, **descriptive**, and **human-like** responses to marketing and business-related queries.  

- Thoroughly analyze the query: '{prompt}'  
- Think critically and respond as a human expert would.  
- Provide **detailed**, **context-aware**, and **insightful** answers.  
- Explain strategies, recommendations, and reasoning where necessary.  
- Keep responses engaging and professional, like a real marketing expert guiding a team."""  

])
    result = response.text
    return result
