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

        btn3=tk.Button(self,text="按鈕3",command=self.btn3_click,padx=30,pady=30)
        btn3.pack(padx=100,pady=50)

    def btn1_click(self):
        if not os.path.isdir('csv'):
            os.makedirs('csv')
        path = "https://raw.githubusercontent.com/roberthsu2003/PythonForDataAnalysis/master/%E8%B3%87%E6%96%99%E9%9B%86/%E5%80%8B%E8%82%A1%E6%97%A5%E6%88%90%E4%BA%A4%E8%B3%87%E8%A8%8A.csv"

        response = requests.get(path)
        with open('csv/個股日成交資訊.csv',mode='w',newline='',encoding='utf-8') as file:
            file.write(response.text)
        

        

    def btn2_click(self):
        if not os.path.isdir('json'):
            os.makedirs('json')
        
        path = "https://raw.githubusercontent.com/roberthsu2003/PythonForDataAnalysis/master/%E8%B3%87%E6%96%99%E9%9B%86/%E6%96%B0%E5%8C%97%E5%B8%82%E5%85%AC%E5%85%B1%E8%87%AA%E8%A1%8C%E8%BB%8A%E7%A7%9F%E8%B3%83%E7%B3%BB%E7%B5%B1.json"

        response = requests.get(path)
        with open('json/新北市公共自行車租賃系統.json',mode='w',encoding='utf-8') as file:
            file.write(response.text)

    def btn3_click(self):
        if not os.path.isdir('excel'):
            os.makedirs('excel')
        
        path = "https://github.com/roberthsu2003/PythonForDataAnalysis/raw/master/%E8%B3%87%E6%96%99%E9%9B%86/%E7%B8%BD%E7%B5%B1.xls"

        response = requests.get(path)        
        with open('excel/總統.xls',mode='wb') as file:
            file.write(response.content)
        



def main():
    window=Window()
    window.title("我的新視窗")
    window.mainloop()

if __name__ == "__main__":
    main()