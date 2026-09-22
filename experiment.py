from embed import get_embeddings
from similarity import cos_similarity, magnitude

sentence_a=input("Enter the first sentence")
sentence_b=input("Enter the second sentence")
sentence_c=input("Enter the third sentence")

print("-"*10)
vec_a = get_embeddings(sentence_a)     
vec_b = get_embeddings(sentence_b)
vec_c = get_embeddings(sentence_c)

score1 = cos_similarity(vec_a, vec_b)
score2 = cos_similarity(vec_a, vec_c)
score3 = cos_similarity(vec_c, vec_b)



print(f"The magnitude of the embeddings are : {magnitude(vec_a)},{magnitude(vec_b)} and {magnitude(vec_c)}")


print(f"The cosine similarities are : {score1},{score2} and {score3}")