import tkinter as tk

class DraggableWidget:
    def __init__(self, root, *frames):
        self.root = root
        self.frames = frames

        self.canvas = tk.Canvas(root, width=400, height=200, bg='white')
        self.canvas.pack()

        self.widget = tk.Frame(self.root, width=50, height=50, bg='blue')
        self.widget.place(x=50, y=50)  # Initial placement

        self.widget.bind('<ButtonPress-1>', self.on_press)
        self.widget.bind('<B1-Motion>', self.on_drag)

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        x, y = event.x, event.y
        self.widget.place(x=self.widget.winfo_x() + x - self.start_x, y=self.widget.winfo_y() + y - self.start_y)
        self.start_x = x
        self.start_y = y

        # Check if the widget is over any frame
        widget_bbox = self.widget.bbox()

        for frame in self.frames:
            frame_bbox = (
                frame.winfo_rootx(),
                frame.winfo_rooty(),
                frame.winfo_rootx() + frame.winfo_width(),
                frame.winfo_rooty() + frame.winfo_height(),
            )

            if self.intersect(widget_bbox, frame_bbox):
                print(f"Widget over Frame {self.frames.index(frame) + 1}")
                break

    def intersect(self, bbox1, bbox2):
        x1, y1, x2, y2 = bbox1
        x3, y3, x4, y4 = bbox2
        return not (x2 < x3 or x1 > x4 or y2 < y3 or y1 > y4)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Draggable Widget Example")

    frame1 = tk.Frame(root, width=200, height=200, bg='lightgreen')
    frame1.pack(side='left')

    frame2 = tk.Frame(root, width=200, height=200, bg='lightblue')
    frame2.pack(side='right')

    frame3 = tk.Frame(root, width=200, height=200, bg='lightyellow')
    frame3.pack(side='bottom')

    draggable_widget = DraggableWidget(root, frame1, frame2, frame3)

    root.mainloop()
