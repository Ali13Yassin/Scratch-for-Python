import tkinter as tk

def add_button():
    new_button = tk.Button(wind, text=f"Button {len(buttons) + 1}")
    new_button.pack(pady=5)
    buttons.append(new_button)

# Create the main window
root = tk.Tk()
root.title("Dynamic Widgets Demo")
wind = tk.Tk()
wind.title("Window 2")

# List to store references to created buttons
buttons = []

# Create a button to add more buttons
add_button = tk.Button(root, text="Add Button", command=add_button)
add_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
wind.mainloop()
