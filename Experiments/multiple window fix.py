from tkinter import Tk, Button, Label, Toplevel

def open_new_window():
    new_window = Toplevel(root)
    new_window.title("New Window")

    # Add widgets to the new window
    label = Label(new_window, text="This is a new window!")
    label.pack(padx=20, pady=20)

    close_button = Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)

# Create the main window
root = Tk()
root.title("Main Window")

# Add widgets to the main window
label = Label(root, text="Click the button to open a new window.")
label.pack(padx=20, pady=20)

open_button = Button(root, text="Open New Window", command=open_new_window)
open_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
