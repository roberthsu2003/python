from tkinter import *

def main():
    w = Tk()
    w.title("我的第一個window")
    w.geometry('300x300')
    b = Button(w, text="確定",command=buttonCallBack)
    b.pack()
    w.mainloop()


def buttonCallBack():
    print("Hello! Python!")

if __name__ == "__main__":
    main()