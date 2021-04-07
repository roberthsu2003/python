import tkinter as tk
import tkinter.ttk as ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        #self.geometry("400x200")

        label = tk.Label(self, text="Choose One", padx=100, pady=30, font=('Times', 24, 'bold italic'))
        label.pack(expand=True)

        hello_button = tk.Button(self, text="Say Hello",padx=20,pady=10,font=('Times', 20), command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20,0), pady=(0,20))

        goodbye_button = tk.Button(self, text="Say Goodbye", padx=20, pady=10, font=('Times', 20), command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(20, 20), pady=(0, 20))

    def say_hello(self):
        print("say_hello")

    def say_goodbye(self):
        print("say_goodbye")

if __name__ == "__main__":
    window = Window()
    window.mainloop()