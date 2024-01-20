import tkinter as tk

class DraggableButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        tk.Button.__init__(self, master, **kwargs)
        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        global dragging
        dragging = False

    def on_drag(self, event):
        x_delta = event.x - self.start_x
        y_delta = event.y - self.start_y
        self.place(x=self.winfo_x() + x_delta, y=self.winfo_y() + y_delta)
        self.start_x = event.x
        self.start_y = event.y
        global dragging
        dragging = True

    def on_release(self, event):
        if dragging:
            print("Dragging stopped")
        else:
            print("Button was pressed")

# Create the main window
root = tk.Tk()
root.title("Draggable Button Demo")

# Create a draggable button
draggable_button = DraggableButton(root, text="Drag Me")
draggable_button.pack()

# Run the Tkinter event loop
root.mainloop()
