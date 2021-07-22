import requests
import tkinter as tk
from tkinter.font import Font
from time import strptime


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


        #建立下方radioButton的介面
        self.fixedWidthFrame = tk.Frame(self,height=600,bg='red')
        self.createdRadioButtonFrame()
        self.fixedWidthFrame.pack(padx=20)

        #建立message介面
        messageDisplayFrame = tk.Frame(self,bd=2,relief=tk.GROOVE,padx=20,pady=10)
        self.mdayLabel = tk.Label(messageDisplayFrame, text="記錄時間:")
        self.mdayLabel.pack(anchor=tk.W)
        self.snaLabel = tk.Label(messageDisplayFrame,text="站名:")
        self.snaLabel.pack(anchor=tk.W)
        self.arLabel = tk.Label(messageDisplayFrame,text="地址:")
        self.arLabel.pack(anchor=tk.W)
        self.bempLabel = tk.Label(messageDisplayFrame, text="空位數量:")
        self.bempLabel.pack(anchor=tk.W)
        self.sbiLabel = tk.Label(messageDisplayFrame, text="可借車數:")
        self.sbiLabel.pack(anchor=tk.W)
        self.totLabel = tk.Label(messageDisplayFrame, text="總車數:")
        self.totLabel.pack(anchor=tk.W)
        messageDisplayFrame.pack(expand=True,fill=tk.BOTH,padx=20,pady=30)




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
        self.createdRadioButtonFrame(data=snaList)


    def createdRadioButtonFrame(self,data=None):
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
        datetimeString = infomation["mday"]
        datetimeFormat = "%Y%m%d%H%M%S"
        structTime = strptime(datetimeString,datetimeFormat)

        self.mdayLabel["text"] = "記錄時間:%d年%d月%d日  %d:%d:%d" % (structTime.tm_year,structTime.tm_mon,structTime.tm_mday,structTime.tm_hour,structTime.tm_min,structTime.tm_sec)
        self.snaLabel["text"] = "站名:%s" % infomation["sna"]
        self.arLabel.configure(text="地址:{0:s}".format(infomation["ar"]))
        self.bempLabel["text"] = "空位數量:{0:d}".format(infomation["bemp"])
        self.sbiLabel["text"] = "可借車數:{0:d}".format(infomation["sbi"])
        self.totLabel["text"] = "總車數:{0:d}".format(infomation["tot"])

if __name__ == "__main__":
    window = Window()
    window.mainloop()
