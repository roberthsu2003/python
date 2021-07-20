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
        self.title("台北市行政區")
        topFrame = tk.Frame(self,bd=2,relief=tk.GROOVE,padx=20,pady=10)
        buttonFont = Font(family='Helvetica', size=20)

        for index, area in enumerate(areas):
            if index % 6 == 0:
                parentframe = tk.Frame(topFrame)
                parentframe.pack()
            btn = tk.Button(parentframe, text=area, font=buttonFont, padx=5, pady=5)
            btn.bind('<Button-1>', self.userClick)
            btn.pack(side=tk.LEFT, padx=5)
        topFrame.pack(padx=20, pady=30)



        self.fixedWidthFrame = tk.Frame(self,width=500,bg='red')
        self.createdBottomFrame()
        self.fixedWidthFrame.pack(side=tk.LEFT,padx=20)


    def userClick(self,event):
        self.bottomFrame.destroy()
        selectedArea = event.widget['text']
        urlString = "https://flask-robert.herokuapp.com/youbike/%s" % selectedArea
        res = requests.get(urlString)
        jsonobj = res.json()
        self.areas = jsonobj['data']
        snaList = []
        for area in self.areas:
            snaList.append(area["sna"])
        self.createdBottomFrame(data=snaList)


    def createdBottomFrame(self,data=None):
        self.bottomFrame = tk.Frame(self.fixedWidthFrame, bd=2, relief=tk.GROOVE, padx=20, pady=10)
        if data == None:
            urlString = "https://flask-robert.herokuapp.com/youbike/南港區"
            res = requests.get(urlString)
            jsonobj = res.json()
            self.areas = jsonobj['data']
            snaList = []
            for area in self.areas:
                snaList.append(area["sna"])
            self.radioButtonData = snaList
        else:
            self.radioButtonData = data

        self.var = tk.IntVar()
        for index, data in enumerate(self.radioButtonData):
            if index % 10 == 0:
                parentframe = tk.Frame(self.bottomFrame)
                parentframe.pack(side=tk.LEFT,expand=True,fill=tk.Y)
            radioButton = tk.Radiobutton(parentframe, text=data, value=index, variable=self.var,command=self.userChoicedRadioButton).pack(anchor=tk.W)
        self.bottomFrame.pack()
        self.var.set(0)

    def userChoicedRadioButton(self):
        index = self.var.get()
        infomation = self.areas[index]
        print(infomation)

if __name__ == "__main__":
    window = Window()
    window.mainloop()
