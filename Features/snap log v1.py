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
    #This will get all the widgets in the canvas
    for widget in canvaswind.winfo_children():
        if isinstance(widget, Block): #Checks if the widget is a block
            widgets[str(widget)] = widget #Stores the widget in a dictionary with the key being the string of the widget
            
    del widgets[str(movingwidget)] #Deletes the moving widget from the list so it doesn't snap to itself
    if ".!toplevel" in widgets: #Deletes the toplevel widget that is created when the window is created
        del widgets[".!toplevel"]

    #This will find the closest widget to snap to
    for key in widgets:
        #Coordinates and size [X,Y,height,width], might change it to a dict for readaility
        #TODO: Rename for readability
        solid_loc = [widgets[key].winfo_x(), widgets[key].winfo_y(), widgets[key].winfo_height(), widgets[key].winfo_width()]
        moving_loc = [movingwidget.winfo_x(), movingwidget.winfo_y(), movingwidget.winfo_height(), movingwidget.winfo_width()]
        snapped = False
        if moving_loc[0]-solid_loc[0] <= 25 and moving_loc[0]-solid_loc[0] >= -25:
            if moving_loc[1]-solid_loc[1] <= solid_loc[2]+25 and moving_loc[1]-solid_loc[1] >=0:
                print("Snapped to {}".format(key)) #Debugging
                #Snaps the widget to the top of the other widget
                movingwidget.place(x=solid_loc[0], y=solid_loc[1]+solid_loc[2]) 
                snap_log(movingwidget, widgets[key]) #Logs the snap
                movingwidget.snapping = [False, True]
                snapped = True
            # elif solid_loc[1]-moving_loc[1] <= moving_loc[2]+15 and solid_loc[1]-moving_loc[1] >=0: #Checks if the button is ontop of the other one
            #     print("Negative Snapped to {}".format(key))
            #     movingwidget.place(x=solid_loc[0], y=solid_loc[1]-moving_loc[2])
            #     snapped = True
    if not snapped:
        detach(movingwidget)

def small_snap(movingwidget):
    widgets = {}
    self_widgets = {}
    #This will get all the widgets in the canvas
    
    for block in canvaswind.winfo_children():
        if isinstance(block, Block): #Checks if the widget is a block
            for widget in block.winfo_children():
                if isinstance(widget, Entry):
                    widgets[str(widget)] = widget #Stores the widget in a dictionary with the key being the string of the widget
    # del widgets[str(movingwidget)] #Deletes the moving widget from the list so it doesn't snap to itself

    for widget in movingwidget.winfo_children(): #Gets the entry widgets in the moving widget
        if isinstance(widget, Entry): #Checks if the widget is a block
            self_widgets[str(widget)] = widget

    for key in self_widgets: #Deletes the moving widget entries from the list so it doesn't snap to itself
        if isinstance(self_widgets[key], Entry):
            del widgets[key]
    print(widgets) #Debugging
    #This will find the closest widget to snap to
    for key in widgets:
        #Coordinates and size [X,Y,height,width], might change it to a dict for readaility
        #TODO: Rename for readability
        parent_widget = canvasmenu.nametowidget(widgets[key].winfo_parent())
        solid_loc = [widgets[key].winfo_x() + parent_widget.winfo_x(), widgets[key].winfo_y() + parent_widget.winfo_y(), widgets[key].winfo_height(), widgets[key].winfo_width()]
        moving_loc = [movingwidget.winfo_x(), movingwidget.winfo_y(), movingwidget.winfo_height(), movingwidget.winfo_width()]
        print(solid_loc)
        print(moving_loc)
        print(key)
        # snapped = False
        if  moving_loc[0]-solid_loc[0] <= 25 and moving_loc[0]-solid_loc[0] >= -25:
            print("first if")
            if  moving_loc[1]-solid_loc[1] <= solid_loc[2]+25 and moving_loc[1]-solid_loc[1] >=0:
                print("Snapped to {}".format(key)) #Debugging
                #Snaps the widget on top of the other widget
                movingwidget.place(x=solid_loc[0], y=solid_loc[1])
                widgets[key].configure(height=moving_loc[2], width=moving_loc[3])
                # snap_log(movingwidget, widgets[key]) #Logs the snap
                # movingwidget.snapping = [False, True]
                # snapped = True
            # elif solid_loc[1]-moving_loc[1] <= moving_loc[2]+15 and solid_loc[1]-moving_loc[1] >=0: #Checks if the button is ontop of the other one
            #     print("Negative Snapped to {}".format(key))
            #     movingwidget.place(x=solid_loc[0], y=solid_loc[1]-moving_loc[2])
            #     snapped = True
    # if not snapped:
    #     pass

