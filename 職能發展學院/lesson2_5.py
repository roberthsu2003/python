import tkinter as tk

class Window(tk.Tk):
    #override init
    def __init__(self):
        super().__init__()
        self.title("這是物件導向的寫法")
        self.message = tk.Label(self,text="訊息:")
        self.message.pack(padx=100,pady=50)
        leftButton = tk.Button(self, text="LEFT Button",padx=10, pady=10,command=self.leftButtonClick)
        leftButton.pack(side=tk.LEFT,padx=(20,0),pady=(0,20))
        centerButton = tk.Button(self,text="Center Button",padx=10, pady=10,command=self.centerButtonClick)
        centerButton.pack(side=tk.LEFT,pady=(0,20))
        rightButton = tk.Button(self,text="right Button",padx=10, pady=10,command=self.rightButtonClick)
        rightButton.pack(side=tk.LEFT,padx=(0,20),pady=(0,20))

    def leftButtonClick(self):
        self.message.configure(text="訊息:左按鈕被按了")

    def centerButtonClick(self):
        self.message.configure(text="訊息:中間按鈕被按了")


    def rightButtonClick(self):
        self.message.configure(text="訊息:右按鈕被按了")



if __name__ == "__main__":
    window = Window()
    window.mainloop()