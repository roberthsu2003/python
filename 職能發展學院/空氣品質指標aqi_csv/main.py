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
        publishTimeLabel = tk.Label(borderFrame,text="發佈時間:2021-07-27 10:00:00")
        publishTimeLabel.pack()
        tk.Button(borderFrame,text="更新",padx=10,pady=10).pack(pady=(20,0),anchor=tk.E)
        borderFrame.pack()
        titleFrame.pack(padx=20,pady=20)

        #下方的frame
        displayFrame = tk.Frame(self)
        #設定分欄
        columnsNum = 5
        rowsNum = len(countyList) // columnsNum + 1
        for index,county in enumerate(countyList):
            subIndex = index % rowsNum
            if subIndex == 0:
                tableFrame = tk.Frame(displayFrame)
                tableFrame.pack(side=tk.LEFT,padx=(20,0),expand=True,fill=tk.Y)
            tk.Label(tableFrame, text=county.siteName).grid(row=subIndex, column=0);
            tk.Label(tableFrame, text=county.name).grid(row=subIndex, column=1);
            tk.Label(tableFrame, text=county.AQI).grid(row=subIndex, column=2);
            tk.Label(tableFrame, text=county.status).grid(row=subIndex, column=3);
        displayFrame.pack()



if __name__ == "__main__":
    countyList = data.aqiData
    window = Window()
    window.title("AQI指標")
    window.mainloop()

