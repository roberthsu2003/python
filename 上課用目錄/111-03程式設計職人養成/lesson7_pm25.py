import tkinter as tk
import requests
from io import StringIO
import csv

class Window(tk.Tk):
    def __init__(self,county):
        super().__init__()
        self.county  = county
        print(self.county)

def main():
    county = get_county()
    window = Window(county)    
    window.mainloop()

def get_county():
    url = "https://data.epa.gov.tw/api/v2/stat_p_115?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate desc&format=CSV"
    response = requests.get(url)
    response.encoding = "utf-8"
    with StringIO(response.text) as like_file:
        csv_reader = csv.reader(like_file)
        csv_list = list(csv_reader)
    county_set = set()
    for item in csv_list:
        county_set.add(item[1])
    county_set.remove("item2")
    county_set.remove("總計")
    county = list(county_set)
    return county

if __name__ == "__main__":
    main()