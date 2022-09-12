import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("side")
        fm = tk.Frame(self)
        tk.Button(fm,text="Top",font=('verdana',20)).pack(side=tk.TOP)
        tk.Button(fm,text="Center",font=('verdana',20)).pack(side=tk.LEFT)
        tk.Button(fm,text="Bottom",font=('verdana',20)).pack(side=tk.RIGHT)
        fm.pack()
        


def main():
    window = Window()    
    window.mainloop()

if __name__ == '__main__':
    main()