#!/usr/bin/env python3.7
'''
讀取txt文件檔案
'''
from tkinter import *

def display_message():
    file = open('news.txt', 'r', encoding='UTF-8')
    content = file.read()
    print(content)
    file.close()

if __name__ == '__main__':
    window = Tk()
    window.title("讀取TxT應用程式")
    window.geometry("300x200")

    mainFrame = Frame(window)

    subFrame = Frame(mainFrame, relief=GROOVE, borderwidth=2)

    subFrame.pack(expand=YES, fill=BOTH, padx=5, pady=20)

    display_btn = Button(subFrame,text='顯示文字',command=display_message)
    display_btn.pack(expand=YES,fill=BOTH,padx=30,pady=30)

    mainFrame.pack(expand=YES, fill=BOTH)
    window.mainloop()