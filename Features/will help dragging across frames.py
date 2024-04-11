import tkinter as tk

class Example:
    def __init__(self):
        self.root = tk.Tk()
        self.lf1 = tk.LabelFrame(self.root, text="Choose me!", width=200, height=200)
        self.lf2 = tk.LabelFrame(self.root, text="No! Choose me!", width=200, height=200)

        self.lf1.pack(side="left", fill="both", expand=True)
        self.lf2.pack(side="right", fill="both", expand=True)

        self.button = tk.Button(self.root, text="Click me", command=self.on_click)
        self.button.place(in_=self.lf1, x=20, y=20)

    def start(self):
        self.root.mainloop()

    def on_click(self):
        current_frame = self.button.place_info().get("in")
        new_frame = self.lf1 if current_frame == self.lf2 else self.lf2
        self.button.place(in_=new_frame, x=20, y=20)


Example().start()