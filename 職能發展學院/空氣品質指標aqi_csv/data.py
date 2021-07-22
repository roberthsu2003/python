#data.py就是自訂的module
#空氣品質AQI的csv檔,線上下載
import requests

downloadURL = "https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=csv"
response = requests.get(downloadURL,stream=True)
with open('aqi.csv','wb') as fileObject:
    #寫入檔案
    for chunk in response.iter_content(chunk_size=128):
        fileObject.write(chunk)
print("下載完成")
