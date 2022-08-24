#各鄉鎮市區人口密度.csv的處理

import csv
import pandas as pd
with open('各鄉鎮市區人口密度.csv',mode='r',encoding='utf-8') as file:
    next(file)
    csv_reader = csv.reader(file)
    df = pd.DataFrame(csv_reader,columns=['統計年','區域別','年底人口數','土地面積','人口密度'])

新北市 = df[df['區域別'].str.contains('新北市')]
台北市 = df[df['區域別'].str.contains('臺北市')]
桃園市 = df[df['區域別'].str.contains('桃園市')]

filename = input("請輸入要儲存的excel檔名")

with pd.ExcelWriter(f'{filename}.xlsx', engine='openpyxl') as excelWriter:
    新北市.to_excel(excelWriter,sheet_name='新北市')
    台北市.to_excel(excelWriter,sheet_name='台北市')
    桃園市.to_excel(excelWriter,sheet_name='桃園市')