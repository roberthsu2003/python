import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Enter New Password")

        tk.Label(self,text="Old Password:",font=('arial',20)).grid(row=0,column=0,sticky=tk.E,pady=20) 
        tk.Label(self,text="New Password:",font=('arial',20)).grid(row=1,column=0,sticky=tk.E,pady=20)
        tk.Label(self,text="Enter New Password Again:",font=('arial',20)).grid(row=2,column=0,sticky=tk.W,pady=20)

        tk.Entry(self,width=20,show="*",font=('arial',20)) .grid(row=0, column=1,padx=10)
        tk.Entry(self,width=20,show="*",font=('arial',20)) .grid(row=1, column=1,padx=10) 
        tk.Entry(self,width=20,show="*",font=('arial',20)) .grid(row=2, column=1,padx=10)     
       
        


def main():
    window = Window()    
    window.mainloop()

if __name__ == '__main__':
    main()