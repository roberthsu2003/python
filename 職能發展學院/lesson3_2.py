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

        bottomFrame = tk.Frame(self,bd=2,relief=tk.GROOVE,padx=20,pady=10)
        radioButtonData = ['仁愛林森路口', '捷運善導寺站(1號出口)', '南昌公園', '國家圖書館', '捷運臺大醫院(4號出口)', '信義連雲街口', '捷運西門站(3號出口)', '和平重慶路口', '金山市民路口', '華山文創園區', '臺北市客家文化主題公園', '捷運小南門站(1號出口)', '臺北轉運站', '羅斯福寧波東街口', '河堤國小', '植物園', '捷運古亭站(2號出口)', '臺北市立大學', '信義杭州路口(中華電信總公司)', '中山堂', '螢橋國小', '濟南紹興路口', '牯嶺公園', '自來水園區', '捷運忠孝新生站(2號出口)', '光華商場', '莒光大埔街口', '重慶南海路口', '中正運動中心', '博愛寶慶路口', '中山青島路口', '紀州庵', '南門國中', '聯合醫院和平院區']
        self.var = tk.IntVar()
        for index,data in enumerate(radioButtonData):
            radioButton = tk.Radiobutton(bottomFrame,text=data,value=index,variable=self.var).pack(anchor=tk.W)
        bottomFrame.pack(padx=100, pady=(30,60),expand=True,fill=tk.X)
        self.var.set(0)

    def userClick(self,event):
        selectedArea = event.widget['text']
        urlString = "https://flask-robert.herokuapp.com/youbike/%s" % selectedArea
        res = requests.get(urlString)
        jsonobj = res.json()
        areas = jsonobj['data']
        snaList = []
        for area in areas:
            snaList.append(area["sna"])
        print(snaList)




if __name__ == "__main__":
    window = Window()
    window.title("台北市行政區")
    window.mainloop()
