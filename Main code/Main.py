#------------------------------------<Initialization Start>-------------------------------------------------------
from tkinter import * #The UI module that this program relies on
from tkinter import messagebox #This is a function that allows making windows message boxes, has to be called separetly
from tkinter.ttk import * #Theamed tkinter which makes the UI look ever so slightly modern
import os
from pathlib import Path

#My modules
from playground import *

os.chdir(Path(__file__).parent) #Changes cmd directory to the one that has the py file

# Checks if the required python files exist, To be implemented...
# if os.path.exists("Corefunctions.py") and os.path.exists("Exportfunctions.py"):
#     from Corefunctions import * #The library I made that handles backend operations
#     from Exportfunctions import * #The library I made that exports information
# else:
#     messagebox.showerror("Error", "Critical files are missing, please redownload the application to function properly.")
#     quit()

#Checks if the debug file exists, and if it does, imports it
#if os.path.exists("debug.py"):
#    from debug import * #The library I made that handles backend operations
#    debugging = True
#else:
#    debugging = False

#Starts the program
def start():
    # filecheck()#Checks if other database files exist and creates them
    window() #Defines properties of the main window
    mainmenu() #The first menu to the application
#    if debugging:
#        load_debug(wind) #Loads the debug menu
    wind.mainloop() #Makes the window apear

def window():
    global wind, div, fnt  # Defines the main window, and div
    wind = Tk()
    wind.configure(bg="#7e8082")  # Change background color to blue
    centx = int((wind.winfo_screenwidth() - 1100) / 2) #Gets coordinates of where to center the window on x-axis
    centy = int((wind.winfo_screenheight() - 650) / 2) #Gets coordinates of where to center the window on y-axis
    wind.geometry("1100x650+{}+{}".format(centx, centy)) #Centers the window
    wind.iconbitmap("SFP.ico")  # Changes icon
    wind.title("Project SFP")
    fnt = "Manrope"  # To be able to change font through one change
    div = Frame(wind)  # Funny name from HTML that's not gonna cause issues at all lolol
    frame_style = Style()
    frame_style.configure("Custom.TFrame", background="#7e8082")
    div.configure(style="Custom.TFrame")
    div.place(relx=0, rely=0, relwidth=1, relheight=1)  # The frame keeps the layout decent
    div.grid_rowconfigure(0, weight=1)
    div.grid_columnconfigure(0, weight=1)

def mainmenu():
    clear() #To clear last menu when coming back
    style = Style()
    style.configure("TButton", font=(fnt, 12))
    Label(div, text="Project SFP", font=(fnt, 25, "bold")).grid(row=0, column=0)
    Button(div, text="New project", command=playgroundmenu).grid(row=1, column=0, padx=10, pady=5)
    Button(div, text="Load project", command=openmenu).grid(row=2, column=0, padx=10, pady=5)

def openmenu():
    clear() #To clear last menu when coming back
    style = Style()
    style.configure("TButton", font=(fnt, 12))
    Label(div, text="Open project menu", font=(fnt, 25, "bold")).grid(row=0, column=0)
    Button(div, text="Back", command=mainmenu).grid(row=1, column=0, padx=10, pady=5)
    Button(div, text="Load project", command=clear).grid(row=2, column=0, padx=10, pady=5)

#Deletes the widgets from previous menu and cleares memory from them
def clear():
    for widget in div.winfo_children():
        widget.destroy() #Used this instead of forget to clear memory

def init_compile():
    import Compiler
    Compiler.startcompile("Project 1", snaplog)
    #This should gather data from all blocks and sent them to compile.py

#------------------------------------<Initialization End>-------------------------------------------------------
#------------------------------------<Playground start>-------------------------------------------------------
def playgroundmenu():
    clear()
    #I need to call a function from the playground system that creates the playground, so that playground system isn't tied to the main code
    total_width = wind.winfo_width()

    frame_style = Style()
    #frame_style.configure("playground.TFrame", background="#2e2e2e")
    frame_style.configure("playground.TFrame", background="white")
    playground = Frame(div, style="playground.TFrame")
    playground.place(relx=0, rely=0, relwidth=0.7, relheight=1)

    frame_style.configure("sidebar.TFrame", background="#c4c4c4")
    sidebar = Frame(div, style="sidebar.TFrame")
    sidebar.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

    Button(playground, text="playground", command=mainmenu).pack()
    Button(sidebar, text="Spawn Print block", command=lambda: block_spawner(block_test["3"])).pack()
    Button(sidebar, text="Compile and export", command=init_compile).pack()

    wind.protocol("WM_DELETE_WINDOW", on_closing)
    spawnplayground(wind)
#------------------------------------<Playground End>-------------------------------------------------------
#This function is called when the user tries to close the window
def on_closing():
    #Needs to check if the project has been saved or exported
    if messagebox.askokcancel("Quit", "Do you want to quit without saving or exporting?"):
        wind.destroy()

start()