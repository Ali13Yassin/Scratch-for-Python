#This is a program that allow a button to be moved without triggering the on-press function,
#and the other button will check the coordinates of the moved button
import tkinter as tk

class DraggableButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        tk.Button.__init__(self, master, **kwargs)
        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        x_delta = event.x - self.start_x
        y_delta = event.y - self.start_y
        self.place(x=self.winfo_x() + x_delta, y=self.winfo_y() + y_delta)
        self.start_x = event.x
        self.start_y = event.y

# Create the main window
root = tk.Tk()
root.title("Draggable Button Demo")

# Function to get the current location of the button
def get_button_location():
    print("Button Location: x={}, y={}".format(draggable_button.winfo_x(), draggable_button.winfo_y()))

# Create a draggable button
draggable_button = DraggableButton(root, text="Drag Me", command=get_button_location)
draggable_button.pack()

# Create a button to check the location
check_location_button = tk.Button(root, text="Check Location", command=get_button_location)
check_location_button.pack()


# Run the Tkinter event loop
root.mainloop()
