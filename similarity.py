import math

def dot_product(list1,list2):
    if(len(list1)!=len(list2)):
        raise ValueError("Lists must have the same length")
    total=0
    for i in range(0,len(list1)):
        total+=list1[i]*list2[i]
    return total

def magnitude(list1):
    total=0
    for i in range(len(list1)):
        total+=list1[i]**2
    return math.sqrt(total)


def cos_similarity(list1,list2):
    if (magnitude(list1)*magnitude(list2))==0:
         raise ZeroDivisionError("Magnitude is Zero")
    return dot_product(list1,list2)/(magnitude(list1)*magnitude(list2))  

if __name__=="__main__":
    print(cos_similarity([0, 0], [1, 2]))
    
