import data
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        '''
        for county in countyList:
            print(county.siteName, county.name, county.AQI, county.status, county.publishTime)
        '''
        titleFrame = tk.Frame(self)
        borderFrame = tk.Frame(titleFrame,borderwidth = 1, relief=tk.GROOVE,padx=20,pady=20)
        tk.Label(borderFrame,text="全省空氣品質指標_AQI",font=("Courier", 25, "italic")).pack()
        self.publishTimeLabel = tk.Label(borderFrame,text="發佈時間:"+countyList[0].publishTime)
        self.publishTimeLabel.pack()
        tk.Button(borderFrame,text="更新",padx=10,pady=10,command=self.userClickUpdate).pack(pady=(20,0),anchor=tk.E)
        borderFrame.pack()
        titleFrame.pack(padx=20,pady=20)

        #建立下方的frame
        self.createDisplayFrame() #建立顯示資料的frame


    def createDisplayFrame(self):
        #建立bottomRootFrame
        self.bottomRootFrame = tk.Frame(self)
        #建立canvas
        canvas = tk.Canvas(self.bottomRootFrame)
        #canvasScrollbar
        canvasScorllBar = tk.Scrollbar(self.bottomRootFrame, orient="vertical", command=canvas.yview)
        canvasScorllBar.pack(side=tk.RIGHT,fill=tk.Y)
        # 下方的frame
        self.displayFrame = tk.Frame(canvas,bg='#cccccc')
        self.displayFrame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        for index, county in enumerate(countyList):
            tk.Label(self.displayFrame, text=county.name, bg='#cccccc').grid(row=index, column=0);
            tk.Label(self.displayFrame, text=county.siteName, bg='#cccccc').grid(row=index, column=1);
            tk.Label(self.displayFrame, text=county.AQI, bg='#cccccc').grid(row=index, column=2);
            statusLabel = tk.Label(self.displayFrame, text=county.status, bg='#cccccc');
            if county.status != '良好':
                statusLabel['fg'] = 'red'
            statusLabel.grid(row=index, column=3)
        canvas.create_window((0,0),window=self.displayFrame, anchor=tk.NW)
        canvas.configure(yscrollcommand=canvasScorllBar.set)
        canvas.pack(side=tk.LEFT)
        self.bottomRootFrame.pack(padx=20,pady=20)

    def updateWindow(self):
        self.bottomRootFrame.destroy()
        self.createDisplayFrame()
        self.publishTimeLabel['text'] = "發佈時間:"+countyList[0].publishTime



    def userClickUpdate(self):
        data.updateData() #更新資料
        self.updateWindow() #更新畫面






if __name__ == "__main__":
    countyList = data.aqiData
    window = Window()
    window.title("AQI指標")
    window.mainloop()

