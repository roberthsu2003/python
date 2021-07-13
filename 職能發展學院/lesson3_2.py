import requests
import tkinter as tk
from tkinter.font import Font


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #取得網路上的資料
        res = requests.get('https://flask-robert.herokuapp.com/youbike')
        jsonObj = res.json()
        areas = jsonObj['areas']

        #介面
        topFrame = tk.Frame(self,bd=2,relief=tk.GROOVE,padx=20,pady=10)
        buttonFont = Font(family='Helvetica', size=20)
        for area in areas:
            btn = tk.Button(topFrame,text=area,font=buttonFont,padx=5,pady=5)
            btn.bind('<Button-1>',self.userClick)
            btn.pack(side=tk.LEFT,padx=5)

        topFrame.pack(padx=100, pady=(30,60))

    def userClick(self,event):
        selectedArea = event.widget['text']
        urlString = "https://flask-robert.herokuapp.com/youbike/%s" % selectedArea
        res = requests.get(urlString)
        jsonobj = res.json()
        print(jsonobj)




if __name__ == "__main__":
    window = Window()
    window.title("台北市行政區")
    window.mainloop()
