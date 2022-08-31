import tkinter as tk
import tkinter.font as tkFont
import datasource as ds
import tkinter.messagebox as messagebox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        fontstyle = tkFont.Font(family="Lucida Grande", size=25)
        #mainFrame
        mainFrame = tk.Frame(self,borderwidth=1,relief=tk.GROOVE,padx=10,pady=10)
        tk.Label(mainFrame,text="全球 covid19 最新統計",font=fontstyle).grid(column=0, row=0,columnspan=2,pady=(0,20))
        #left_sub_frame
        left_sub_frame = tk.Frame(mainFrame)
        self.countries_listbox = tk.Listbox(left_sub_frame,selectmode=tk.MULTIPLE)
        country_names = ds.get_countries()
        for country in country_names:
            self.countries_listbox.insert(tk.END, country)
        self.countries_listbox.pack(side="left")
        scroll_bar = tk.Scrollbar(left_sub_frame)
        scroll_bar.pack(side="left",fill = tk.BOTH,padx=(0,10))
        self.countries_listbox.configure(yscrollcommand = scroll_bar.set)
        scroll_bar.config(command = self.countries_listbox.yview)
        left_sub_frame.grid(column=0,row=1)

        button = tk.Button(mainFrame,text="轉換為Excel檔 >>",command=self.button_click)
        button.grid(column=1,row=1,sticky='N')
        mainFrame.grid(column=0,row=0,padx=20,pady=20)

    def button_click(self):
        if len(self.countries_listbox.curselection()) == 0:
            messagebox.showwarning(title="警告",message="最少必需選取一個國家")
        else:
            country_name = []
            for i in self.countries_listbox.curselection():
                print(self.countries_listbox.get(i))
                country_name.append(self.countries_listbox.get(i))

            ds.convert_excel(country_name)
            messagebox.showinfo(title="提示", message="轉檔完成")


def main():
    window = Window()
    window.title("全球_covid19_最新統計")
    window.mainloop()

if __name__ == "__main__":
    main()
