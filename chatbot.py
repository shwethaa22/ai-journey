from storage import load_history, save_history
from ai import ai_convo


    
   
while(True):
    user_input=input("Provide your input here: ")
    if(user_input=="/quit"):
        break 
    history=load_history()
    history.append({"role" : "user", "content":user_input})
    reply=ai_convo(history)
    history.append({"role" : "assistant", "content":reply})

save_history(history)
print(f"The total number of message is {len(history)}")
for item in history:
    print(f"{item['role']} : {item['content']}")        
       