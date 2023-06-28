import requests
import json
import csv
from datetime import datetime
import os

#下載
youbikeURL = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'

response = requests.get(youbikeURL)
if response.ok:
    print("下載成功")
#找尋無車可借的站點
youbike_list = json.loads(response.text)
print("目前台北youbike2.0,無車可借的站點是:")
i = 0
sbi0_list = []
for site in youbike_list:
    if site['sbi'] == 0:        
        sbi0_list.append(site)
        i += 1
    
print(f"目前無車可借的站點數有{i}")

#存成csv
current = datetime.now()
filename = f"{current.year}-{current.month}-{current.day}-{current.hour}-{current.minute}-{current.second}.csv"
path = os.path.abspath('./')
path_name= os.path.join(path,'data',filename)
heads = list(sbi0_list[0].keys())
print(heads)
with open(path_name,mode='w',encoding='utf-8',newline='') as file:
    writedCsv = csv.DictWriter(file,heads)
    writedCsv.writeheader()
    writedCsv.writerows(sbi0_list)