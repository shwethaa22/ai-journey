from ai import ai_convo
from embed import get_embeddings
from build_prompt import build_prompt
from search import search
from vector_store import load_store
from confidence import is_confident

def answer_question(question,records):
    vector=get_embeddings(question)
    print(len(vector))  # length of query embedding
    for rec in records[:5]:
        print(len(rec["vector"]))  # length of stored embeddings
    chunks=[]
    sources=[]

    chunk_search=search(vector,records)
    
    if(not is_confident(chunk_search)):
        return {"answer":"I don't have information about that in my documents." , "source":[]}
    for i in chunk_search:
        chunks.append(i["text"])
        sources.append(i["source"])
    prompt=build_prompt(question, chunks)
    
    response=ai_convo([{"role":"user","content":prompt}])
    return {"answer":response, "source":sources}


if __name__ == "__main__":
    records = load_store()
    print(answer_question("I want to check the status of my refund.But i forgot my password.What to do now?",records))