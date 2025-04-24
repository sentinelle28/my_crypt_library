from random import randint,choice

key:str = ""

def generate_key(_text:str):
    key:str = ""
    for i in range(8):
        key += str(randint(1,9))
    return key

def crypt(message:str,key:str)->str:
    index:int = 0
    temp:str = ""
    for i in range(len(message)):
        if i%int(key[index]) == 0:
            index += 1
            index %= 7
            temp += message[i]
        else:
            temp+= chr( ( ord(message[i]) + int(key[index]) ) % 255 )
    return temp
        

def uncrypt(message:str,key:str)->str:
    index:int = 0
    temp:str = ""
    for i in range(len(message)):
        if i%int(key[index]) == 0:
            index += 1
            index %= 7
            temp += message[i]
        else:
            temp += chr( ( ord(message[i]) - int(key[index]) ) % 255 )
    return temp
