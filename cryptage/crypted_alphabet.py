import random
import time
def Generate_key_alphabet():
    global key_1
    global key_2
    element_to_clear = 0
    key_1 = ""
    key_2 = ""
    alphabet_1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    alphabet_2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    while bool(alphabet_2):
        element_to_clear = random.randint(0,len(alphabet_1) - 1)
        key_1 += alphabet_1[element_to_clear]
        alphabet_1.remove(alphabet_1[element_to_clear])
        element_to_clear = random.randint(0,len(alphabet_2) - 1)
        key_2 += alphabet_2[element_to_clear]
        alphabet_2.remove(alphabet_2[element_to_clear])
        
        
        
        
    print(key_1,"\n",key_2)    
    
  

def Crypt_alphabet_code(key_1, key_2, list_to_crypt):
    global var_crypted
    var_crypted = ""
    list_crypted = []
    list_crypted.clear
    index = 0
    for letters in list(list_to_crypt):
        if letters == "a":
            if index%2 == 0:
                list_crypted.append(key_1[0])
            else:
                list_crypted.append(key_2[0])  
        if letters == "b":
            if index%2 == 0:
                list_crypted.append(key_1[1])
            else:
                list_crypted.append(key_2[1])
        if letters == "c":
            if index%2 == 0:
                list_crypted.append(key_1[2])
            else:
                list_crypted.append(key_2[2])
        if letters == "d":
            if index%2 == 0:
                list_crypted.append(key_1[3])
            else:
                list_crypted.append(key_2[3])
        if letters == "e":
            if index%2 == 0:
                list_crypted.append(key_1[4])
            else:
                list_crypted.append(key_2[4])
        if letters == "f":
            if index%2 == 0:
                list_crypted.append(key_1[5])
            else:
                list_crypted.append(key_2[5])
        if letters == "g":
            if index%2 == 0:
                list_crypted.append(key_1[6])
            else:
                list_crypted.append(key_2[6])
        if letters == "h":
            if index%2 == 0:
                list_crypted.append(key_1[7])
            else:
                list_crypted.append(key_2[7])
        if letters == "i":
            if index%2 == 0:
                list_crypted.append(key_1[8])
            else:
                list_crypted.append(key_2[8])
        if letters == "j":
            if index%2 == 0:
                list_crypted.append(key_1[9])
            else:
                list_crypted.append(key_2[9])
        if letters == "k":
            if index%2 == 0:
                list_crypted.append(key_1[10])
            else:
                list_crypted.append(key_2[10])
        if letters == "l":
            if index%2 == 0:
                list_crypted.append(key_1[11])
            else:
                list_crypted.append(key_2[11])
        if letters == "m":
            if index%2 == 0:
                list_crypted.append(key_1[12])
            else:
                list_crypted.append(key_2[12])
        if letters == "n":
            if index%2 == 0:
                list_crypted.append(key_1[13])
            else:
                list_crypted.append(key_2[13])
        if letters == "o":
            if index%2 == 0:
                list_crypted.append(key_1[14])
            else:
                list_crypted.append(key_2[14])
        if letters == "p":
            if index%2 == 0:
                list_crypted.append(key_1[15])
            else:
                list_crypted.append(key_2[15])
        if letters == "q":
            if index%2 == 0:
                list_crypted.append(key_1[16])
            else:
                list_crypted.append(key_2[16])
        if letters == "r":
            if index%2 == 0:
                list_crypted.append(key_1[17])
            else:
                list_crypted.append(key_2[17])
        if letters == "s":
            if index%2 == 0:
                list_crypted.append(key_1[18])
            else:
                list_crypted.append(key_2[18])
        if letters == "t":
            if index%2 == 0:
                list_crypted.append(key_1[19])
            else:
                list_crypted.append(key_2[19])
        if letters == "u":
            if index%2 == 0:
                list_crypted.append(key_1[20])
            else:
                list_crypted.append(key_2[20])
        if letters == "v":
            if index%2 == 0:
                list_crypted.append(key_1[21])
            else:
                list_crypted.append(key_2[21])
        if letters == "w":
            if index%2 == 0:
                list_crypted.append(key_1[22])
            else:
                list_crypted.append(key_2[22])
        if letters == "x":
            if index%2 == 0:
                list_crypted.append(key_1[23])
            else:
                list_crypted.append(key_2[23])
        if letters == "y":
            if index%2 == 0:
                list_crypted.append(key_1[24])
            else:
                list_crypted.append(key_2[24])
        if letters == "z":
            if index%2 == 0:
                list_crypted.append(key_1[25])
            else:
                list_crypted.append(key_2[25])
        if letters == "0":
            if index%2 == 0:
                list_crypted.append(key_1[26])
            else:
                list_crypted.append(key_2[26])
        if letters == "1":
            if index%2 == 0:
                list_crypted.append(key_1[27])
            else:
                list_crypted.append(key_2[27])
        if letters == "2":
            if index%2 == 0:
                list_crypted.append(key_1[28])
            else:
                list_crypted.append(key_2[28])
        if letters == "3":
            if index%2 == 0:
                list_crypted.append(key_1[29])
            else:
                list_crypted.append(key_2[29])
        if letters == "4":
            if index%2 == 0:
                list_crypted.append(key_1[30])
            else:
                list_crypted.append(key_2[30])
        if letters == "5":
            if index%2 == 0:
                list_crypted.append(key_1[31])
            else:
                list_crypted.append(key_2[31])
        if letters == "6":
            if index%2 == 0:
                list_crypted.append(key_1[32])
            else:
                list_crypted.append(key_2[32])
        if letters == "7":
            if index%2 == 0:
                list_crypted.append(key_1[33])
            else:
                list_crypted.append(key_2[33])
        if letters == "8":
            if index%2 == 0:
                list_crypted.append(key_1[34])
            else:
                list_crypted.append(key_2[34])
        if letters == "9":
            if index%2 == 0:
                list_crypted.append(key_1[35])
            else:
                list_crypted.append(key_2[35])
        index += 1    
    for letter in list_crypted:
        var_crypted += letter
    print(var_crypted)    

