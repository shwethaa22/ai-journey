from similarity import cos_similarity
from vector_store import load_store

def get_score(result):
    return result["score"]

def search(query_vector, records, top_k=3):
    results=[]
    for i in range(len(records)):
        a={"text":records[i]["text"],"score":cos_similarity(query_vector,records[i]["vector"])}
        results.append(a)
    sorted_result=sorted(results,key=get_score, reverse=True)
    return sorted_result[0:top_k]    
  
 
if __name__=="__main__":
    #text=[
     #    "To reset your password, go to the settings menu.",
      #    "Refunds are processed within 5-7 business days.", 
    #    "Our office is open from 9 AM to 5 PM."
    #] 
    #records=[{"text":text[i],"vector":get_embeddings(text[i])} for i in range(len(text))]
    #b=[]
    #query=get_embeddings("I can't log into my account, how do i recover my account?")
   # answer=search(query,records,5)
    #print(f"The closest contexts are: {answer}")
    #TESTING THE LOAD_VECTOR FUNCTION:
    records=load_store()
    query=[1,0]
    print(search(query, records, top_k=2))