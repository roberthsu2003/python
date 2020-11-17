from tkinter import *
import time
import threading
import lineTool


def main():
    repeadingSomeThing()
    w = Tk()
    w.title("我的第一個window")
    w.geometry('500x300')
    Button(w, text="確定1",command=lineMe).pack(ipadx=25,ipady=10,side=TOP,expand=YES)
    Button(w, text="確定2").pack(side=TOP,ipadx=25,ipady=10,expand=YES)
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

def repeadingSomeThing():
    t1 = threading.Thread(target=doJob);
    t1.start()

def doJob():
    while True:
        print("Hello! Python!")
        time.sleep(1)

if __name__ == "__main__":
    main()


