import random
lenght_of_the_cryptage = 5
text_to_cypher = input("txt")




def Generate(list_to_cypher,lenght_of_the_cryptage):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    global list_of_letter
    global key
    list_of_letter = []
    key = []
    for letter in list_to_cypher:
        if not letter in list_of_letter:
            a = ""
            for i in range(lenght_of_the_cryptage):
                a += alphabet[random.randint(0,len(alphabet) - 1)]
            key.append(a)
            list_of_letter.append(letter)
            
def Cypher(list_to_cypher,key,list_of_letter):
    global list_cyphered
    list_cyphered = []
    for letter in list_to_cypher:
        list_cyphered.append(key[list_of_letter.index(letter)])
        
def Decypher(list_to_decypher,key,list_of_letter):
    global list_decyphered
    list_decyphered = []
    for letter in list_to_decypher:
        list_decyphered.append(list_of_letter[key.index(letter)])
        
Generate(list(text_to_cypher),lenght_of_the_cryptage)       
Cypher(list(text_to_cypher),key,list_of_letter)
print(list_cyphered)
Decypher(list_cyphered,key,list_of_letter)
print(list_decyphered)        
        
                

    