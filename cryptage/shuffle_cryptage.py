import random
import cryptage.normalise as normal

def Cypher(key:list[int],list_to_decypher:list[str])->list[str]:
    list_cyphered:list[str] = []
    for i in key:
        list_cyphered.append(list_to_decypher[i])
    return list_cyphered
        

def Generate(input:str)->list[int]:
    key:list[int] = []
    for i in range(len(input)):
        while len(key) - 1 !=  i:
            r = random.randint(0,len(input) - 1)
            if not r in key:
                key.append(r)
    return key
                
                
def Decypher(key:list[int],list_to_decypher:list[str])->list[str]:
    list_decyphered:list[str] = []
    for i in range(0,len(list_to_decypher)):
        for ir in key:
            if ir == i:
                list_decyphered.append(list_to_decypher[key.index(ir)])   
    return list_decyphered             
                
                
def generate_key(text:str)->str:
    key:list[int] =Generate(text)
    temp:str = normal.normalised_key(key,"/")
    return temp

def crypt(text:str,key:str)->str:
    list_text:list[str] = list(text)
    n_key:list[str] = normal.unormalized(key,"/")
    i_key:list[int] = []
    for elt in n_key:
        i_key.append(int(elt))
    result:list[str] = Cypher(i_key,list_text)
    return "".join(result)

def uncrypt(text:str,key:str)->str:
    list_text:list[str] = list(text)
    n_key:list[str] = normal.unormalized(key,"/")
    i_key:list[int] = []
    for elt in n_key:
        i_key.append(int(elt))
    result:list[str] = Decypher(i_key,list_text)
    return "".join(result)
    
    
    
    