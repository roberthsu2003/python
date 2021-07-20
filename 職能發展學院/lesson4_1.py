import tkinter as tk
from tkinter import Button

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lesson4_1")

        Button(self,text='LEFT',width=15).pack(side=tk.LEFT)
        Button(self, text='Center',width=15).pack(side=tk.LEFT)
        Button(self, width=15,text='Right').pack(side=tk.RIGHT)



if __name__ == "__main__":
    window = Window()
    window.mainloop()