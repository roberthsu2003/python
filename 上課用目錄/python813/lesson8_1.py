#台北市youbike2.0及時資料
#https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
import requests
youbike_taipei = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
response = requests.get(youbike_taipei)
if response.status_code == 200:
    print("下載成功")
    print(response.text)