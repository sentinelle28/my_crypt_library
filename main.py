from tkinter import *
from tkinter.ttk import *
screen = Tk(screenName="crypt app")
screen.geometry("600x700")

crypt_drop_down = Combobox(
    state="readonly",
    value= ["test","new"]
)
crypt_drop_down.place(x=100,y=200)



mainloop()


