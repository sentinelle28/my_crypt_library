from tkinter import *
from tkinter.ttk import *

import cryptage.variation_cypher as CVC
import cryptage.discovered as CD

#for all module
dico_crypt = {"CVC":CVC,"CD":CD}


#function
def get_text():
    text = text_input.get(1.0,END)
    text = list(text)
    del text[-1]
    text = "".join(text)
    return text

def get_key():
    key = key_input.get(1.0,END)
    key = list(key)
    del key[-1]
    key = "".join(key)
    return key

def can_do(module_to_use):
    return module_to_use in dico_crypt and len(get_text()) != 0



def generate_key():
    module_to_use = crypt_drop_down.get()
    if can_do(module_to_use):
        key_input.delete(1.0,END)
        key_input.insert(END,dico_crypt[module_to_use].generate_key(get_text()))

def  crypt():
    module_to_use = crypt_drop_down.get()
    if can_do(module_to_use):
        text = dico_crypt[module_to_use].crypt(get_text(),get_key())
        text_input.delete(1.0,END)
        text_input.insert(END,text)

def uncrypt():
    module_to_use = crypt_drop_down.get()
    if can_do(module_to_use):
        text = dico_crypt[module_to_use].uncrypt(get_text(),get_key())
        text_input.delete(1.0,END)
        text_input.insert(END,text)

#object       
screen = Tk(screenName="crypt app")
screen.geometry("600x700")


liste = list(dico_crypt.keys())

crypt_drop_down = Combobox(
    state="readonly",
    value = liste
)
key_input = Text(height=5,width=20)
text_input = Text(height=5,width=20)


#placing things up
crypt_drop_down.place(x=100,y=200)
key_input.place(x=200,y=300)
text_input.place(x=400,y=300)

generate_key_button = Button(command=generate_key,text="generate a key").place(x=200,y=200)
crypt_button = Button(command=crypt,text="crypt text").place(x=400,y=200)
uncrypt_button = Button(command=uncrypt,text="uncrypt text").place(x=400,y=600)




mainloop()