def Uncrypt_alphabet_code(key,list_to_uncrypt):
    global var_uncrypt
    var_crypted = ""
    list_uncrypt = []
    list_uncrypt.clear
    index = 0
    for letter in list(list_to_uncrypt):
        for letters in key_1:
            if letter == letters:
                if index%2 == 0:
                    if key_1.index(letters) == 0:
                        list_uncrypt.append("a")
                        break
                    if key_1.index(letters) == 1:
                        list_uncrypt.append("b")
                        break
                    if key_1.index(letters) == 2:
                        list_uncrypt.append("c")
                        break
                    if key_1.index(letters) == 3:
                        list_uncrypt.append("d")
                        break
                    if key_1.index(letters) == 4:
                        list_uncrypt.append("e")
                        break
                    if key_1.index(letters) == 5:
                        list_uncrypt.append("f")
                        break
                    if key_1.index(letters) == 6:
                        list_uncrypt.append("g")
                        break
                    if key_1.index(letters) == 7:
                        list_uncrypt.append("h")
                    if key_1.index(letters) == 8:
                        list_uncrypt.append("i")
                        break
                    if key_1.index(letters) == 9:
                        list_uncrypt.append("j")
                        break
                    if key_1.index(letters) == 10:
                        list_uncrypt.append("k")
                        break
                    if key_1.index(letters) == 11:
                       list_uncrypt.append("l")
                       break
                    if key_1.index(letters) == 12:
                        list_uncrypt.append("m")
                        break
                    if key_1.index(letters) == 13:
                        list_uncrypt.append("n")
                        break
                    if key_1.index(letters) == 14:
                        list_uncrypt.append("o")
                        break
                    if key_1.index(letters) == 15:
                        list_uncrypt.append("p")
                        break
                    if key_1.index(letters) == 16:
                        list_uncrypt.append("q")
                        break
                    if key_1.index(letters) == 17:
                        list_uncrypt.append("r")
                        break
                    if key_1.index(letters) == 18:
                        list_uncrypt.append("s")
                        break
                    if key_1.index(letters) == 19:
                        list_uncrypt.append("t")
                    if key_1.index(letters) == 20:
                        list_uncrypt.append("u")
                        break
                    if key_1.index(letters) == 21:
                        list_uncrypt.append("v")
                        break
                    if key_1.index(letters) == 22:
                        list_uncrypt.append("w")
                        break
                    if key_1.index(letters) == 23:
                        list_uncrypt.append("x")
                    if key_1.index(letters) == 24:
                        list_uncrypt.append("y")
                        break
                    if key_1.index(letters) == 25:
                       list_uncrypt.append("z")
                       break
                    if key_1.index(letters) == 26:
                        list_uncrypt.append("0")
                        break
                    if key_1.index(letters) == 27:
                        list_uncrypt.append("1")
                        break
                    if key_1.index(letters) == 28:
                        list_uncrypt.append("2")
                        break
                    if key_1.index(letters) == 29:
                        list_uncrypt.append("3")
                        break
                    if key_1.index(letters) == 30:
                        list_uncrypt.append("4")
                        break
                    if key_1.index(letters) == 31:
                        list_uncrypt.append("5")
                        break
                    if key_1.index(letters) == 32:
                        list_uncrypt.append("6")
                        break
                    if key_1.index(letters) == 33:
                        list_uncrypt.append("7")
                        break
                    if key_1.index(letters) == 34:
                        list_uncrypt.append("8")
                        break
                    if key_1.index(letters) == 35:
                        list_uncrypt.append("9")
                        break
                else:
                    break
                
        for lettre in key_2:            
            if lettre == letter:
                if index%2 == 1:
                    if key_2.index(letters) == 0:
                        list_uncrypt.append("a")
                        break
                    if key_2.index(letters) == 1:
                        list_uncrypt.append("b")
                        break
                    if key_2.index(letters) == 2:
                        list_uncrypt.append("c")
                        break
                    if key_2.index(letters) == 3:
                        list_uncrypt.append("d")
                        break
                    if key_2.index(letters) == 4:
                        list_uncrypt.append("e")
                        break
                    if key_2.index(letters) == 5:
                        list_uncrypt.append("f")
                        break
                    if key_2.index(letters) == 6:
                        list_uncrypt.append("g")
                        break
                    if key_2.index(letters) == 7:
                        list_uncrypt.append("h")
                        break
                    if key_2.index(letters) == 8:
                        list_uncrypt.append("i")
                        break
                    if key_2.index(letters) == 9:
                        list_uncrypt.append("j")
                        break
                    if key_2.index(letters) == 10:
                        list_uncrypt.append("k")
                        break
                    if key_2.index(letters) == 11:
                        list_uncrypt.append("l")
                        break
                    if key_2.index(letters) == 12:
                        list_uncrypt.append("m")
                        break
                    if key_2.index(letters) == 13:
                        list_uncrypt.append("n")
                        break
                    if key_2.index(letters) == 14:
                        list_uncrypt.append("o")
                        break
                    if key_2.index(letters) == 15:
                        list_uncrypt.append("p")
                        break
                    if key_2.index(letters) == 16:
                        list_uncrypt.append("q")
                        break
                    if key_2.index(letters) == 17:
                        list_uncrypt.append("r")
                        break
                    if key_2.index(letters) == 18:
                        list_uncrypt.append("s")
                        break
                    if key_2.index(letters) == 19:
                        list_uncrypt.append("t")
                        break
                    if key_2.index(letters) == 20:
                        list_uncrypt.append("u")
                        break
                    if key_2.index(letters) == 21:
                        list_uncrypt.append("v")
                        break
                    if key_2.index(letters) == 22:
                        list_uncrypt.append("w")
                        break
                    if key_2.index(letters) == 23:
                        list_uncrypt.append("x")
                        break
                    if key_2.index(letters) == 24:
                        list_uncrypt.append("y")
                        break
                    if key_2.index(letters) == 25:
                        list_uncrypt.append("z")
                        break
                    if key_2.index(letters) == 26:
                        list_uncrypt.append("0")
                        break
                    if key_2.index(letters) == 27:
                        list_uncrypt.append("1")
                        break
                    if key_2.index(letters) == 28:
                        list_uncrypt.append("2")
                        break
                    if key_2.index(letters) == 29:
                        list_uncrypt.append("3")
                        break
                    if key_2.index(letters) == 30:
                        list_uncrypt.append("4")
                        break
                    if key_2.index(letters) == 31:
                        list_uncrypt.append("5")
                        break
                    if key_2.index(letters) == 32:
                        list_uncrypt.append("6")
                        break
                    if key_2.index(letters) == 33:
                        list_uncrypt.append("7")
                        break
                    if key_2.index(letters) == 34:
                        list_uncrypt.append("8")
                        break
                    if key_2.index(letters) == 35:
                        list_uncrypt.append("9")
                        break  
                else:
                    break    
                              
        index += 1                
    for letter in list_uncrypt:
        var_crypted += letter            
    print(var_crypted)            

