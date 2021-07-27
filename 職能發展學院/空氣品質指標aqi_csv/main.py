import data
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        '''
        for county in countyList:
            print(county.siteName, county.name, county.AQI, county.status, county.publishTime)
        '''
        titleFrame = tk.Frame(self,bg="#9CEFB5",borderwidth = 3,relief=tk.GROOVE)
        tk.Label(titleFrame,text="全省空氣品質指標_AQI",font=("Courier", 25, "italic")).pack()
        titleFrame.pack(padx=20,pady=20)


if __name__ == "__main__":
    countyList = data.aqiData
    window = Window()
    window.mainloop()

