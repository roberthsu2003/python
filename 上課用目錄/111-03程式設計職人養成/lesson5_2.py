import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Event")
        fm = tk.Frame(self,background="#eeeeee")
        btn = tk.Button(fm,text="Click Me")
        btn.bind("<Button-1>",self.enter)
        btn.pack(expand=True,fill=tk.BOTH)
        fm.pack(expand=True,fill=tk.BOTH,padx=20,pady=20)

    def enter(self,event):
        print(f"enter Frame: x={event.x}, y={event.y}")
        


def main():
    window = Window()    
    window.mainloop()

if __name__ == '__main__':
    main()