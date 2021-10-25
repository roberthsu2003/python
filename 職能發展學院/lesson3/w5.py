import tkinter as tk
import tkinter.messagebox as msgbox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("tk button")

        self.label_text = tk.StringVar()
        self.label_text.set("請選擇一個按鈕")
        label = tk.Label(self,textvar=self.label_text,font=("arial",20))
        label.pack(padx=100, pady=50)

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
        #self.label_text.set("Hello! Python!")
        msgbox.showerror("Hello","Hello! python!")

if __name__ == "__main__":
    window = Window()
    window.mainloop()