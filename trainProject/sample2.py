from tkinter import *
import time
import threading

def main():
    repeadingSomeThing()
    w = Tk()
    w.title("我的第一個window")
    w.geometry('500x300')
    Button(w, text="確定1").pack(ipadx=25,ipady=10,side=TOP,expand=YES)
    Button(w, text="確定2").pack(side=TOP,ipadx=25,ipady=10,expand=YES)
    Button(w, text="確定3").pack(side=TOP,ipadx=25,ipady=10,expand=YES)
    w.mainloop()


def repeadingSomeThing():
    t1 = threading.Thread(target=doJob);
    t1.start()

def doJob():
    while True:
        print("Hello! Python!")
        time.sleep(1)

if __name__ == "__main__":
    main()