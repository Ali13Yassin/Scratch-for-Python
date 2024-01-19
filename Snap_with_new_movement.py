#------------------------------------<Initialization Start>-------------------------------------------------------
from tkinter import * #The UI module that this program relies on
from tkinter import messagebox #This is a function that allows making windows message boxes, has to be called separetly
from tkinter.ttk import * #Theamed tkinter which makes the UI look ever so slightly modern
import os #Used to change directory, and other things
from pathlib import Path #Used to get the path to the python file

os.chdir(Path(__file__).parent)

def snap():
        X = draggable_button.winfo_x()
        Y = draggable_button.winfo_y()
        x = second_button.winfo_x()
        y = second_button.winfo_y()
        if x-X <= 75 and x-X >= -75:
            if y-Y <= 40 and y-Y >=0:
                print("Snapped!")
                second_button.place(x=X, y=Y+24)

            elif Y-y <= 40 and Y-y >=0: #Checks if the button is ontop of the other one
                print("Negative Snapped!")
                second_button.place(x=X, y=Y+24)

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
        global dragging
        dragging = True

    def on_drag_motion(self, event): #Happens every frame the button is being actually dragged
        x = self.winfo_x() - self._drag_start_x + event.x
        y = self.winfo_y() - self._drag_start_y + event.y
        self.place(x=x, y=y)

    def on_release(self, event):
        if dragging:
            print("{} Location: x={}, y={}".format(self, self.winfo_x(), self.winfo_y()))
            snap()
        else:
            print("Button was pressed")

buttons = []

def add_button():
    new_button = DraggableButton(wind, text=f"Button {len(buttons) + 1}")
    new_button.pack(pady=5)
    buttons.append(new_button)
# Create the main window
root = Tk()
root.title("Draggable Button Demo")
wind = Tk()
wind.title("Window 2")

def move_button(x, y):
    draggable_button.place(x=x, y=y)

# Function to get the current location of the button
def get_button_location():
    print("Button Location: x={}, y={}".format(draggable_button.winfo_x(), draggable_button.winfo_y()))

# Create a draggable button
draggable_button = DraggableButton(wind, text="Drag Me", command=lambda: print("pressed!!!"))
draggable_button.pack()
second_button = DraggableButton(wind, text="Drag Me Too")
second_button.pack()

# Create a button to check the location
check_location_button = Button(root, text="Check Location", command=get_button_location)
check_location_button.pack()

buttons = []

# Create a button to add more buttons
add_button = Button(root, text="Add Button", command=add_button)
add_button.pack(pady=10)
move_button_button = Button(root, text="Move Button", command=lambda: move_button(100, 100))
move_button_button.pack()

# Run the Tkinter event loop
root.mainloop()
wind.mainloop()