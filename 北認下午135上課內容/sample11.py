#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:50:09 2020

@author: roberthsu2003
"""
from tkinter import *

if __name__ == '__main__':
    window = Tk()
    window.title("BMI應用程式")
    window.geometry("300x200")
    mainFrame = Frame(window)
    
    subFrame = Frame(mainFrame, relief=GROOVE, borderwidth=2)
    titleLabel = Label(mainFrame,text="BMI Control").place(relx=0.05, rely=0.025, anchor=NW)
    button = Button(subFrame, text="BMI計算").pack(expand=YES, fill=BOTH, padx=40, pady=25)
    subFrame.pack(expand=YES, fill=BOTH, padx=5, pady=20)
    
    mainFrame.pack(expand=YES, fill=BOTH)
    window.mainloop()

