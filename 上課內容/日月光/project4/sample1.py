import tkinter as tk
import tkinter.ttk as ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")

        label = tk.Label(self, text="Hello First Window")
        label.pack(fill=tk.BOTH, expand=tk.YES, padx=100, pady=50)

if __name__ == "__main__":
    window = Window()
    window.mainloop()