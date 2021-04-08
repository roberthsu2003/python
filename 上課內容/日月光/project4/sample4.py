import tkinter as tk
import tkinter.messagebox as msgbox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        self.label_text = tk.StringVar()
        self.label_text.set("請問您的姓名是:")

        label = tk.Label(self, textvariable=self.label_text ,font=('Times', 24, 'bold italic'))
        label.pack(expand=True,padx=100, pady=(30,10))

        self.name_text = tk.StringVar()

        name_entry = tk.Entry(self,textvariable=self.name_text,font=('Times', 24, 'bold italic'))
        name_entry.pack(pady=(0,30))

        hello_button = tk.Button(self, text="Say Hello",padx=20,pady=10,font=('Times', 20), command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20,0), pady=(0,20))

        goodbye_button = tk.Button(self, text="Say Goodbye", padx=20, pady=10, font=('Times', 20), command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(20, 20), pady=(0, 20))

    def say_hello(self):
        message = "Hello,您的名字是" + self.name_text.get()
        msgbox.showinfo("Hello", message)

    def say_goodbye(self):
        if msgbox.askyesno("關閉視窗嗎?",f"{self.name_text.get()},真的想要關閉視窗嗎?"):
            self.label_text.set("Goodbye!(2秒後引爆)")
            self.after(2000, self.destroy)
        else:
            msgbox.showinfo("不會關閉視窗", f"{self.name_text.get()}非常好!將回到原視窗")

if __name__ == "__main__":
    window = Window()
    window.mainloop()



