import tkinter as tk
from tkinter import messagebox
from Page1 import Page1
from Page2 import Page2

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("900x600")
        self.title("Main Menu")      
        self.frames = [ Page1(self),Page2(self)]
        self.switchFrame(0)

    def switchFrame(self, frameNum):
        # hide all frames except the one chosen
        for i in range(len(self.frames)):
            frame = self.frames[i]
            if i == frameNum:
                frame.grid(row=0, column=0, sticky="NSWE")
                frame.loadUp()
            else:
                frame.grid_forget()


app = Main()
app.mainloop()
