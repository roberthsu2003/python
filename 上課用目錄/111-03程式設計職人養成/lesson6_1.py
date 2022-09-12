import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("上市公司每月營業收入彙種表")
        tk.Label(self,text="上市公司每月營業收入彙種表",font=("arial",20)).pack()

def main():
   window = Window()
   window.mainloop()

if __name__ == "__main__":
    main()