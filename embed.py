from dotenv import load_dotenv
import os
from urllib import response
import requests
from streamlit import text

load_dotenv()
API_KEY=os.getenv("GEMINI_API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:embedContent?key={API_KEY}"
MODEL = "gemini-embedding-001"

if not API_KEY:
    exit()
    

def get_embeddings(text):
    payload = {
         "model": MODEL,
        "content":{
             "parts": [
                 {
                     "text":text
                 }
             ]
         }
    }
    response = requests.post(URL, json=payload,timeout=10,)
    return response.json()['embedding']['values'][0:5]




if __name__ == "__main__":
    text = input("Enter text to get embeddings: ")
    embeddings = get_embeddings(text)
    print(f"Embeddings for '{text}': {embeddings}")