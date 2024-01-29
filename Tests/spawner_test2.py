from tkinter import *

def mainmenu(parent):
    # clear() #To clear last menu when coming back
    # style = Style()
    # style.configure("TButton", font=(fnt, 12))
    Label(parent, text="Project SFP").grid(row=0, column=0)
    Button(parent, text="New project", command=placeholder).grid(row=1, column=0, padx=10, pady=5)
    Button(parent, text="Load project", command=placeholder).grid(row=2, column=0, padx=10, pady=5)

def placeholder():
    print("placeholder")