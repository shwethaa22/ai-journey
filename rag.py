from ai import ai_convo
from embed import get_embeddings
from build_prompt import build_prompt
from search import search
from vector_store import load_store
from confidence import is_confident

def answer_question(question,records):
    vector=get_embeddings(question)
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
    questions=[("direct hit","I'm locked out of my account, what do I do?"),
               ("other chunk","How long until I get my money back?"),
               ("two topics","I want to check my refund status but I forgot my password. What now?"),
               ("absent","Do you offer a student discount?"),
               ("borderline","Can I cancel an order after it has shipped?")]

    for label, question in questions:
        print("="*60)
        print(f"[{label}] {question}")
        result=answer_question(question,records)
        print(f"Answer: {result['answer']}")
        print(f"Sources: {result['source']}")