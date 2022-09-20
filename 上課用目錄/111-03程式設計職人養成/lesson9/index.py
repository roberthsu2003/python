
import tkinter as tk
import requests

class Window(tk.Tk):
    def __init__(self,codes):
        super().__init__()
        self.codes = codes
        self.title("各縣市4天天氣預測")
        print(self.codes)
        tk.Label(self, text="各縣市4天天氣預測", font=("arial",20)).pack(padx=100, pady=50)

        buttonFrame = tk.Frame(self)        
        for index,cities in enumerate(self.codes.items()):            
            cname,ename= cities
            btn = tk.Button(buttonFrame,text=f"{cname}\n{ename}",padx=20,pady=10,width=5)
            btn.grid(column=index % 4,row=index // 4)
            btn.bind('<Button>',self.btnClick)
        buttonFrame.pack()

        
        self.chage_content_frame = tk.Frame(self) #會改變內容的frame       
        #這裏的內容必需使用者按下按鈕後才面產生
        self.chage_content_frame.pack()



    def btnClick(self,event):
        btn=event.widget
        btn_text = btn["text"]
        nameList = btn_text.split()
        cname = nameList[0]
        ename = nameList[1]
        if hasattr(self, 'displayFrame'):
            self.displayFrame.destroy()
        self.displayFrame = DisplayFrame(self.chage_content_frame,cname=cname,ename=ename)
        self.displayFrame.pack()
        

class DisplayFrame(tk.LabelFrame):
    def __init__(self,master,cname,ename):
        super().__init__(master)
        self.cname = cname
        self.ename = ename
        self.forecast = DisplayFrame.get_forecast(ename=self.ename)
        print(len(self.forecast))        
        leftFrame = tk.Frame(self,width=150,height=150,background='#333333')
        leftFrame.pack(side=tk.LEFT)
        centerFrame = tk.Frame(self,width=150,height=150,background='#666666')
        centerFrame.pack(side=tk.LEFT)
        rightFrame = tk.Frame(self,width=150,height=150,background='#999999')
        rightFrame.pack(side=tk.LEFT)

    @staticmethod
    def get_forecast(ename):        
        url = "https://api.openweathermap.org/data/2.5/forecast?q="+ename+",tw&APPID=29c4f184354b9889e87f7b494ac86aed&lang=zh_tw&units=metric"
        response = requests.request("GET",url)
        if response.ok == True:
            print("下載成功")    
            all_data = response.json()
        list_data = all_data['list']

        county_forcase = []
        for item in list_data:
            county_forcase.append([item['dt_txt'],item['main']['temp'],item['weather'][0]['description'],item['main']['humidity']])
        
        return county_forcase



def main():
    tw_county_names = {"台北":"Taipei",
                   "台中":"Taichung",
                   "基隆":"Keelung",
                   "台南":"Tainan",
                   "高雄":"Kaohsiung",
                   "新北":"New Taipei",
                   "宜蘭":"Yilan",
                   "桃園":"Taoyuan",
                   "嘉義":"Chiayi",
                   "新竹":"Hsinchu",
                   "苗栗":"Miaoli",
                   "南投":"Nantou",
                   "彰化":"Changhua",
                   "雲林":"Yunlin",
                   "屏東":"Pingtung",
                   "花蓮":"Hualien",
                   "台東":"Taitung",
                   "金門":"Kinmen",
                   "澎湖":"Penghu",
                   "連江":"Lienchiang"
                   }
    window = Window(codes=tw_county_names)
    window.mainloop()

if __name__ == "__main__":
    main()