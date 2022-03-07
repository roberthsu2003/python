import requests

url = 'https://data.tainan.gov.tw/dataset/da3520b0-f1a8-475d-8932-32e225c044d8/resource/66b11687-9b28-4366-b5c8-412a68b0cc9f/download/opendata.json'
r = requests.get(url)
if r.status_code == 200:
    allData = r.json()

carNames = []
for dict_item in allData:
    for key,value in dict_item.items():
        if key == '車隊名稱':
            carNames.append(value)

print(carNames)