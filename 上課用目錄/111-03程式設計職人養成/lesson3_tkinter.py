import tkinter as tk
from tkinter import *

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.option_add('*font',('verdana', 12, 'bold'))
        self.title("lesson2_3")

        Button(self, text='Top').pack(side=TOP)
        Button(self, text='This is th Center button').pack(side=TOP)
        Button(self, text='Bottom').pack(side=TOP)

if __name__ == "__main__":
    window = Window()
    window.mainloop()