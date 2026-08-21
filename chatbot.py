import json


def get_reply(message):
    if(len(message)<5):
        return f"The message '{message}' is too short"
    elif(len(message)>5):
        return f"The message '{message}' is too long"
    else:
        return f"The message '{message}' is of perfect length"



    
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
    history.append({"role" : "model", "content":get_reply(user_input)})

with open("history.json","w") as d:
    json.dump(history,d, indent=2)
print(f"The total number of message is {len(history)}")
for item in history:
    print(f"{item['role']} : {item['content']}")
    
       