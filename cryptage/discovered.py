import random
lenght_of_the_cryptage = 5





def generate_key(text_to_cypher):
    list_to_cypher = list(text_to_cypher)
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    global list_of_letter
    list_of_letter = []
    key = []
    for letter in list_to_cypher:
        if not letter in list_of_letter:
            a = ""
            for i in range(lenght_of_the_cryptage):
                a += alphabet[random.randint(0,len(alphabet) - 1)]
            key.append(a)
            list_of_letter.append(letter)
    return "".join(key)
            
def crypt(text_to_cypher,key):
    list_to_cypher = list(text_to_cypher)
    list_cyphered = []
    for letter in list_to_cypher:
        list_cyphered.append(key[list_of_letter.index(letter)])
    return "".join(list_cyphered)
        
def uncrypt(text_to_cypher,key):
    list_to_decypher = list(text_to_cypher)
    list_decyphered = []
    for letter in list_to_decypher:
        list_decyphered.append(list_of_letter[key.index(letter)])
    return "".join(list_decyphered)          
        
                

    