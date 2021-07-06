import tkinter as tk

class Window(tk.Tk):
    #override init
    def __init__(self):
        super().__init__()
        self.title("這是物件導向的寫法")
        self.lable = tk.Label(self,text="請選擇其中一個按鈕")
        self.lable.pack(padx=100,pady=50)
        helloButton = tk.Button(self, text="Say Hello",padx=10, pady=10,command=self.say_hello)
        helloButton.pack(side=tk.LEFT,padx=(20,0),pady=(0,20))
        goodbyeButton = tk.Button(self,text="再見",padx=10, pady=10,command=self.say_goodbye)
        goodbyeButton.pack(side=tk.RIGHT,padx=(0,20),pady=(0,20))

    def say_hello(self):
        self.lable.configure(text="您選擇了sayHello")
        print("sayHello")

    def say_goodbye(self):
        self.lable.configure(text="您選擇了sayGoodbye,2秒後關閉視窗")
        self.after(2000,self.destroy)
        print("sayGoodbye")



if __name__ == "__main__":
    window = Window()
    window.mainloop()