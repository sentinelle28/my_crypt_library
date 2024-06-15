import random
text_to_cypher = input("txt")
key = []
list_t = []

def Cypher(key,list_to_decypher):
    global list_cyphered 
    list_cyphered = []
    for i in key:
        list_cyphered.append(list_to_decypher[i])
        

def Generate(key,input):
    for i in range(len(input)):
        while len(key) - 1 !=  i:
            r = random.randint(0,len(input) - 1)
            if not r in key:
                key.append(r)
                
                
def Decypher(key,list_to_decypher):
    global list_decyphered
    list_decyphered = []
    for i in range(0,len(list_to_decypher)):
        for ir in key:
            if ir == i:
                list_decyphered.append(list_to_decypher[key.index(ir)])                
                
                
Generate(key,list(text_to_cypher))
Cypher(key,list(text_to_cypher))
print(list_cyphered)
Decypher(key,list_cyphered)
print(list_decyphered)