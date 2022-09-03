#台北市youbike2.0及時資料
#https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
import requests
import json
import csv
youbike_taipei = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
response = requests.get(youbike_taipei)
if response.status_code == 200:
    print("下載成功")
    json_txt = response.text
    data = json.loads(json_txt)
    two_list_data = []
    for item in data:
        newList = [item['mday'],item['sarea'],item['sna'], item['ar'], item['tot'], item['sbi'], item['bemp']]
        two_list_data.append(newList)
    with open('台北市youbike2.csv',mode='w',encoding='utf-8',newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["資料更新時間","行政區","站點名稱","地址","總車輛數","可借","可還"])
        csv_writer.writerows(two_list_data)
    print("存檔成功")
