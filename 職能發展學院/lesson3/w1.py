import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("第一個視窗")
        label = tk.Label(self,text="Hello! Tkinter.",background="#777777",font=("arias", 20))
        label.pack(pady=100,padx=50)

if __name__ == "__main__":
    window = Window()
    window.mainloop()