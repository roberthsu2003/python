import tkinter as tk

class Window(tk.Tk):
    pass

def main():
    #chinese和english區域變數
    window = Window()
    window.title("這是我的第一個視窗")
    window.geometry("800x300")
    window.mainloop()

if __name__ == "__main__":
    main()
    
