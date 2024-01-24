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
    global wind, div, fnt  # Defines the main window, and div
    wind = Tk()
    wind.configure(bg="#7e8082")  # Change background color to blue
    centx = int((wind.winfo_screenwidth() - 1100) / 2) #Gets coordinates of where to center the window on x-axis
    centy = int((wind.winfo_screenheight() - 650) / 2) #Gets coordinates of where to center the window on y-axis
    wind.geometry("1100x650+{}+{}".format(centx, centy)) #Centers the window
    # wind.iconbitmap("SFP.ico")  # Changes icon
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

def basic_snap(movingwidget):
    #A potential fix to all this is using the latest prompt in chatgpt (find() or in) to filter EACH
    #widget in the list then removing that item, which is not ideal but does the job for now
    #a complicated fix for such a small issue like what the fuck
    widgets = {}
    for widget in playground.winfo_children():
        widgets[str(widget)] = widget
    del widgets[str(movingwidget)]
    # del widgets[".!toplevel"] #Broken if window is closed
    for key in widgets:
        #Coordinates and size [X,Y,height,width], might change it to a dict for readaility
        solid_loc = [widgets[key].winfo_x(), widgets[key].winfo_y(), widgets[key].winfo_height(), widgets[key].winfo_width()]
        moving_loc = [movingwidget.winfo_x(), movingwidget.winfo_y(), movingwidget.winfo_height(), movingwidget.winfo_width()]
        if moving_loc[0]-solid_loc[0] <= 25 and moving_loc[0]-solid_loc[0] >= -25:
            if moving_loc[1]-solid_loc[1] <= solid_loc[2]+25 and moving_loc[1]-solid_loc[1] >=0:
                print("Snapped to {}".format(key))
                movingwidget.place(x=solid_loc[0], y=solid_loc[1]+solid_loc[2])
            elif solid_loc[1]-moving_loc[1] <= moving_loc[2]+15 and solid_loc[1]-moving_loc[1] >=0: #Checks if the button is ontop of the other one
                print("Negative Snapped to {}".format(key))
                movingwidget.place(x=solid_loc[0], y=solid_loc[1]-moving_loc[2])

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

#------------------------------------<Initialization End>-------------------------------------------------------
#------------------------------------<Playground start>-------------------------------------------------------
def playgroundmenu():
    clear()
    global playground
    total_width = wind.winfo_width()

    # 70% for playground
    playground_width = int(total_width * 70)
    frame_style = Style()
    frame_style.configure("playground.TFrame", background="#2e2e2e")
    playground = Frame(div, style="playground.TFrame")
    playground.configure(style="playground.TFrame")
    playground.place(relx=0, rely=0, relwidth=0.7, relheight=1)

    # 30% for sidebar
    sidebar_width = int(total_width * 0.3)
    frame_style = Style()
    frame_style.configure("sidebar.TFrame", background="#c4c4c4")
    sidebar = Frame(div, style="sidebar.TFrame")
    sidebar.configure(style="sidebar.TFrame")
    sidebar.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

    global draggable_button, second_button
    draggable_button = DraggableButton(playground, text="Drag Me", command=lambda: print("pressed!!!"))
    draggable_button.pack()
    second_button = DraggableButton(playground, text="Drag Me\nToo")
    second_button.pack()

#------------------------------------<Playground End>-------------------------------------------------------
start()