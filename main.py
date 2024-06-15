from tkinter import *
from tkinter.ttk import *

#function
def generate_key():
    if crypt_drop_down.get() != "":
        key_input.delete(1.0,END)
        key_input.insert(END,"test")

#object       
screen = Tk(screenName="crypt app")
screen.geometry("600x700")

crypt_drop_down = Combobox(
    state="readonly",
    value= ["test","new"]
)
key_input = Text(height=5,width=20)

#placing things up
crypt_drop_down.place(x=100,y=200)
key_input.place(x=200,y=300)

generate_key_button = Button(command=generate_key,text="generate a key").place(x=200,y=200)





mainloop()


