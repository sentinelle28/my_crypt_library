import random


def Generate(list_to_cypher):
    global list_of_letter
    global key
    global referencement
    global element_to_put
    element_to_put =  0
    list_of_letter = []
    key = []
    for letter in list_to_cypher:
        if not letter in list_of_letter:
            list_of_letter.append(letter)
            
    for i in list_of_letter:
        while True:
            r = random.randint(1,len(list_of_letter) + 1)
            if not r in key:
                key.append(r)
                break
    
    
    referencement = random.randint(2,len(key)*2)
    it = 0
    while True:
        it += 1
        if not it in key:
            element_to_put = it
            break
    
def Cypher(list_to_cypher,key,list_of_letter):
    global list_cyphered
    list_cyphered = []
    for i in range(len(list_to_cypher)):
        search = key[list_of_letter.index(list_to_cypher[i])] + (referencement + (i + 1))
        list_cyphered.append(search)
        
def Decypher(list_to_decypher,key,list_of_letter):
    global list_decyphered
    list_decyphered = []
    for i in range(len(list_to_decypher)):
        search = list_to_decypher[i] - (referencement + (i + 1))
        list_decyphered.append(list_of_letter[key.index(search)])
 
def normalised_key(object_list,element_to_put):
    normalised_key_text = ""
    for object in object_list:
        normalised_key_text += str(object)
        normalised_key_text += str(element_to_put)
    return normalised_key_text
       
def unormalized(text,element_to_put):
    extracted_list = []
    elements = text.split(str(element_to_put))
    for element in elements:
        if element:
            extracted_list.append(int(element))   # pour les chiffres sinon decypher ne marche pas...
            
    return extracted_list 
 
def assemble_text(liste):
    text = ""
    for i in liste:
        text+= i
    return text
    
while True:
    choice = input("Advanced subsitution with number cryptage \n 1:Generate the Key \n 2:Cyphered the text \n 3:Decyphered a text \n 4: Unnormalized key \n 5: quit \nyour choice:")
    if choice.isnumeric():
        #generate keys 
        choice = int(choice)
        if choice == 1:
            text_to_cypher = input("text you want to crypt:") 
            Generate(list(text_to_cypher))
            #key  showing for the users       
            print("normalised key: ",normalised_key(key,"/"))              
            print("normalised letter key: ",normalised_key(list_of_letter,"/"))
            print(f"third key:{referencement}")
            print(f"Fourth key: {element_to_put}")
                        
        #cypher the text      
        if choice == 2:
            if len(key) != 0 and referencement != None and len(list_of_letter) != 0:
                if text_to_cypher != None:
                    Cypher(list(text_to_cypher),key,list_of_letter)
                    list_cyphered = normalised_key(list_cyphered,element_to_put)
                    print(list_cyphered)
                else:
                    text_to_cypher = input("text you want to crypt:")
                    Cypher(list(text_to_cypher),key,list_of_letter)
                    list_cyphered = normalised_key(list_cyphered,element_to_put)
                    print(list_cyphered)
            else:
                print("you don't have a key")
        #decypher        
        if choice == 3:
            if len(key) != 0 and referencement != None and len(list_of_letter) != 0:
                if len(list_cyphered) != 0:
                    Decypher(unormalized(list_cyphered,element_to_put),key,list_of_letter)
                    print(assemble_text(list_decyphered))
                else:
                    text_to_decyphered = input("text you want to decrypt:")
                    Decypher(unormalized(text_to_decyphered,element_to_put),key,list_of_letter)
                    print(assemble_text(list_decyphered)) 
            else:
                print("you don't have a key")
        #get key        
        if choice == 4:
            key.clear()
            key = unormalized(input("Enter the normalised key"),"/")
            list_of_letter.clear()
            list_of_letter = input("Enter the normalised letter key").split("/")
            referencement = int(input("Enter the third key"))
            element_to_put = int(input("enter the fourth key"))
        
        if choice == 5:
            break
            
        
     


#normalised key:  13/5/15/20/8/11/9/6/1/4/23/10/18/22/16/24/7/3/19/17/14/2/12/
#normalised letter key:  y/o/u/ /s/c/e/f/l/n/r/p/t/h/i/m/a/g/k/:/I/b/w/
#third key:43
#Fourth key: 21
    