import tkinter as tk
from tkinter import Button,Frame
from tkinter.font import Font



class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lesson4_2")
        self.geometry("400x200")
        #self["bg"] = 'blue'
        #self.configure(bg="blue")
        self.config(bg="blue")
        # 建立系統基本字型
        buttonFontStyle = Font(size=25)
        frame = Frame(self,bg='red')
        Button(frame,text='LEFT',font=buttonFontStyle,pady=5).pack(side=tk.LEFT,expand=True,fill='both')
        Button(frame, text='Center',font=buttonFontStyle,pady=5).pack(side=tk.LEFT,expand=True,fill='both')
        Button(frame, text='Right',font=buttonFontStyle,pady=5).pack(side=tk.RIGHT,expand=True,fill='both')
        frame.pack(expand=True,fill='both')



if __name__ == "__main__":
    window = Window()
    window.mainloop()