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
    spawned_widgets[movingwidget]["snapped_to"] = stillwidget
    recsnapped = spawned_widgets[movingwidget]
    snaplog.append(recsnapped)
    print(snaplog)

#Spawns a block with the given properties, and adds it to the spawned_widgets list 
def block_spawner(block):
    #This will spawn a block on the canvas
    #Could also have another function that spawns all block instead of doing each one
    widget_id = DraggableFrame(canvaswind)
    widget_id.config(cursor="hand2")
    frame_style = Style()
    frame_style.configure("{}.TFrame".format(widget_id), background="#2e2e2e")
    widget_id.configure(style="{}.TFrame".format(widget_id))  # Set background color
    #The {} only specifies where the entrys will be, the entrys will be placed at the end if not specified
    texts = block["name"].split("{}")
    print(texts)
    step = 0
    label_style = Style()
    # Configure a new style for a specific label
    label_style.configure("Custom.TLabel", foreground="white", background="#2e2e2e")
    for text in texts:
        DraggableLabel(widget_id, text=text, style="Custom.TLabel").grid(row=0, column=step, padx=3, pady=3)
        step += 2
    spawned_widgets[widget_id] = {
        "widget_id":widget_id,
        "snapped_to":None,
        "block_id":block["btype"],
        "values":{}
        }
    #Gets the how many values and their type and sets it in the widget list and properties
    step = 1
    #This will create the entrys for the specified values in block
    for key in block["values"]:
        spawned_widgets[widget_id]["values"][key] = StringVar()
        #This will create an entry that modifies the value of the dictionary
        Entry(widget_id, textvariable= spawned_widgets[widget_id]["values"][key],width=7).grid(row=0, column=step, padx=3, pady=3)
        step += 2
    # widget_id.pack_propagate(False)
    widget_id.pack()

class DraggableFrame(Frame):
    def __init__(self, master=None,*args, **kwargs):
        Frame.__init__(self, master,*args, **kwargs)
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

class DraggableLabel(Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<Button-1>", self.on_drag_start)
        self.bind("<B1-Motion>", self.on_drag_motion)
        self.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        global dragging
        dragging = False

    def on_drag_start(self, event): #Happens when button is clicked or once when dragged
        self._drag_start_x = event.x
        self._drag_start_y = event.y
        self.master.lift()
        global dragging
        dragging = True

    def on_drag_motion(self, event): #Happens every frame the button is being actually dragged
        x = self.master.winfo_x() - self._drag_start_x + event.x
        y = self.master.winfo_y() - self._drag_start_y + event.y
        self.master.place(x=x, y=y)

    def on_release(self, event):
        if dragging:
            # print("{} Location: x={}, y={}".format(self, self.winfo_x(), self.winfo_y()))
            basic_snap(self.master)
        else:
            print("Button was pressed")

def canvasmenu():
    # Create a draggable button
    global draggable_button, second_button #Only used for debug menu
    frame_style = Style()
    frame_style.configure("playground.TFrame", background="#2e2e2e")
    draggable_frame = DraggableFrame(canvaswind, width=200, height=50) #, text="Drag Me")
    draggable_frame.configure(style="playground.TFrame")  # Set background color
    draggable_frame.pack_propagate(False)
    draggable_frame.pack()
    second_frame = DraggableFrame(canvaswind, width=200, height=50) #, text="Drag Me\nToo")
    second_frame.pack()
    #make a button that spawns a block
    button = Button(canvaswind, text="Spawn Block", command=lambda: block_spawner(block_test["2"]))
    button.pack()
    button2 = Button(canvaswind, text="print", command=debug_print)
    button2.pack()
    block_spawner(block_test["2"])
    canvaswind.mainloop()
    
def debug_print():
    for widget_id in spawned_widgets:
        print(spawned_widgets[widget_id]["widget_id"])
        for key in spawned_widgets[widget_id]["values"]:
            print(spawned_widgets[widget_id]["values"][key].get())

block_test = {"2":{
        "name":"Set Variable {} as {}",
        "btype":"block",
        "color":"orange",
        "code":"{} = {}",
        "values":{
            "name":"str",
            "value":"any"
        }
    },
    "custom":{
        "name":"Custom code",
        "btype":"block",
        "color":"purple",
        "code":"",
        "values":{
            "value1":"custom"
        }
    }}


# Function to get the current location of the button

# def clear():
#     for widget in div.winfo_children():
#         widget.destroy() #Used this instead of forget to clear memory

# Run the Tkinter event loop
spawned_widgets = {}
windows()
canvasmenu()