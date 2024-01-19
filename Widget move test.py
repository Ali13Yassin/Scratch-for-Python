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

# Function to move the button to specified coordinates
def move_button(x, y):
    draggable_button.place(x=x, y=y)

# Create the main window
root = tk.Tk()
root.title("Move Draggable Button Demo")

# Create a draggable button
draggable_button = DraggableButton(root, text="Drag Me")
draggable_button.pack()

# Create a button to move the draggable button
move_button_button = tk.Button(root, text="Move Button", command=lambda: move_button(100, 100))
move_button_button.pack()

# Run the Tkinter event loop
root.mainloop()
