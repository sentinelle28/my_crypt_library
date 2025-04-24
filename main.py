from tkinter import *
from tkinter.ttk import *

import cryptage.variation_cypher as CVC
import cryptage.discovered as CD

#for all module
dico_crypt:dict = {"CVC":CVC,"CD":CD}


#function
def get_text()->str:
    text:str = text_input.get(1.0,END)
    temp:list[str] = list(text)
    del temp[-1]
    text = "".join(temp)
    return text

def get_key()->str:
    key:str = key_input.get(1.0,END)
    temp:list[str] = list(key)
    del temp[-1]
    key = "".join(temp)
    return key

def can_do(module_to_use)->bool:
    return module_to_use in dico_crypt and len(get_text()) != 0



def generate_key()->None:
    module_to_use = crypt_drop_down.get()
    if can_do(module_to_use):
        key_input.delete(1.0,END)
        key_input.insert(END,dico_crypt[module_to_use].generate_key(get_text()))

def  crypt()->None:
    module_to_use = crypt_drop_down.get()
    if can_do(module_to_use):
        text:str = dico_crypt[module_to_use].crypt(get_text(),get_key())
        text_input.delete(1.0,END)
        text_input.insert(END,text)

def uncrypt()->None:
    module_to_use = crypt_drop_down.get()
    if can_do(module_to_use):
        text:str = dico_crypt[module_to_use].uncrypt(get_text(),get_key())
        text_input.delete(1.0,END)
        text_input.insert(END,text)

#object       
screen:Tk = Tk(screenName="crypt app")
screen.geometry("600x700")


liste:list[str] = list(dico_crypt.keys())

crypt_drop_down:Combobox = Combobox(
    state="readonly",
    value = liste
)
key_input:Text = Text(height=5,width=20)
text_input:Text = Text(height=5,width=20)


#placing things up
crypt_drop_down.place(x=100,y=200)
key_input.place(x=200,y=300)
text_input.place(x=400,y=300)

generate_key_button:Button = Button(command=generate_key,
                                    text="generate a key")
generate_key_button.place(x=200,y=200)
crypt_button:Button = Button(command=crypt,text="crypt text")
crypt_button.place(x=400,y=200)
uncrypt_button:Button = Button(command=uncrypt,text="uncrypt text")
uncrypt_button.place(x=400,y=600)
mainloop()


