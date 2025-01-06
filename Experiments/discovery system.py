from tkinter import Tk, Button

def get_widget_names(parent):
    widget_names = []
    for widget in parent.winfo_children():
        widget_name = widget.winfo_name()
        widget_names.append(widget_name)
    return widget_names

def print_widget_names(parent):
    widget_names = get_widget_names(parent)
    print("Widget Names:", widget_names)

root = Tk()

button1 = Button(root, text="Button 1")
button2 = Button(root, text="Button 2")

button1.pack()
button2.pack()

# Print names of all widgets in the main window
print_widget_names(root)

root.mainloop()
