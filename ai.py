from dotenv import load_dotenv
import os
from urllib import response
import requests

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
URL="https://api.groq.com/openai/v1/chat/completions"
MODEL="openai/gpt-oss-20b"
SYSTEM={"role": "system", "content": "You are a helpful assistant." }

if not API_KEY:
    exit()
    
    
def ai_convo(messages):
    response=requests.post(
        URL,
        headers={"Authorization":f"Bearer {API_KEY}"},
        json={
            "messages": [SYSTEM] + messages,
            "model": MODEL,
            "temperature": 0.7,
        },
        timeout=10,
    )  
    if response.status_code != 200:
        return f"API error: {response.status_code} - {response.text[:150]}"
    data=response.json()
    print(f"tokens used: {data["usage"]["total_tokens"]}")
    return(data["choices"][0]["message"]["content"])
    