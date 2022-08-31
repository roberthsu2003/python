import requests
import csv
import pandas as pd
from datetime import datetime
from tkinter import filedialog

def loadData():
    url = 'https://od.cdc.gov.tw/eic/covid19/covid19_global_cases_and_deaths.csv'
    response = requests.get(url)
    if response.ok:
        print("下載成功")

    response.encoding = "utf-8"
    return response.text.splitlines()

def get_df(csv_text):
    csv_reader = csv.reader(csv_text)
    df = pd.DataFrame(csv_reader)
    df = df.iloc[1:]
    df.columns = ['國家', 'country', '確診', '死亡']
    df.set_index('國家', inplace=True)
    df['確診'] = df['確診'].str.replace(",", "")
    df['死亡'] = df['死亡'].str.replace(",", "")
    df['確診'] = df['確診'].astype(int)
    df['死亡'] = df['死亡'].astype(int)
    df["死亡比例"] = df["死亡"] / df["確診"] * 100
    return df

def get_countries():
    csv_text = loadData()
    df = get_df(csv_text)
    return df.index

def convert_excel(countrylist):
    csv_text = loadData()
    df = get_df(csv_text)
    selected_df = df.loc[countrylist]
    file_path = filedialog.askdirectory()
    print(file_path)

    now = datetime.now()
    filename = '_'.join(countrylist)+f"_{now.year}{now.month}{now.day}"+'.xlsx'
    with pd.ExcelWriter(file_path+"/"+filename) as writer:
        selected_df.to_excel(writer, sheet_name='_'.join(countrylist))