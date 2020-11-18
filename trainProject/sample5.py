from tkinter import *

def main(w):
    gui(w)
    w.mainloop()

def gui(w):
    w.title("收集資料")
    # w.geometry('500x300')
    topFrame = Frame(w,bd=1,relief=GROOVE)
    Button(topFrame, text="確定1").pack(ipadx=25, ipady=10, side=LEFT, expand=YES)
    Button(topFrame, text="確定2").pack(ipadx=25, ipady=10, side=LEFT, expand=YES)
    Button(topFrame, text="確定3").pack(ipadx=25, ipady=10, side=LEFT, expand=YES)
    topFrame.pack(ipady=20,ipadx=20,pady=20,padx=20)

    bottomFrame = Frame(w,bd=1,relief=GROOVE)
    bottomFrame.pack(ipady=20,ipadx=20,pady=20,padx=20,expand=YES,fill=X)


if __name__ == "__main__":
    window = Tk()
    main(window)