import tkinter as tk
from tkinter import Button
from tkinter.font import Font



class Window(tk.Tk):


    def __init__(self):
        super().__init__()
        self.title("Lesson4_1")
        # 建立系統基本字型
        buttonFontStyle = Font(family="Lucida Grande", size=25)
        Button(self,text='LEFT',width=15,font=buttonFontStyle,pady=5).pack(side=tk.LEFT,padx=(20,10),pady=30)
        Button(self, text='Center',width=15,font=buttonFontStyle,pady=5).pack(side=tk.LEFT,padx=10)
        Button(self, width=15,text='Right',font=buttonFontStyle,pady=5).pack(side=tk.RIGHT,padx=(10,20))



if __name__ == "__main__":
    window = Window()
    window.mainloop()