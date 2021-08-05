from datasource.source import getData
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("股票成交價及時查詢提醒系統")
        mainFrame = tk.Frame(self, relief="groove",borderwidth=2)
        titleFrame = tk.Frame(mainFrame)
        tk.Label(titleFrame, text="股票成交價及時查詢系統",font=("Arial",20,'bold'),fg='#555555').pack(padx=10)
        titleFrame.pack()
        tk.Label(mainFrame, text="----------------------------").pack()
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

        tk.Label(self.listFrame, text='最高成交價:', font=("Arial", 14)).grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)
        self.highLabel = tk.Label(self.listFrame, text="", font=("Arial", 14))
        self.highLabel.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)

        tk.Label(self.listFrame, text='最低成交價:', font=("Arial", 14)).grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)
        self.lowLabel = tk.Label(self.listFrame, text="", font=("Arial", 14))
        self.lowLabel.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)

        tk.Label(self.listFrame, text='開盤價:', font=("Arial", 14)).grid(row=4, column=0, sticky=tk.E, padx=10, pady=10)
        self.openLabel = tk.Label(self.listFrame, text="", font=("Arial", 14))
        self.openLabel.grid(row=4, column=1, sticky=tk.W, padx=10, pady=10)

        self.listFrame.pack()

        mainFrame.pack(pady=30,ipadx=20,ipady=20)

    def getStockID(self):
        inputID=self.stockIDEngry.get()
        stockInfo=getData(inputID)
        if not stockInfo.error:
            self.companyLabel.configure(text=stockInfo.name)
            self.closeLabel.configure(text=f"{stockInfo.close}元")
            self.highLabel.configure(text=f"{stockInfo.high}元")
            self.lowLabel.configure(text=f"{stockInfo.low}元")
            self.openLabel.configure(text=f"{stockInfo.open}元")
        else:
            print(stockInfo.error)



def closeWindow():
    print("視窗關閉")
    window.destroy()


if __name__ == "__main__":
    window = Window()
    window.protocol("WM_DELETE_WINDOW",closeWindow)
    window.resizable(width=0,height=0)
    window.mainloop()

    """
    stockID = input("請輸入股票代號:")
    data = getData(stockID)
    if not data.error:
        # 沒有錯誤
        print(f"股票代號:{data.id}")
        print(f"股票名稱:{data.name}")
        print(f"收盤價:{data.close}")
    else:
        print("資類取得錯誤", data.error)
    
    """
