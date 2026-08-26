import json
import os
from urllib import response
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
URL="https://api.groq.com/openai/v1/chat/completions"
MODEL="openai/gpt-oss-20b"
SYSTEM={"role": "system", "content": "You are a helpful assistant.You should never answer in more than two sentences.""Do not give code examples unless explicitly asked. "

  "For greetings or small talk, respond briefly and warmly, then invite a programming question. "

  "For substantive questions unrelated to programming, politely decline and say what you can help with. "

  "If you don't know something, say so rather than guessing." }

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

    
try:
    with open("history.json","r") as f:
        history=json.load(f)  
        print(f"All {len(history)} old messages have been loaded into the list")
except(FileNotFoundError):
    history=[]          
    print(f"New file had been created since it didn't exist")
except(json.JSONDecodeError):
    print(f"The file is unreadable, so starting fresh")
    history=[]    
while(True):
    user_input=input("Provide your input here: ")
    if(user_input=="/quit"):
        break 
    
    history.append({"role" : "user", "content":user_input})
    reply=ai_convo(history)
    history.append({"role" : "assistant", "content":reply})

with open("history.json","w") as d:
    json.dump(history,d, indent=2)
print(f"The total number of message is {len(history)}")
for item in history:
    print(f"{item['role']} : {item['content']}")
    
       