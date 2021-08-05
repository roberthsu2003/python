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
        mainFrame.pack(pady=30,ipadx=20,ipady=20)


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
