from random import randint


dict_tripplet:dict[int, list[str]] = {
    0:["A","Z","U"],
                 1:["O","Q","F"],
                 3:["G"," ","I"],
                 4:["J","X","P"],
                 5:["M","C","D"],
                 6:["L","S","R"],
                 7:["E","T","N"],
                 8:["B","W","K"],
                 9:["Y","V","H"]}

def generate_key(_text:str)->str:
    return "BE CAREFUL WE ONLY TAKE LETTERS OR SPACE"

def crypt(message:str,_key:str)->str:
    message_crypter:str = ""
    for letter in message:
        key:int = find_in_dict(letter)
        index:int = dict_tripplet[key].index(str(letter).upper())
        message_crypter += str(key)+ str(index + 3*randint(1,2))
        
    return message_crypter
         
def find_in_dict(letter:str)->int:
    for key in dict_tripplet:
        if str(letter).upper() in dict_tripplet[key]:
            return key
  
def uncrypt(message:str,_key:str)->str:
    text_solved:str = ""
    for i in range(0,len(message)-1,2):
        text_solved += dict_tripplet[int(message[i])][int(message[i+1])%3]
    return str(text_solved).lower()
        
