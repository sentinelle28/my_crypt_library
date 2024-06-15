from random import *
import binascii
def format_hex(hex_to_format):
    temp = list(hex_to_format)
    del temp[0:2]
    
    a = ""
    for elt in temp:
        a+= elt
    return a

def generate_key():
    def generate_hexa():
        return hex(randint(0,255))
    key = format_hex(generate_hexa())
    for i in range(randint(5,10)):
        key += format_hex(generate_hexa())
    print("key:",key)
    return key

def crypt(to_crypt,key):
    def add(i,letter):
        temp = int(begin,base=16) + int(key[i:i+1],base=16) + ord(letter)
        if temp > 127:
            temp -= 127
        return temp
        
        
    begin = key[0:2]
    crypted_message = ""
    index_in_the_text = 0
    while len(crypted_message) < len(to_crypt):
        for i in range(2,len(key)-1,2):
            if len(crypted_message) >= len(to_crypt):
                break
            else:
                crypted_message += chr(add(i,to_crypt[index_in_the_text]))      
                index_in_the_text += 1
    print("crypted message:",crypted_message)
    return crypted_message




def uncrypt(message,key):
    def reduce(i,letter):
        temp = -int(begin,base=16) - int(key[i:i+1],base=16) + ord(letter)
        if temp < 0:
            temp += 127
        return temp
    
    
    
    begin = key[0:2]
    uncrypted_message = ""
    index_in_the_text = 0
    while len(uncrypted_message) < len(message):
        
        for i in range(2,len(key)-1,2):
            if len(uncrypted_message) >= len(message):
                break
            else:
                uncrypted_message += chr(reduce(i,message[index_in_the_text]))      
                index_in_the_text += 1
                
    print("uncrypted message:",uncrypted_message)
    return uncrypted_message



little_key = generate_key()
temp = crypt("my message",little_key)
uncrypt(temp,little_key)