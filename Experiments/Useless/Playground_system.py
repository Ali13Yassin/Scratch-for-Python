#------------------------------------<Initialization Start>-------------------------------------------------------
from tkinter import * #The UI module that this program relies on
from tkinter import messagebox #This is a function that allows making windows message boxes, has to be called separetly
from tkinter.ttk import * #Theamed tkinter which makes the UI look ever so slightly modern
import os #Used to change directory, and other things
from pathlib import Path #Used to get the path to the python file

os.chdir(Path(__file__).parent)

def windows():
    global actionwind,canvaswind
    canvaswind = Tk()
    canvaswind.title("Canvas menu")
    canvaswind.geometry("600x400")
    actionwind = Toplevel(canvaswind)
    actionwind.title("Debug menu")
    actionwind.geometry("200x100")

def basic_snap(movingwidget):
    widgets = {}
    for widget in canvaswind.winfo_children():
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
                snap_log(movingwidget, widgets[key])
            elif solid_loc[1]-moving_loc[1] <= moving_loc[2]+15 and solid_loc[1]-moving_loc[1] >=0: #Checks if the button is ontop of the other one
                print("Negative Snapped to {}".format(key))
                movingwidget.place(x=solid_loc[0], y=solid_loc[1]-moving_loc[2])

def snap_log(movingwidget, stillwidget):
    global snaplog
    snaplog = []
    recsnapped = {
        "widget id": movingwidget,
        "snapped to": stillwidget,
        "block_id": "0",
        "values": {
            "valu1":["Hello world", "2"],
            "valu2":["world hello", "2"],
        }
    }
    snaplog.append(recsnapped)
    print(snaplog)

def block_spawner(block):
    #This will spawn a block on the canvas
    #Could also have another function that spawns all block instead of doing each one
    widget_id = DraggableButton(canvaswind, text=block["name"])
    spawned_widgets[widget_id] = {
        "widget_id":widget_id,
        "snapped_to":None,
        "block_id":block["btype"],
        "values":{}
        }
    #Gets the how many values and their type and sets it in the widget list and properties
    for key in block["values"]:
        spawned_widgets[widget_id]["values"][key]
        

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

def canvasmenu():
    # Create a draggable button
    global draggable_button, second_button #Only used for debug menu
    draggable_button = DraggableButton(canvaswind, text="Drag Me", command=lambda: print("pressed!!!"))
    draggable_button.pack()
    second_button = DraggableButton(canvaswind, text="Drag Me\nToo")
    second_button.pack()
    
    # Create a button to check the location
    check_location_button = Button(actionwind, text="Check Location", command=get_button_location)
    check_location_button.pack()
    
def actionmenu():
    def add_button():
        new_button = DraggableButton(canvaswind, text=f"Button {len(buttons) + 1}")
        new_button.pack(pady=5)
        buttons.append(new_button)
        print(buttons)

    def move_button(x, y):
        draggable_button.place(x=x, y=y)
    
    buttons = []

    # Create a button to add more buttons
    add_button = Button(actionwind, text="Add Button", command=add_button)
    add_button.pack(pady=10)
    move_button_button = Button(actionwind, text="Move Button", command=lambda: move_button(100, 100))
    move_button_button.pack()
    canvaswind.mainloop()

def get_button_location():
    print("Button Location: x={}, y={}".format(draggable_button.winfo_x(), draggable_button.winfo_y()))
# Function to get the current location of the button

# def clear():
#     for widget in div.winfo_children():
#         widget.destroy() #Used this instead of forget to clear memory

# Run the Tkinter event loop
spawned_widgets = {}
windows()
canvasmenu()
actionmenu()