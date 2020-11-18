from tkinter import *

def main():

    w = Tk()
    w.title("我的第一個window")
    w.geometry('500x300')
    Button(w, text="確定1").pack(ipadx=25,ipady=10,side=LEFT,expand=YES)
    Button(w, text="確定2").pack(ipadx=25,ipady=10,side=LEFT,expand=YES)
    Button(w, text="確定3").pack(ipadx=25,ipady=10,side=LEFT,expand=YES)
    w.mainloop()
if __name__ == "__main__":
    main()