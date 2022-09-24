import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("這是我的第一個視窗")
        self.geometry("800x300")

def main():
    #chinese和english區域變數
    window = Window()   
    window.mainloop()

if __name__ == "__main__":
    main()
    
