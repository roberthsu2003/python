from datasource.source import getData
from datasource.source import driver
import tkinter as tk
from tkinter import messagebox
from threading import Timer

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.t = None #先設None值,為了使用者如果沒有搜尋股票，直接關閉
        self.currentStockID = ""
        self.title("股票成交價及時查詢提醒系統")
        mainFrame = tk.Frame(self, relief="groove",borderwidth=2)
        titleFrame = tk.Frame(mainFrame)
        tk.Label(titleFrame, text="股票成交價及時查詢系統",font=("Arial",20,'bold'),fg='#555555').pack(padx=10)
        titleFrame.pack(pady=30)
        # -------------建立inputFrame---------------
        self.inputFrame = tk.Frame(mainFrame,width=50)
        tk.Label(self.inputFrame, text="輸入欲查詢的股票號碼:",font=("Arial",13)).grid(row=0,column=0,sticky=tk.E)
        self.stockIDEngry = tk.Entry(self.inputFrame,textvariable=tk.StringVar(),bd=5)
        self.stockIDEngry.grid(row=0,column=1, sticky=tk.E)
        submitButton = tk.Button(self.inputFrame, font=("Arial",15),text="搜尋",command=self.getStockID)
        submitButton.grid(row=0,column=2,sticky=tk.E)
        self.inputFrame.pack()

        # --------------建立顯示畫面 -----------
        self.listFrame = tk.Frame(mainFrame)
        tk.Label(self.listFrame,text='公司名',font=("Arial",14)).grid(row=0,column=0,sticky=tk.E,padx=10,pady=10)
        self.companyLabel = tk.Label(self.listFrame,text="",font=("Arial",14))
        self.companyLabel.grid(row=0,column=1, sticky=tk.W,padx=10,pady=10)


        tk.Label(self.listFrame, text='目前成交價:', font=("Arial", 14)).grid(row=1, column=0, sticky=tk.E, padx=10, pady=10)
        self.closeLabel = tk.Label(self.listFrame, text="", font=("Arial", 14))
        self.closeLabel.grid(row=1, column=1, sticky=tk.W, padx=10, pady=10)

        tk.Label(self.listFrame, text='目前狀況:', font=("Arial", 14)).grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)
        self.diffLabel = tk.Label(self.listFrame, text="", font=("Arial", 14))
        self.diffLabel.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)

        tk.Label(self.listFrame, text='漲跌價差(百分比):', font=("Arial", 14)).grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)
        self.percentLabel = tk.Label(self.listFrame, text="", font=("Arial", 14))
        self.percentLabel.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)

        tk.Label(self.listFrame, text='當盤_成交量:', font=("Arial", 14)).grid(row=4, column=0, sticky=tk.E, padx=10,
                                                                             pady=10)
        self.tv_odd_Label = tk.Label(self.listFrame, text="", font=("Arial", 14))
        self.tv_odd_Label.grid(row=4, column=1, sticky=tk.W, padx=10, pady=10)

        tk.Label(self.listFrame, text='累積_成交量:', font=("Arial", 14)).grid(row=5, column=0, sticky=tk.E, padx=10,
                                                                          pady=10)
        self.v_odd_Label = tk.Label(self.listFrame, text="", font=("Arial", 14))
        self.v_odd_Label.grid(row=5, column=1, sticky=tk.W, padx=10, pady=10)

        tk.Label(self.listFrame, text='最高成交價:', font=("Arial", 14)).grid(row=6, column=0, sticky=tk.E, padx=10, pady=10)
        self.highLabel = tk.Label(self.listFrame, text="", font=("Arial", 14))
        self.highLabel.grid(row=6, column=1, sticky=tk.W, padx=10, pady=10)

        tk.Label(self.listFrame, text='最低成交價:', font=("Arial", 14)).grid(row=7, column=0, sticky=tk.E, padx=10, pady=10)
        self.lowLabel = tk.Label(self.listFrame, text="", font=("Arial", 14))
        self.lowLabel.grid(row=7, column=1, sticky=tk.W, padx=10, pady=10)

        tk.Label(self.listFrame, text='開盤價:', font=("Arial", 14)).grid(row=8, column=0, sticky=tk.E, padx=10, pady=10)
        self.openLabel = tk.Label(self.listFrame, text="", font=("Arial", 14))
        self.openLabel.grid(row=8, column=1, sticky=tk.W, padx=10, pady=10)

        self.listFrame.pack()

        mainFrame.pack(pady=30,padx=30,ipadx=30,ipady=30)

    def getStockID(self):
        inputID=self.stockIDEngry.get()
        # 檢查目前顯示的股票id是否和正在更新的一樣,如果不一樣，停止目前的更新，建立新的更新，
        if inputID != self.currentStockID: #檢查現在輸入的股票id和先前更新的是否不一樣，如果不一樣
            if self.t and self.t.is_alive(): #檢查是否有t(t不是None)和是否有在執行
                self.t.cancel() #關閉執行緒
            self.currentStockID = inputID
        elif self.currentStockID == "": #如果第一次是空字串，則直接return
            print("不可以為空字串")
            messagebox.showerror("錯誤","輸入欄位不可以為空字串")
            return

        stockInfo=getData(self.currentStockID)
        if not stockInfo.error:
            self.companyLabel.configure(text=stockInfo.name)
            self.closeLabel.configure(text=f"{stockInfo.close}元")
            self.diffLabel.configure(text=f"{stockInfo.diff}元")
            self.percentLabel.configure(text=stockInfo.percent)
            self.tv_odd_Label.configure(text=f"{stockInfo.tv_odd}張")
            self.v_odd_Label.configure(text=f"{stockInfo.v_odd}張")
            self.highLabel.configure(text=f"{stockInfo.high}元")
            self.lowLabel.configure(text=f"{stockInfo.low}元")
            self.openLabel.configure(text=f"{stockInfo.open}元")
        else:
            #出錯了
            print("出錯了")
            print(stockInfo.error)
            messagebox.showerror("錯誤", stockInfo.error)
        self.repeatCheck()

    def repeatCheck(self):
        print("更新")
        self.t = Timer(20,self.getStockID)
        self.t.start()



def closeWindow():
    # 應用程式關閉,有t就關閉
    if window.t and window.t.is_alive():
        print("關閉更新")
        window.t.cancel()

    window.destroy()
    if not (driver is None):
        print("關閉webdriver")
        driver.close()
        driver.quit()
    print("視窗關閉")


if __name__ == "__main__":
    window = Window()
    window.protocol("WM_DELETE_WINDOW",closeWindow)
    window.resizable(width=0,height=0)
    window.mainloop()
