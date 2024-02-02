import tkinter as tk

class DraggableLabel(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        tk.Label.__init__(self, parent, *args, **kwargs)
        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        x = self.winfo_rootx() + (event.x - self.start_x)
        y = self.winfo_rooty() + (event.y - self.start_y)
        self.master.geometry(f"+{x}+{y}")

# Create the main window
root = tk.Tk()
root.title("Draggable Label Example")

# Create a label outside the class
label = tk.Label(root, text="Not draggable")
label.pack()

# Create a DraggableLabel
draggable_label = DraggableLabel(root, text="Drag me!", width=10, height=2, bg="lightblue")
draggable_label.pack()

# Run the Tkinter event loop
root.mainloop()
