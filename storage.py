import os
import json
from dotenv import load_dotenv


FILE_NAME="history.json"
def load_history(path=FILE_NAME):
    try:
        with open(path, "r") as f:
             history = json.load(f)                      # 1. READ it into a name
             print(f"Loaded {len(history)} previous messages.")   # 2. TALK about it
             return history   
        
    except(FileNotFoundError):
        print(f"New file had been created since it didn't exist")
        return []          
        
    except(json.JSONDecodeError):
        print(f"The file is unreadable, so starting fresh")
        return []

    
    
def save_history(history, path=FILE_NAME):    
    with open(path,"w") as d:
        json.dump(history,d, indent=2)

        