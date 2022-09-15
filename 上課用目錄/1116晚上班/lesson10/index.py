import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("這是我的視窗程式")
               

def main():
    window = Window()
    window.mainloop()


if __name__ == "__main__":
    main()