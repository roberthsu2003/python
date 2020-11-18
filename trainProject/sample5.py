from tkinter import *
import urllib3
import certifi

def main(w):
    gui(w)
    w.mainloop()

def gui(w):
    w.title("收集資料")
    # w.geometry('500x300')
    topFrame = Frame(w,bd=1,relief=GROOVE)
    topFrame.config(bg="#dddddd")
    Button(topFrame, text="空氣品質指標",font=('Verdans',13,'bold'),command=aqi).pack(ipadx=25, ipady=10, side=LEFT, expand=YES)
    Button(topFrame, text="確定2",font=('Verdans',13,'bold')).pack(ipadx=25, ipady=10, side=LEFT, expand=YES)
    Button(topFrame, text="確定3",font=('Verdans',13,'bold')).pack(ipadx=25, ipady=10, side=LEFT, expand=YES)
    topFrame.pack(ipady=20,ipadx=20,pady=20,padx=20)
    bottomFrame = Frame(w,bd=1,relief=GROOVE)
    bottomFrame.pack(ipady=20,ipadx=20,pady=20,padx=20,expand=YES,fill=X)

def aqi():
    # 下載AQI
    print("下載資料")
    CSV_URL = "https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&format=csv"
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
    try:
        response = http.request('GET', CSV_URL)
    except:
        print("主機忙線中")
        return

    if response.status == 200:
        print("下載成功")
        #儲存檔案
        file = open("空氣品質指標.csv","wb")
        file.write(response.data)
        file.close()
        print("存檔成功")
    else:
        print("下載失敗")
        return
    print(response.data)



if __name__ == "__main__":
    window = Tk()
    main(window)