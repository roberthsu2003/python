import tkinter as tk
import tools
import datasource
import csv

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("這是我的第一個視窗")        
        btn1 = tk.Button(self,text="下載空氣品質\n儲存csv",padx=50,pady=25,font=('Arial',20,'bold'),command=self.btn1_click)
        btn1.pack(padx=100,pady=20)

        btn2 = tk.Button(self,text="下載csv\n儲存excel",padx=50,pady=25,font=('Arial',20,'bold'),command=self.btn2_click)
        btn2.pack(padx=100,pady=20)

    def btn1_click(self):
        dataList = datasource.download_air_data()
        with open("6都空氣品質.csv",mode="w",encoding="utf-8",newline="") as file:
            keys = list(dataList[0].keys())
            dictWriter = csv.DictWriter(file,fieldnames=keys)
            dictWriter.writeheader()
            for item in dataList:
                dictWriter.writerow(item)          
            print("儲存'6都空氣品質.csv'成功")

    def btn2_click(self):
        datasource.download_github_csv()

        
        

def main():
    #chinese和english區域變數
    window = Window()   
    window.mainloop()

if __name__ == "__main__":
    main()
    
