#This is to test if I can have modules interact with tkinter
from tkinter import *
# from tkinter.ttk import *
from spawner_test2 import *

def start():
    # filecheck()#Checks if other database files exist and creates them
    window() #Defines properties of the main window
    mainmenu(wind) #The first menu to the application
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
    # frame_style = Style()
    # frame_style.configure("Custom.TFrame", background="#7e8082")
    # div.configure(style="Custom.TFrame")
    div.place(relx=0, rely=0, relwidth=1, relheight=1)  # The frame keeps the layout decent
    div.grid_rowconfigure(0, weight=1)
    div.grid_columnconfigure(0, weight=1)

start()