def snap_log(movingwidget, stillwidget):
    logger = []
    #Makes sure the widget is cleaned if it was snapped to something before
    if movingwidget.snapped_to != None:
        detach(movingwidget)
    if movingwidget.parent == "self": #If the widget was a parent
        #Do something I dunno, kill me
        pass
    #If stillwidget wasn't not snapped to anything before
    if stillwidget.parent == None:
        movingwidget.parent = stillwidget
        stillwidget.parent = "self"
        logger.insert(0, stillwidget)
        logger.insert(1, movingwidget)
        snaplog.append(logger)

    #If the widget is snapped to a supposed parent, not supposed to happen!!!
    elif stillwidget.parent == "self":
        # movingwidget.parent = stillwidget #This will make the widget a child of the supposed parent
        print("Snapped to 'supposed parent' {}".format(stillwidget))

    #If the widget is snapped to a normal widget
    else:
        movingwidget.parent = stillwidget.parent #Inherits the parent of the widget it is snapped to
        # snaplog[spawned_widgets[stillwidget]["parent"]] TODO
        for i in range(len(snaplog)):
            if snaplog[i][0] == stillwidget.parent:
                snaplog[i].append(movingwidget)
                break
    movingwidget.snapped_to = stillwidget

def snap_lock(movingwidget, stillwidget):
    #This will lock the widget to the other widget
    pass
    

def detach(movingwidget):
    #This cleans up and resets the properties of the widget
    if movingwidget.parent != None: #Checks if the widget was snapped to something before
        #Get parent of widget then check it's type
        widgets_parent = movingwidget.snapped_to
        if movingwidget.parent == "self": #If the widget was A parent
            movingwidget.parent = None #Resets the parent of the snapped_to
            for i in range(len(snaplog)):
                if snaplog[i][0] == movingwidget:
                    del snaplog[i]
                    break
        elif widgets_parent.parent == "self": #If the widget was snapped to a parent
            widgets_parent.parent = None #Resets the parent of the snapped_to
            for i in range(len(snaplog)):
                if snaplog[i][0] == movingwidget.parent:
                    del snaplog[i]
                    break
        else:
            #Removes the widget from the parent
            for i in range(len(snaplog)):
                if snaplog[i][0] == movingwidget.parent:
                    snaplog[i].remove(movingwidget)
                    break
        print("Detached {}".format(movingwidget))
        movingwidget.parent = None
        movingwidget.snapped_to = None
        movingwidget.snapping = [True, True]

#Spawns a block with the given properties, and adds it to the spawned_widgets list 
#TODO: Make it only spawn the GUI and not the properties
def block_spawner(block):
    #This will spawn a block on the canvas
    #Could also have another function that spawns all block instead of doing each one
    widget_id = Block(canvaswind)
    widget_id.config(cursor="hand2") 
    frame_style = Style()
    frame_style.configure("{}.TFrame".format(widget_id), background="#2e2e2e")
    widget_id.configure(style="{}.TFrame".format(widget_id))  # Set background color
    #The {} only specifies where the entrys will be, the entrys will be placed at the end if not specified
    texts = block["name"].split("{}")
    step = 0
    label_style = Style()
    # Configure a new style for a specific label
    label_style.configure("Custom.TLabel", foreground="white", background="#2e2e2e")
    for text in texts:
        DraggableLabel(widget_id, text=text, style="Custom.TLabel").grid(row=0, column=step, padx=3, pady=3)
        step += 2

    widget_id.widget_id = widget_id #TODO: might cause issues
    widget_id.snapped_to = None
    widget_id.parent = None
    widget_id.snapping = [True, True]
    widget_id.block_id = block["btype"]
    widget_id.values = {}
    spawned_blocks.append(widget_id) #Logs blocks
    #Gets the how many values and their type and sets it in the widget list and properties
    step = 1
    #This will create the entrys for the specified values in block
    for key in block["values"]:
        widget_id.values[key] = StringVar()
        #This will create an entry that modifies the value of the dictionary
        name = Entry(widget_id, textvariable= widget_id.values[key],width=7).grid(row=0, column=step, padx=3, pady=3)
        step += 2
    # widget_id.pack_propagate(False)
    widget_id.pack()

