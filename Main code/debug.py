#Not sure how this is going to work yet
#------------------------------------<Initialization Start>-------------------------------------------------------
from tkinter import * #The UI module that this program relies on
from tkinter import messagebox #This is a function that allows making windows message boxes, has to be called separetly
from tkinter.ttk import * #Theamed tkinter which makes the UI look ever so slightly modern
import os
from pathlib import Path
from playground import *

def add_button(parent, buttons):
    new_button = DraggableWidget(parent, text=f"Button {buttons}")
    new_button.pack(pady=5)
    buttons.append(new_button)
    print(buttons)

def quit():
    #Exits the program
    exit()

commands = {
        "exit": "quit()",
    }

def commander(command):
    if command in commands:
        exec(commands[command])
    else:
        #use messagebox to show error
        messagebox.showerror("Error", "Command not found")

def loadoptions(parent):
    buttons = 0
    commandbox = Entry(parent)
    commandbox.pack()
    enter = Button(parent, text="Enter", command=lambda: commander(commandbox.get()))
    enter.pack()
    #Doesn't work
    addbutton = Button(parent, text="Add Button", command=lambda: add_button(parent, buttons))
    addbutton.pack(pady=10)


#Has to be at the end of the file to ensure that all functions are loaded
def load_debug(parent): #Loads the debug menu
    debugwind = Toplevel(parent)
    debugwind.title("Debug menu")
    debugwind.geometry("250x400")
    loadoptions(debugwind)