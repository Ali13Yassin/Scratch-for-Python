#------------------------------------<Initialization Start>-------------------------------------------------------
from tkinter import * #The UI module that this program relies on
from tkinter import messagebox #This is a function that allows making windows message boxes, has to be called separetly
from tkinter.ttk import * #Theamed tkinter which makes the UI look ever so slightly modern
# import os #Used to change directory, and other things
# from pathlib import Path #Used to get the path to the python file

# os.chdir(Path(__file__).parent)

# def windows():
#     # global actionwind,canvaswind
#     canvaswind = Tk()
#     canvaswind.title("Canvas menu")
#     canvaswind.geometry("600x400")
#     actionwind = Toplevel(canvaswind)
#     actionwind.title("Debug menu")
#     actionwind.geometry("200x100")

def basic_snap(parent,movingwidget):
    widgets = {}
    for widget in parent.winfo_children():
        widgets[str(widget)] = widget
    del widgets[str(movingwidget)]
    del widgets[".!toplevel"] #Broken if window is closed
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
            
            basic_snap(self.nametowidget(self.winfo_parent()).winfo_name(),self)
        else:
            print("Button was pressed")

def spawnplayground(parent):
    draggable_button = DraggableButton(parent, text="Drag Me", command=lambda: print("pressed!!!"))
    draggable_button.pack()
    second_button = DraggableButton(parent, text="Drag Me\nToo")
    second_button.pack()