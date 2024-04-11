#------------------------------------<Initialization Start>-------------------------------------------------------
from tkinter import * #The UI module that this program relies on
from tkinter import messagebox #This is a function that allows making windows message boxes, has to be called separetly
from tkinter.ttk import * #Theamed tkinter which makes the UI look ever so slightly modern
import os
from pathlib import Path

os.chdir(Path(__file__).parent) #Changes cmd directory to the one that has the py file

#Checks if the required python files exist, To be implemented...
# if os.path.exists("Corefunctions.py") and os.path.exists("Exportfunctions.py"):
#     from Corefunctions import * #The library I made that handles backend operations
#     from Exportfunctions import * #The library I made that exports information
# else:
#     messagebox.showerror("Error", "Critical files are missing, please redownload the application to function properly.")
#     quit()

#Starts the program
def start():
    # filecheck()#Checks if other database files exist and creates them
    window() #Defines properties of the main window
    mainmenu() #The first menu to the application
    wind.mainloop() #Makes the window apear

def window():
    global wind,playground,blockmenu,fnt #Defines the main window, and blockmenu
    wind = Tk()
    wind.configure(bg="#7e8082")  # Change background color to blue
    centx = int((wind.winfo_screenwidth() - 1100) / 2) #Gets coordinates of where to center the window on x-axis
    centy = int((wind.winfo_screenheight() - 650) / 2) #Gets coordinates of where to center the window on y-axis
    wind.geometry("1100x650+{}+{}".format(centx, centy)) #Centers the window
    # wind.iconbitmap("Logo.ico") #Changes icon
    # wind.grid_rowconfigure(1, weight=1)     #Helps center objects
    # wind.grid_columnconfigure(1, weight=1)  #Helps center objects
    wind.title("Project purple mebibyte")
    fnt = "Manrope" #To be able to change font through one change
    blockmenu = Frame(wind) #Funny name from html that's not gonna cause issues at all lolol
    frame_style = Style()
    frame_style.configure("Custom.TFrame", background="#7e8082")
    blockmenu.configure(style="Custom.TFrame")
    blockmenu.grid(row=0, column=1, padx=10, pady=5) #The frame keeps the layout decent
    playground = Frame(wind)
    frame_style.configure("Custom.TFrame", background="#afb3b0")
    playground.configure(style="Custom.TFrame")
    playground.grid(row=0, column=0, padx=10, pady=5) #The frame keeps the layout decent

def mainmenu():
    clear() #To clear last menu when coming back
    style = Style()
    style.configure("TButton", font=(fnt, 12))
    Label(blockmenu, text="Project purple mebibyte", font=(fnt, 25, "bold")).grid(row=0, column=0)
    Button(blockmenu, text="Print()", command=clear).grid(row=1, column=0, padx=10, pady=5)
    Button(blockmenu, text="If", command=openmenu).grid(row=2, column=0, padx=10, pady=5)
    Button(blockmenu, text="Else", command=openmenu).grid(row=3, column=0, padx=10, pady=5)
    Button(playground, text="Else", command=openmenu).grid(row=1, column=0, padx=10, pady=5)

def openmenu():
    clear() #To clear last menu when coming back
    style = Style()
    style.configure("TButton", font=(fnt, 12))
    Label(blockmenu, text="Open project menu", font=(fnt, 25, "bold")).grid(row=0, column=0)
    Button(blockmenu, text="Back", command=mainmenu).grid(row=1, column=0, padx=10, pady=5)
    Button(blockmenu, text="Load project", command=clear).grid(row=2, column=0, padx=10, pady=5)

def button1(): #Can be used to run the user's project after completion
    script_path = 'C:\\Users\\SUT\\Downloads\\Scratch for Python\\Snap_with_new_movement.py'
    with open(script_path, 'r') as script_file:
        exec(script_file.read())

#Deletes the widgets from previous menu and cleares memory from them
def clear():
    for widget in blockmenu.winfo_children():
        widget.destroy() #Used this instead of forget to clear memory
#------------------------------------<Initialization End>-------------------------------------------------------
#------------------------------------<Editing start>-------------------------------------------------------

#------------------------------------<Editing End>-------------------------------------------------------
start()