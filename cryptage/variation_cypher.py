from random import *

def format_hex(hex_to_format:str)->str:
    temp:list[str] = list(hex_to_format)
    del temp[0:2]
    a:str = ""
    for elt in temp:
        a+= elt
    return a

def generate_key(_text_to_crypher:str)->str:
    def generate_hexa():
        return hex(randint(0,255))
    key:str = format_hex(generate_hexa())
    for i in range(randint(5,10)):
        key += format_hex(generate_hexa())
    return key

def crypt(to_crypt:str,key:str)->str:
    def add(i:int,letter:str)->int:
        temp:int = int(begin,base=16) + int(key[i:i+1],base=16) + ord(letter)
        if temp > 127:
            temp -= 127
        return temp
        
        
    begin:str = key[0:2]
    crypted_message:str = ""
    index_in_the_text:int = 0
    while len(crypted_message) < len(to_crypt):
        for i in range(2,len(key)-1,2):
            if len(crypted_message) >= len(to_crypt):
                break
            else:
                crypted_message += chr(add(i,to_crypt[index_in_the_text]))      
                index_in_the_text += 1
    return crypted_message




def uncrypt(message:str,key:str)->str:
    def reduce(i:int,letter:str)->int:
        temp:int = -int(begin,base=16) - int(key[i:i+1],base=16) + ord(letter)
        if temp < 0:
            temp += 127
        return temp
    
    
    
    begin:str = key[0:2]
    uncrypted_message:str = ""
    index_in_the_text:int = 0
    while len(uncrypted_message) < len(message):
        
        for i in range(2,len(key)-1,2):
            if len(uncrypted_message) >= len(message):
                break
            else:
                uncrypted_message += chr(reduce(i,message[index_in_the_text]))      
                index_in_the_text += 1
                
    return uncrypted_message

