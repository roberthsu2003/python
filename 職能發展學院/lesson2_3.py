import tkinter as tk

class Window(tk.Tk):
    #override init
    def __init__(self):
        super().__init__()
        self.title("這是物件導向的寫法")
        lable = tk.Label(self,text="Hello tkinter")
        lable.pack(padx=100,pady=50)

if __name__ == "__main__":
    window = Window()
    window.mainloop()