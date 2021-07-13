import requests
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        res = requests.get('https://flask-robert.herokuapp.com/youbike')
        jsonObj = res.json()
        areas = jsonObj['areas']
        for area in areas:
            print(area)

if __name__ == "__main__":
    window = Window()
    window.mainloop()
