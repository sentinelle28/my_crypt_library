import random



def Generate(list_to_cypher:str):
    element_to_put:int =  0
    list_of_letter:list = []#:list[str]
    key:list = []#list[int]
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
    return key,list_of_letter,referencement,element_to_put
    
def Cypher(list_to_cypher:list,key:list,list_of_letter:list,referencement:int):
    list_cyphered = []
    for i in range(len(list_to_cypher)):
        search = key[list_of_letter.index(list_to_cypher[i])] + (referencement + (i + 1))
        list_cyphered.append(search)
    return list_cyphered
        
def Decypher(list_to_decypher:list,key:list,list_of_letter:list,referencement:int):
    list_decyphered = []
    for i in range(len(list_to_decypher)):
        print(list_to_decypher[i])
        search = list_to_decypher[i] - (referencement + (i + 1))
        list_decyphered.append(list_of_letter[key.index(search)])
    return list_decyphered
 
def normalised_key(object_list,element_to_put:str):
    normalised_key_text = ""
    for object in object_list:
        normalised_key_text += str(object)
        normalised_key_text += str(element_to_put)
    return normalised_key_text
       
def unormalized(text:str,element_to_put:str):
    extracted_list = [] #list[int]
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
 
"""
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
            
        
     



"""  

#normalised key:  13/5/15/20/8/11/9/6/1/4/23/10/18/22/16/24/7/3/19/17/14/2/12/
#normalised letter key:  y/o/u/ /s/c/e/f/l/n/r/p/t/h/i/m/a/g/k/:/I/b/w/
#third key:43
#Fourth key: 21   


def extract_key(text:str,element_to_put:str):        
    return text.split(str(element_to_put)) 

key_1 = unormalized("13/5/15/20/8/11/9/6/1/4/23/10/18/22/16/24/7/3/19/17/14/2/12/","/") #list[int]
key_2 = extract_key("y/o/u/ /s/c/e/f/l/n/r/p/t/h/i/m/a/g/k/:/I/b/w/","/") #list[str]
key_3 = 43 #int
key_4 = 18 #int

#message = "258608778168818081808242820481308154821082888391819887682008378826481618360830083648297819682908330874489684958408849083608407826687028120845182108430848487658460851781104858881100811738572831889728121081064862781392810628126081464824881134813448156087268938812248207877084978728116881110875088368770814828869811208145881312814948159681870818068870896883568198089108193281023818881140896081067849089908110087078153081751814568315810608224782268810908121081887811208259981254820708812822238259681785825208278381342861581240813758239483818192081548811708131081452829268281482430828568287781380823638308083243832668314685768232081460816178296817888150081661824328306082310832558171682669815808174983840828988340283912865682970834868400881848830428187081197830968207684002817508193682301835608214883780818108200281830855285558186082244856482079824708191082112811588582835108274482758819808" 
message = "1501877182418521884181351864181021821618304181801842188818322182401822518182182971833618464184801893182881856118306181751839618481183041811718401841182941860218308184051859818658184321863718300182551872818"
message_1 = unormalized(message,str(key_4)) #list[int] 1/4
print(message_1)
message_2 = Decypher(message_1,key_1,key_2,key_3) #4/4
print(message_2)
