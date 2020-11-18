from tkinter import *
import urllib3
import certifi
import csv

def main(w):
    gui(w)
    w.mainloop()

def gui(w):
    global scrollbar,mylist
    w.title("收集資料")
    # w.geometry('500x300')
    topFrame = Frame(w,bd=1,relief=GROOVE)
    topFrame.config(bg="#dddddd")
    Button(topFrame, text="空氣品質指標",font=('Verdans',13,'bold'),command=aqi).pack(ipadx=25, ipady=10, side=LEFT, expand=YES)
    Button(topFrame, text="確定2",font=('Verdans',13,'bold')).pack(ipadx=25, ipady=10, side=LEFT, expand=YES)
    Button(topFrame, text="確定3",font=('Verdans',13,'bold')).pack(ipadx=25, ipady=10, side=LEFT, expand=YES)
    topFrame.pack(ipady=20,ipadx=20,pady=20,padx=20)
    bottomFrame = Frame(w,bd=1,relief=GROOVE)
    scrollbar = Scrollbar(bottomFrame)
    scrollbar.pack(side=LEFT)
    mylist = Listbox(bottomFrame,yscrollcommand=scrollbar.set)
    bottomFrame.pack(ipady=20,ipadx=20,pady=20,padx=20,expand=YES,fill=X)

def aqi():
    # 下載AQI
    global rows
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

        with open("空氣品質指標.csv","r",encoding='UTF-8') as file:
            #content = file.read()
            next(file)
            rows=csv.reader(file)
            for item in rows:
                mylist.insert(END,item[0])
            mylist.pack(side=LEFT, fill=BOTH)
            scrollbar.config(command = mylist.yview)
            file.close()

    else:
        print("下載失敗")
        return




if __name__ == "__main__":
    rows = None
    scrollbar = None
    mylist = None
    window = Tk()
    main(window)