from tkinter import *

r = Tk()
r.geometry("400x400")

t = Text(r,)
t.pack()

def change_text_size():
    t.config(pady=4000)  # Change the font size to 12  # Change the internal padding of the Text widget to 3 pixels
button = Button(r, text="Change Text Size", command=change_text_size)
button.pack()

r.mainloop()