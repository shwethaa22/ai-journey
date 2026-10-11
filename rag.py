from ai import ai_convo
from embed import get_embeddings
from build_prompt import build_prompt
from search import search

def answer_question(question,records):
    vector=get_embeddings(question)
    chunks=[]
    chunk_search=search(vector,records)
    for i in chunk_search:
        chunks.append(i["text"])
    prompt=build_prompt(question, chunks)
    
    response=ai_convo([{"role":"user","content":prompt}])
    return response


if __name__ == "__main__":
    records = load_records()
    print(answer_question("How do I reset my password?", records))