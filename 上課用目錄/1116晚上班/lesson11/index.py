import tkinter as tk
import os

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        btn1=tk.Button(self,text="按鈕1",command=self.btn1_click,padx=30,pady=30)
        btn1.pack(padx=100,pady=50)

        btn2=tk.Button(self,text="按鈕2",command=self.btn2_click,padx=30,pady=30)
        btn2.pack(padx=100,pady=50)

    def btn1_click(self):
        if not os.path.isdir('csv'):
            os.makedirs('csv')
        

    def btn2_click(self):
        print("按鈕2的click")


def main():
    window=Window()
    window.title("我的新視窗")
    window.mainloop()

if __name__ == "__main__":
    main()