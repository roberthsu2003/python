import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("side")        
        fm = tk.Frame(self,background="#eeeeee")
        tk.Button(fm,text="Top",font=('verdana',20)).pack(side=tk.TOP,expand=True,fill=tk.X)
        tk.Button(fm,text="Center",font=('verdana',20)).pack(side=tk.TOP,expand=True,fill=tk.X)
        tk.Button(fm,text="Bottom",font=('verdana',20)).pack(side=tk.TOP,expand=True,fill=tk.X)
        fm.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

        fm1 = tk.Frame(self,background="#eeeeee")
        tk.Button(fm1,text="Top",font=('verdana',20)).pack(side=tk.LEFT,expand=True,fill=tk.Y)
        tk.Button(fm1,text="Center",font=('verdana',20)).pack(side=tk.LEFT,expand=True,fill=tk.Y)
        tk.Button(fm1,text="Bottom",font=('verdana',20)).pack(side=tk.LEFT,expand=True,fill=tk.Y)
        fm1.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        


def main():
    window = Window()    
    window.mainloop()

if __name__ == '__main__':
    main()