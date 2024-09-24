import tkinter as tk
from tkinter import messagebox

class Page1(tk.Frame):
    def __init__(self, parent):
        
        #Call parent constructor
        self.parent = parent
        tk.Frame.__init__(self, parent)
       
        #Set up my page
        someText = tk.Label(self,text = "This is page 1")
        someText.grid(row=0,column=0)
        page2Button = tk.Button(self, text="Go to Page 2", command = self.GoToPage2)
        page2Button.grid(row=0,column=1)
    
    def GoToPage2(self):
        self.parent.switchFrame(1)
        
    def loadUp(self):
        print("loaded page 1")
        
