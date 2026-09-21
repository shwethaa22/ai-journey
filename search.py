from similarity import cos_similarity

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
    records = [
        {"text": "boats",   "vector": [0, 1]},
        {"text": "kittens", "vector": [0.9, 0.1]},
        {"text": "cats",    "vector": [1, 0]}
    ] 
    b=[]
    query=[1,0]
    answer=search(query,records,5)
    print(f"The closest contexts are: {answer}")