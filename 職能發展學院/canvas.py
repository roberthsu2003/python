from tkinter import Tk,Canvas
window = Tk()
window.title("Canvas")
canvas = Canvas(window, width=400, height=400, bg='#cccccc')
canvas.create_oval(10,10,100,100,fill='white')
canvas.pack()
window.mainloop()