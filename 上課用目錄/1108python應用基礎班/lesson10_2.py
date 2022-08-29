import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        tk.Frame(self,width=700,height=250,borderwidth=1,relief=tk.GROOVE).grid(column=0,row=0,padx=20,pady=20)

def main():
    window = Window()
    window.title("全球_covid19_最新統計")
    window.mainloop()

if __name__ == "__main__":
    main()
