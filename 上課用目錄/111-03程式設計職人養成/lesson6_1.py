import tkinter as tk
import requests

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("上市公司每月營業收入彙種表")
        tk.Label(self,text="上市公司每月營業收入彙種表",font=("arial",20)).pack(padx=50, pady=50)
        tk.Button(self,text="下載資料",font=("arial",20),command=self.download).pack(padx=100,pady=50)
    
    def download(self):
        url = "https://mopsfin.twse.com.tw/opendata/t187ap05_L.csv"
        response = requests.get(url,stream=True)
        with open("上市公司每月營業收入彙種表.csv", 'wb') as fd:
            for chunk in response.iter_content(chunk_size=128):
                fd.write(chunk)


def main():
    
   window = Window()
   window.mainloop()

if __name__ == "__main__":
    main()