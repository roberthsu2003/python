from tkinter import Tk,Label,BOTH


if __name__ == '__main__':
    window = Tk()
    window.title("這是我的第一個視窗軟體")
    window.geometry('600x300+200+100')
    lable = Label(window, text="Hello! Tkinter")
    lable.pack(padx=100,pady=50,expand=True)
    window.mainloop()