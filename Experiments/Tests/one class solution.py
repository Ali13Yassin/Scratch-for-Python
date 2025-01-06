import tkinter as tk

class Draggable:
    def __init__(self, widget):
        self.widget = widget
        widget.bind("<Button-1>", self.start_drag)
        widget.bind("<B1-Motion>", self.drag)
        self.x = 0
        self.y = 0

    def start_drag(self, event):
        self.x = event.x
        self.y = event.y

    def drag(self, event):
        dx = event.x - self.x
        dy = event.y - self.y
        self.widget.place_configure(x=self.widget.winfo_x() + dx, y=self.widget.winfo_y() + dy)

root = tk.Tk()
frame = tk.Frame(root, width=100, height=100, bg='red')
frame.place(x=50, y=50)
label = tk.Label(root, text="Drag me", bg='blue')
label.place(x=200, y=200)

Draggable(frame)
Draggable(label)

root.mainloop()