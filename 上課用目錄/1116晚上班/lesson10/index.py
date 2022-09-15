from data import Person,Student
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("這是我的視窗程式")
        tk.Button(self,text="請按我",command=self.userClick).pack(padx=100,pady=100)
    
    def userClick(self):
        s1 = Student(n="jone",chinese=85)
        s2 = Student(n="peter",age=21,english=92)
        s1.description()
        print("總分",s1.sum)
        print("=============")
        s2.description()
        print("總分",s2.sum)

               

def main():
    window = Window()
    window.mainloop()


if __name__ == "__main__":
    main()