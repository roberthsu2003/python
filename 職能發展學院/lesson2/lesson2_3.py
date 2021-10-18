import tkinter as tk

window=tk.Tk()
window.title("Hello Tkinter")
#window.geometry("500x100")
label = tk.Label(window,text="Hello World",bg='yellow', fg='#263238', font=('Arial', 20),padx=100,pady=50)
label.pack(padx=100,pady=50)
window.mainloop()