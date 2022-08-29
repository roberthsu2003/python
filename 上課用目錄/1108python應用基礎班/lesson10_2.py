import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        fontstyle = tkFont.Font(family="Lucida Grande", size=25)
        mainFrame = tk.Frame(self,borderwidth=1,relief=tk.GROOVE,padx=10,pady=10)
        tk.Label(mainFrame,text="全球 covid19 最新統計",font=fontstyle).grid(column=0, row=0)
        countries_listbox = tk.Listbox(mainFrame)
        countries_listbox.insert(tk.END, 'apple','banana','orange','lemon','tomato')
        countries_listbox.grid(column=0,row=1)
        mainFrame.grid(column=0,row=0,padx=20,pady=20)

def main():
    window = Window()
    window.title("全球_covid19_最新統計")
    window.mainloop()

if __name__ == "__main__":
    main()