def Force_uncrypt(list_to_uncrypt):
    global var_forced_to_uncrypt
    
    test_in_charge = True
    try_number = 0
    
    while test_in_charge:
        var_forced_to_uncrypt = ""
        list_uncrypt = []
        list_uncrypt.clear
        index = 0
        key_3 = ""
        key_4 = ""
        alphabet_1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
        alphabet_2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
        while bool(alphabet_2):
            element_to_clear = random.randint(0,len(alphabet_1) - 1)
            key_3 += alphabet_1[element_to_clear]
            alphabet_1.remove(alphabet_1[element_to_clear])
            element_to_clear = random.randint(0,len(alphabet_2) - 1)
            key_4 += alphabet_2[element_to_clear]
            alphabet_2.remove(alphabet_2[element_to_clear])
    
        for letter in list(list_to_uncrypt):
            for letters in key_3:
                if letter == letters:
                    if index%2 == 0:
                        if key_3.index(letters) == 0:
                            list_uncrypt.append("a")
                            break
                        if key_3.index(letters) == 1:
                            list_uncrypt.append("b")
                            break
                        if key_3.index(letters) == 2:
                            list_uncrypt.append("c")
                            break
                        if key_3.index(letters) == 3:
                            list_uncrypt.append("d")
                            break
                        if key_3.index(letters) == 4:
                            list_uncrypt.append("e")
                            break
                        if key_3.index(letters) == 5:
                            list_uncrypt.append("f")
                            break
                        if key_3.index(letters) == 6:
                            list_uncrypt.append("g")
                            break
                        if key_3.index(letters) == 7:
                            list_uncrypt.append("h")
                        if key_3.index(letters) == 8:
                            list_uncrypt.append("i")
                            break
                        if key_3.index(letters) == 9:
                            list_uncrypt.append("j")
                            break
                        if key_3.index(letters) == 10:
                            list_uncrypt.append("k")
                            break
                        if key_1.index(letters) == 11:
                            list_uncrypt.append("l")
                            break
                        if key_3.index(letters) == 12:
                            list_uncrypt.append("m")
                            break
                        if key_3.index(letters) == 13:
                            list_uncrypt.append("n")
                            break
                        if key_3.index(letters) == 14:
                            list_uncrypt.append("o")
                            break
                        if key_3.index(letters) == 15:
                            list_uncrypt.append("p")
                            break
                        if key_3.index(letters) == 16:
                            list_uncrypt.append("q")
                            break
                        if key_3.index(letters) == 17:
                            list_uncrypt.append("r")
                            break
                        if key_3.index(letters) == 18:
                            list_uncrypt.append("s")
                            break
                        if key_3.index(letters) == 19:
                            list_uncrypt.append("t")
                        if key_3.index(letters) == 20:
                            list_uncrypt.append("u")
                            break
                        if key_3.index(letters) == 21:
                            list_uncrypt.append("v")
                            break
                        if key_3.index(letters) == 22:
                            list_uncrypt.append("w")
                            break
                        if key_3.index(letters) == 23:
                            list_uncrypt.append("x")
                        if key_3.index(letters) == 24:
                            list_uncrypt.append("y")
                            break
                        if key_3.index(letters) == 25:
                            list_uncrypt.append("z")
                            break
                        if key_3.index(letters) == 26:
                            list_uncrypt.append("0")
                            break
                        if key_3.index(letters) == 27:
                            list_uncrypt.append("1")
                            break
                        if key_3.index(letters) == 28:
                            list_uncrypt.append("2")
                            break
                        if key_3.index(letters) == 29:
                            list_uncrypt.append("3")
                            break
                        if key_3.index(letters) == 30:
                            list_uncrypt.append("4")
                            break
                        if key_3.index(letters) == 31:
                            list_uncrypt.append("5")
                            break
                        if key_3.index(letters) == 32:
                            list_uncrypt.append("6")
                            break
                        if key_3.index(letters) == 33:
                            list_uncrypt.append("7")
                            break
                        if key_3.index(letters) == 34:
                            list_uncrypt.append("8")
                            break
                        if key_3.index(letters) == 35:
                            list_uncrypt.append("9")
                            break
                    else:
                        break
                    
            for lettre in key_4:            
                if lettre == letter:
                    if index%2 == 1:
                        if key_4.index(letters) == 0:
                            list_uncrypt.append("a")
                            break
                        if key_4.index(letters) == 1:
                            list_uncrypt.append("b")
                            break
                        if key_4.index(letters) == 2:
                            list_uncrypt.append("c")
                            break
                        if key_4.index(letters) == 3:
                            list_uncrypt.append("d")
                            break
                        if key_4.index(letters) == 4:
                            list_uncrypt.append("e")
                            break
                        if key_4.index(letters) == 5:
                            list_uncrypt.append("f")
                            break
                        if key_4.index(letters) == 6:
                            list_uncrypt.append("g")
                            break
                        if key_4.index(letters) == 7:
                            list_uncrypt.append("h")
                            break
                        if key_4.index(letters) == 8:
                            list_uncrypt.append("i")
                            break
                        if key_4.index(letters) == 9:
                            list_uncrypt.append("j")
                            break
                        if key_4.index(letters) == 10:
                            list_uncrypt.append("k")
                            break
                        if key_4.index(letters) == 11:
                            list_uncrypt.append("l")
                            break
                        if key_4.index(letters) == 12:
                            list_uncrypt.append("m")
                            break
                        if key_4.index(letters) == 13:
                            list_uncrypt.append("n")
                            break
                        if key_4.index(letters) == 14:
                            list_uncrypt.append("o")
                            break
                        if key_4.index(letters) == 15:
                            list_uncrypt.append("p")
                            break
                        if key_4.index(letters) == 16:
                            list_uncrypt.append("q")
                            break
                        if key_4.index(letters) == 17:
                            list_uncrypt.append("r")
                            break
                        if key_4.index(letters) == 18:
                            list_uncrypt.append("s")
                            break
                        if key_4.index(letters) == 19:
                            list_uncrypt.append("t")
                            break
                        if key_4.index(letters) == 20:
                            list_uncrypt.append("u")
                            break
                        if key_4.index(letters) == 21:
                            list_uncrypt.append("v")
                            break
                        if key_4.index(letters) == 22:
                            list_uncrypt.append("w")
                            break
                        if key_4.index(letters) == 23:
                            list_uncrypt.append("x")
                            break
                        if key_4.index(letters) == 24:
                            list_uncrypt.append("y")
                            break
                        if key_4.index(letters) == 25:
                            list_uncrypt.append("z")
                            break
                        if key_4.index(letters) == 26:
                            list_uncrypt.append("0")
                            break
                        if key_4.index(letters) == 27:
                            list_uncrypt.append("1")
                            break
                        if key_4.index(letters) == 28:
                            list_uncrypt.append("2")
                            break
                        if key_4.index(letters) == 29:
                            list_uncrypt.append("3")
                            break
                        if key_4.index(letters) == 30:
                            list_uncrypt.append("4")
                            break
                        if key_4.index(letters) == 31:
                            list_uncrypt.append("5")
                            break
                        if key_4.index(letters) == 32:
                            list_uncrypt.append("6")
                            break
                        if key_4.index(letters) == 33:
                            list_uncrypt.append("7")
                            break
                        if key_4.index(letters) == 34:
                            list_uncrypt.append("8")
                            break
                        if key_4.index(letters) == 35:
                            list_uncrypt.append("9")
                            break  
                    else:
                        break    
                                
            index += 1                
        for letter in list_uncrypt:
            var_forced_to_uncrypt += letter            
        if var_forced_to_uncrypt == "moimoi":
            test_in_charge = False
            print(try_number)
        else:
            try_number += 1
            
        print(try_number)
            


Generate_key_alphabet()          
Crypt_alphabet_code(key_1,key_2,"moimoi")

Force_uncrypt(var_crypted)