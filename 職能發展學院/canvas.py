from tkinter import Tk,Canvas,Frame,Label
import tkinter as tk
window = Tk()
window.title("Canvas")
canvas = Canvas(window, width=400, height=400, bg='#cccccc')
canvas.create_oval(10,10,100,100,fill='white')
canvas.create_line(105,10,200,100, fill='red')
canvas.create_rectangle(205,10,300,105, outline='white', fill='#777777')

xy = 10, 105, 100, 200
canvas.create_arc(xy,start=0, extent=270, fill='#777777')

frm = Frame(canvas,relief=tk.GROOVE,borderwidth=2)
Label(frm, text="嵌入 Frame/Label").pack()
canvas.create_window(280, 280, window=frm)

canvas.pack()
window.mainloop()