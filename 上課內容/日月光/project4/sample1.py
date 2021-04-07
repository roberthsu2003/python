import tkinter as tk
import tkinter.ttk as ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        #self.geometry("400x200")

        label = tk.Label(self, text="Hello First Window", padx=100, pady=50, font=('Times', 24, 'bold italic'))
        label.pack(expand=True)

if __name__ == "__main__":
    window = Window()
    window.mainloop()