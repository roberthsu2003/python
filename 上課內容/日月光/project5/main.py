import tkinter as tk
import datasource
import linebot

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Line Bot")
        font = ('arial',20)
        lineButton = tk.Button(self,text='send Line Message',padx=30, pady=30,command=self.sendLineMessage,font=font)
        lineButton.pack(padx=20,pady=20)

    def sendLineMessage(self):
        print("sendLineMessage")
        imageURI = datasource.getMathGraphic()
        status_code=linebot.sendLineNotify("5年9班的數學成績",imageURI)
        if status_code == 200:
            print("傳送成功")
        else:
            print("傳送失敗")



if __name__ == "__main__":
    window = Window()
    window.mainloop()