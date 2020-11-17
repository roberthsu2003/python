from tkinter import Tk,Button,Label

def main():
    w = Tk()
    w.title("我的第一個window")
    w.geometry('300x300')
    b = Button(w, text="OK")
    b.pack()
    w.mainloop()
    pass

if __name__ == "__main__":
    main()