from tkinter import *

def main(w):
    gui(w)
    w.mainloop()

def gui(w):
    w.title("收集資料")
    # w.geometry('500x300')
    topFrame = Frame(w)
    Button(topFrame, text="確定1").pack(ipadx=25, ipady=10, side=LEFT, expand=YES)
    Button(topFrame, text="確定2").pack(ipadx=25, ipady=10, side=LEFT, expand=YES)
    Button(topFrame, text="確定3").pack(ipadx=25, ipady=10, side=LEFT, expand=YES)
    topFrame.pack(ipady=20,ipadx=20)

    bottomFrame = Frame(w)
    bottomFrame.pack(ipady=20, ipadx=20)


if __name__ == "__main__":
    window = Tk()
    main(window)