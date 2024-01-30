#Not sure how this is going to work yet
#------------------------------------<Initialization Start>-------------------------------------------------------
from tkinter import * #The UI module that this program relies on
from tkinter import messagebox #This is a function that allows making windows message boxes, has to be called separetly
from tkinter.ttk import * #Theamed tkinter which makes the UI look ever so slightly modern
import os
from pathlib import Path

def add_button(parent, buttons):
    new_button = DraggableButton(parent, text=f"Button {buttons}")
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
    addbutton = Button(parent, text="Add Button", command=lambda: add_button(parent, buttons))
    addbutton.pack(pady=10)

class DraggableButton(Button):
    def __init__(self, master=None, **kwargs):
        Button.__init__(self, master, **kwargs)
        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<Button-1>", self.on_drag_start)
        self.bind("<B1-Motion>", self.on_drag_motion)
        self.bind("<ButtonRelease-1>", self.on_release)
        
    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        global dragging
        dragging = False

    def on_drag_start(self, event): #Happens when button is clickeed or once when dragged
        self._drag_start_x = event.x
        self._drag_start_y = event.y
        self.lift()
        global dragging
        dragging = True

    def on_drag_motion(self, event): #Happens every frame the button is being actually dragged
        x = self.winfo_x() - self._drag_start_x + event.x
        y = self.winfo_y() - self._drag_start_y + event.y
        self.place(x=x, y=y)

    def on_release(self, event):
        if dragging:
            # print("{} Location: x={}, y={}".format(self, self.winfo_x(), self.winfo_y()))
            basic_snap(self)
        else:
            print("Button was pressed")

#Has to be at the end of the file to ensure that all functions are loaded
def load_debug(parent): #Loads the debug menu
    debugwind = Toplevel(parent)
    debugwind.title("Debug menu")
    debugwind.geometry("250x400")
    loadoptions(debugwind)