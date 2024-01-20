import tkinter as tk

main = tk.Tk()

def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event): #Happens when button is clickeed or once when dragged
    print("on_drag_start")
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event): #Happens every frame the button is being actually dragged
    print("on_drag_motion")
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)

frame = tk.Frame(main, bd=4, bg="grey")
# frame.place(x=10, y=10)
butt = tk.Button(main, text="button")
butt.place(x=10, y=10)
make_draggable(butt)

notes = tk.Text(frame)
notes.pack()
main.mainloop()