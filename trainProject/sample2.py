from tkinter import *
import time
import threading
import lineTool
import requests


def main():
    repeadingSomeThing()
    w = Tk()
    w.title("我的第一個window")
    w.geometry('500x300')
    Button(w, text="確定1",command=lineMe).pack(ipadx=25,ipady=10,side=TOP,expand=YES)
    Button(w, text="確定2",command=lineYou).pack(side=TOP,ipadx=25,ipady=10,expand=YES)
    Button(w, text="確定3").pack(side=TOP,ipadx=25,ipady=10,expand=YES)
    w.mainloop()

def lineMe():
    token = ""
    msg = "Python 語言整合通訊軟體,恭喜您"
    response = lineTool.lineNotify(token, msg)
    if response == 200:
        print("傳送成功")
    else:
        print("傳送失敗")

def lineYou():
    token = ""
    msg = "熊來了!"
    picURI = "bear.jpeg"
    status=sendLineNotify(token, msg, picURI)
    if status == 200:
        print("success")
    else:
        print("fauil")

def sendLineNotify(token, msg, picURI):
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization":"Bearer " + token}
    payload = {"message": msg}
    files = {"imageFile":open(picURI, 'rb')}
    r = requests.post(url, headers=headers, params = payload, files = files)
    return r.status_code

def repeadingSomeThing():
    t1 = threading.Thread(target=doJob);
    t1.start()

def doJob():
    while True:
        print("Hello! Python!")
        time.sleep(1)

if __name__ == "__main__":
    main()


