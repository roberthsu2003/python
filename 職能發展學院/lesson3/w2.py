import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("tk button")
        label = tk.Label(self, text="選擇一個按鈕",font=("arial",20))
        label.pack(padx=100, pady=50)

        hello_button = tk.Button(self, text="Say Hello",font=("arial", 20),padx=5,pady=5)
        hello_button.pack(side=tk.LEFT,padx=20,pady=20)

        goodbye_button = tk.Button(self, text="Say Goodbye", font=("arial", 20), padx=5, pady=5)
        goodbye_button.pack(side=tk.RIGHT, padx=20, pady=20)

if __name__ == "__main__":
    window = Window()
    window.mainloop()