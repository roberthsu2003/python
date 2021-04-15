import tkinter as tk
import datasource

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


if __name__ == "__main__":
    window = Window()
    window.mainloop()