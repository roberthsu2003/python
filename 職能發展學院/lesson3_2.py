import requests
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #取得網路上的資料
        res = requests.get('https://flask-robert.herokuapp.com/youbike')
        jsonObj = res.json()
        areas = jsonObj['areas']

        #介面
        topFrame = tk.Frame(self)
        for area in areas:
            tk.Button(topFrame,text=area).pack(side=tk.LEFT)
        topFrame.pack(padx=100, pady=(30,60))




if __name__ == "__main__":
    window = Window()
    window.title("台北市行政區")
    window.mainloop()
