#!/usr/bin/env python3.7
'''
讀取讀取氣象觀測資料
'''
from tkinter import *
import urllib3
import certifi
import json

def display_message():
    print("讀取氣象觀測資料")

if __name__ == '__main__':
    window = Tk()
    window.title("讀取氣象觀測資料應用程式")
    window.geometry("300x200")

    mainFrame = Frame(window)

    subFrame = Frame(mainFrame, relief=GROOVE, borderwidth=2)

    subFrame.pack(expand=YES, fill=BOTH, padx=5, pady=20)

    display_btn = Button(subFrame,text='氣象觀測資料',command=display_message)
    display_btn.pack(expand=YES,fill=BOTH,padx=30,pady=30)

    mainFrame.pack(expand=YES, fill=BOTH)
    window.mainloop()