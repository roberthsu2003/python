#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:50:09 2020

@author: roberthsu2003
"""
from tkinter import *

def calculate():
    print("使用者按下按鈕")

if __name__ == '__main__':
    window = Tk()
    window.title("BMI應用程式")
    window.geometry("300x200")

    mainFrame = Frame(window)

    subFrame = Frame(mainFrame, relief=GROOVE, borderwidth=2)

    height_frame = Frame(subFrame)
    height_label = Label(height_frame,text='身高(cm)')
    height_label.pack(side=LEFT)
    height_entry = Entry(height_frame)
    height_entry.pack(side=LEFT)
    height_frame.pack(side=TOP)

    weight_frame = Frame(subFrame)
    weight_label = Label(weight_frame, text='體重(kg)')
    weight_label.pack(side=LEFT)
    weight_entry = Entry(weight_frame)
    weight_entry.pack(side=LEFT)
    weight_frame.pack(side=TOP)
    subFrame.pack(expand=YES, fill=BOTH, padx=5, pady=20)

    result_label = Label(subFrame,text="建議")
    result_label.pack();

    calculate_btn = Button(subFrame,text='馬上計算',command=calculate)
    calculate_btn.pack()

    mainFrame.pack(expand=YES, fill=BOTH)
    window.mainloop()

