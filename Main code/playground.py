#------------------------------------<Initialization Start>-------------------------------------------------------
from tkinter import * #The UI module that this program relies on
from tkinter import messagebox #This is a function that allows making windows message boxes, has to be called separetly
from tkinter.ttk import * #Theamed tkinter which makes the UI look ever so slightly modern

def basic_snap(movingwidget,event):
    widgets = {}
    parentName = event.widget.winfo_parent()
    parent = event.widget._nametowidget(parentName)
    for widget in parent.winfo_children():
        widgets[str(widget)] = widget
    del widgets[str(movingwidget)]
    if ".!toplevel" in widgets:
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

class DraggableWidget(Label):
    def __init__(self, master, **kwargs):
        Label.__init__(self, master, **kwargs)
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
            
            basic_snap(self,event)
        else:
            print("Button was pressed")

def spawnplayground(parent): #Should spawn all buttons in all_widgets
    draggable_button = DraggableWidget(parent, text="Drag Me", font=(100))
    draggable_button.pack()
    second_button = DraggableWidget(parent, text="Drag Me\nToo", font=(50))
    second_button.pack()