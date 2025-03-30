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
  contents=[sample_file, f"YOU are marketing assistant. you will give accurate answer on {prompt}. don't give extra explanation just give me exact answer read or thing"])
    result = response.text
    return result
