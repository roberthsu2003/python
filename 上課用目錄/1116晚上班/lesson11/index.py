import tkinter as tk
import os
import requests

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
        path = "https://raw.githubusercontent.com/roberthsu2003/PythonForDataAnalysis/master/%E8%B3%87%E6%96%99%E9%9B%86/%E5%80%8B%E8%82%A1%E6%97%A5%E6%88%90%E4%BA%A4%E8%B3%87%E8%A8%8A.csv"

        response = requests.get(path)
        with open('csv/個股日成交資訊.csv',mode='w',newline='',encoding='utf-8') as file:
            file.write(response.text)
        

        

    def btn2_click(self):
        print("按鈕2的click")


def main():
    window=Window()
    window.title("我的新視窗")
    window.mainloop()

if __name__ == "__main__":
    main()