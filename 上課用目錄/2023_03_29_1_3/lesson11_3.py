import requests
import json
import csv

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
heads = list(sbi0_list[0].keys())
with open('youbike2.0無車可借.csv',mode='w',encoding='utf-8',newline='') as file:
    writedCsv = csv.DictWriter(file,heads)
    writedCsv.writeheader()
    writedCsv.writerows(sbi0_list)