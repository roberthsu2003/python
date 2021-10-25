import tkinter as tk
import tkinter.messagebox as msgbox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("tk button")

        self.label_text = tk.StringVar()
        self.label_text.set("請輸入姓名:")

        label = tk.Label(self,textvar=self.label_text,font=("arial",20))
        label.pack(padx=100, pady=50)

        self.name_text = tk.StringVar()
        name_entry = tk.Entry(self, textvar=self.name_text)
        name_entry.pack(padx=20,pady=20)

        hello_button = tk.Button(self, text="Say Hello",font=("arial", 20),padx=5,pady=5,command=self.say_hello)
        hello_button.pack(side=tk.LEFT,padx=20,pady=20)

        goodbye_button = tk.Button(self, text="Say Goodbye", font=("arial", 20), padx=5, pady=5,command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=20, pady=20)


    def say_goodbye(self):
        if msgbox.askyesno("Close Window?","Would you like to close this window?"):
            self.label_text.set("GoodBye! \n 2秒鐘後")
            self.after(2000,self.destroy)
        else:
            msgbox.showerror("noClose", "Not Close")

    def say_hello(self):
        name = self.name_text.get()
        msgbox.showinfo("Hello",f"{name}您好")

if __name__ == "__main__":
    window = Window()
    window.mainloop()