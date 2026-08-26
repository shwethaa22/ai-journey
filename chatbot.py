from storage import load_history, save_history
from ai import ai_convo

<<<<<<< HEAD
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
URL="https://api.groq.com/openai/v1/chat/completions"
MODEL="openai/gpt-oss-20b"
SYSTEM={"role": "system", "content": "You are a helpful assistant.You should never answer in more than two sentences.""Do not give code examples unless explicitly asked. "

  "For greetings or small talk, respond briefly and warmly, then invite a programming question. "

  "For substantive questions unrelated to programming, politely decline and say what you can help with. "

  "If you don't know something, say so rather than guessing." }
=======
>>>>>>> 3bc975dac7563ec7858043a555e751427ca5c7e7

history=load_history()    
   
while(True):
    user_input=input("Provide your input here: ")
    if(user_input=="/quit"):
        break 
    
    history.append({"role" : "user", "content":user_input})
    reply=ai_convo(history)
    history.append({"role" : "assistant", "content":reply})

save_history(history)
print(f"The total number of message is {len(history)}")
for item in history:
    print(f"{item['role']} : {item['content']}")        
       