def small_block_spawner(block):
    #This will spawn a small block on the canvas
    widget_id = Small_Block(canvaswind)
    widget_id.config(cursor="hand2") 
    frame_style = Style()
    frame_style.configure("{}.TFrame".format(widget_id), background="#34a1eb")
    widget_id.configure(style="{}.TFrame".format(widget_id))  # Set background color
    #The {} only specifies where the entrys will be, the entrys will be placed at the end if not specified
    texts = block["name"].split("{}")
    step = 0
    label_style = Style()
    # Configure a new style for a specific label
    label_style.configure("Custom.TLabel", foreground="white", background="#2e2e2e")
    for text in texts:
        small_label(widget_id, text=text, style="Custom.TLabel").grid(row=0, column=step, padx=3, pady=3)
        step += 2

    widget_id.widget_id = widget_id #TODO: might cause issues
    widget_id.snapped_to = None
    widget_id.parent = None
    widget_id.snapping = [True, True]
    widget_id.block_id = block["btype"]
    widget_id.values = {}
    spawned_blocks.append(widget_id) #Logs blocks
    #Gets the how many values and their type and sets it in the widget list and properties
    step = 1
    #This will create the entrys for the specified values in block
    for key in block["values"]:
        widget_id.values[key] = StringVar()
        #This will create an entry that modifies the value of the dictionary
        Entry(widget_id, textvariable= widget_id.values[key],width=7).grid(row=0, column=step, padx=3, pady=3)
        step += 2
    # widget_id.pack_propagate(False)
    widget_id.pack()
class Block(Frame):
    def __init__(self, master=None,*args, **kwargs):
        self.widget_id = None #ID of widget
        self.snapped_to = None #ID of widget on top
        self.parent = None #ID of the widget on top of all
        self.snapping = [False, False]  #[Top, Bottom]If the widget is allowed to snap to top or bottom
        self.block_id = None #Type of block
        self.values = {} #Stores the values of the block

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

    def set_coordinates(self, x, y):
        self.place(x=x, y=y)

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

class Small_Block(Block):
    def on_release(self, event):
        if dragging:
            # print("{} Location: x={}, y={}".format(self, self.winfo_x(), self.winfo_y()))
            small_snap(self)
        else:
            print("Button was pressed")

class small_label(DraggableLabel):
    def on_release(self, event):
        if dragging:
            # print("{} Location: x={}, y={}".format(self, self.winfo_x(), self.winfo_y()))
            small_snap(self.master)
        else:
            print("Button was pressed")

def canvasmenu():
    # Create a draggable button
    global draggable_button, second_button #Only used for debug menu
    frame_style = Style()
    frame_style.configure("playground.TFrame", background="#2e2e2e")
    draggable_frame = Block(canvaswind, width=200, height=50) #, text="Drag Me")
    draggable_frame.configure(style="playground.TFrame")  # Set background color
    draggable_frame.pack_propagate(False)
    draggable_frame.pack()
    #make a button that spawns a block
    button = Button(canvaswind, text="Spawn Block", command=lambda: block_spawner(block_test["2"]))
    button.pack()
    button2 = Button(canvaswind, text="print values", command=debug_print)
    button2.pack()
    button3 = Button(canvaswind, text="print snaplog", command=lambda: print(snaplog))
    button3.pack()
    button4 = Button(canvaswind, text="print spawned widgets", command=lambda: print(spawned_widgets))
    button4.pack()
    button5 = Button(canvaswind, text="print spawned blocks", command=lambda: print(spawned_blocks))
    button5.pack()
    button6 = Button(canvaswind, text="print parents", command=debug_parents)
    button6.pack()
    button6 = Button(canvaswind, text="spawn small block", command=lambda: small_block_spawner(block_test["small1"]))
    button6.pack()
    block_spawner(block_test["2"])
    canvaswind.mainloop()
    
def debug_print():
    for widget_id in spawned_blocks:
        print(widget_id.widget_id)
        for key in widget_id.values:
            print(widget_id.values[key].get())
def debug_parents():
    for widget_id in spawned_blocks:
        print("{} --> {}".format(widget_id.widget_id, widget_id.parent))

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
    "3":{
        "name":"Print {}",
        "btype":"block",
        "color":"blue",
        "code":"print({})",
        "values":{
            "value":"any"
        }
    },
    "small1":{
        "name":"Variable {} equals {}",
        "btype":"block",
        "color":"blue",
        "code":"{} = {}",
        "values":{
            "value":"any"
        }
    },
    "small2":{
        "name":"{} + {}",
        "btype":"block",
        "color":"blue",
        "code":"{} + {}",
        "values":{
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

# Run the Tkinter event loop
global snaplog, spawned_widgets, spawned_blocks
snaplog = []
spawned_widgets = {}
spawned_blocks = []
windows()
canvasmenu()