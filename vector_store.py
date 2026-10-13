import json



def save_store(records, path="vector_store.json"):
   with open(path,"w") as d:
        json.dump(records,d,indent=2)
        print(f"Saved {len(records)} records.")                
    
    
def load_store(path="vector_store.json", expected_model=None):
    try:
        with open(path,"r") as f:
            records=json.load(f)   
            return records
    except FileNotFoundError:
        return [] 
    
if __name__ == "__main__":
    records = [
        {"text": "To reset your password, go to Account Settings.", "vector": get_embeddings("To reset your password, go to Account Settings and click on 'Reset Password'.")},
        {"text": "Refunds are processed within 5-7 business days.", "vector": get_embeddings("Refunds are processed within 5-7 business days.")},
    ]
    save_store(records)
    back = load_store()
    print("same again:", back == records)    