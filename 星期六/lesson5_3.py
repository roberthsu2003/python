import requests

urlpath = 'https://data.tainan.gov.tw/dataset/da3520b0-f1a8-475d-8932-32e225c044d8/resource/66b11687-9b28-4366-b5c8-412a68b0cc9f/download/opendata.json'
response = requests.get(urlpath)
if response.status_code == 200:
    print("下載成功")
    print(f"下載的編碼{response.encoding}")
    print(f"下載的文字{response.text}")
    downloadData = response.json()
print(downloadData.__class__)
for item in downloadData:
    print(f"車隊名稱:{item['車隊名稱']},公司地址:{item['公司地址']},聯絡電話:{item['聯絡電話']}")
    print("=============")
