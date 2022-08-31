import tkinter as tk
import tkinter.font as tkFont
import datasource as ds

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        fontstyle = tkFont.Font(family="Lucida Grande", size=25)
        #mainFrame
        mainFrame = tk.Frame(self,borderwidth=1,relief=tk.GROOVE,padx=10,pady=10)
        tk.Label(mainFrame,text="全球 covid19 最新統計",font=fontstyle).grid(column=0, row=0,columnspan=2)
        #left_sub_frame
        left_sub_frame = tk.Frame(mainFrame)
        countries_listbox = tk.Listbox(left_sub_frame,selectmode=tk.MULTIPLE)
        country_names = ds.get_countries()
        for country in country_names:
            countries_listbox.insert(tk.END, country)
        countries_listbox.pack(side="left")
        scroll_bar = tk.Scrollbar(left_sub_frame)
        scroll_bar.pack(side="left",fill = tk.BOTH)
        countries_listbox.configure(yscrollcommand = scroll_bar.set)
        scroll_bar.config(command = countries_listbox.yview)
        left_sub_frame.grid(column=0,row=1)

        button = tk.Button(mainFrame,text="轉換為Excel檔 >>")
        button.grid(column=1,row=1)
        mainFrame.grid(column=0,row=0,padx=20,pady=20)


def main():
    window = Window()
    window.title("全球_covid19_最新統計")
    window.mainloop()

if __name__ == "__main__":
    main()
