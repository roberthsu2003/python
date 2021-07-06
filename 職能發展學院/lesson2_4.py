import tkinter as tk

class Window(tk.Tk):
    #override init
    def __init__(self):
        super().__init__()
        self.title("這是物件導向的寫法")
        lable = tk.Label(self,text="請選擇其中一個按鈕")
        lable.pack(padx=100,pady=50)
        hello_button = tk.Button(self, text="Say Hello",padx=10, pady=10)
        hello_button.pack(side=tk.LEFT,padx=(20,0),pady=(0,20))
        goodbye_button = tk.Button(self,text="再見",padx=10, pady=10)
        goodbye_button.pack(side=tk.RIGHT,padx=(0,20),pady=(0,20))

if __name__ == "__main__":
    window = Window()
    window.mainloop()