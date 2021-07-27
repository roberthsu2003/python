import data
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        for county in countyList:
            print(county.siteName, county.name, county.AQI, county.status, county.publishTime)

if __name__ == "__main__":
    countyList = data.aqiData
    window = Window()
    window.mainloop()

