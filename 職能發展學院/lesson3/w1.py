import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("第一個視窗")

if __name__ == "__main__":
    window = Window()
    window.mainloop()