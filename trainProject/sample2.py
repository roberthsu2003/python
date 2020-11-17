from tkinter import *

def main():
    w = Tk()
    w.title("我的第一個window")
    w.geometry('500x300')
    Button(w, text="確定1",command=buttonCallBack).pack(ipadx=25,ipady=10,side=TOP,expand=YES)
    Button(w, text="確定2", command=buttonCallBack).pack(side=TOP,ipadx=25,ipady=10,expand=YES)
    Button(w, text="確定3", command=buttonCallBack).pack(side=TOP,ipadx=25,ipady=10,expand=YES)


    w.mainloop()


def buttonCallBack():
    print("Hello! Python!")

if __name__ == "__main__":
    main()