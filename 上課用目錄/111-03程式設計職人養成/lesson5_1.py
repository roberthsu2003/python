import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Event")
        fm = tk.Frame(self,background="#eeeeee")
        fm.pack(expand=True,fill=tk.BOTH,padx=20,pady=20)
        


def main():
    window = Window()    
    window.mainloop()

if __name__ == '__main__':
    main()