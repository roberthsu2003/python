import requests
import json
from datetime import datetime
import csv

def download_json():
    url = "http://api.openweathermap.org/data/2.5/group?id=1668341,1668399,1670481&units=metric&appid=29c4f184354b9889e87f7b494ac86aed"
    res = requests.get(url)

    if res.ok:
        print("下載成功")
        return res.text
    else:
        print("下載失敗")


def main():
    jsonText = download_json()

    data = json.loads(jsonText)

    datalist = data["list"]
    weathers = []
    for item in datalist:
        city = [item['dt'],item['name'],item['coord']['lat'],item['coord']['lon'],item['main']['temp']]
        weathers.append(city)

    for city in weathers:
        timestamp = city[0]
        dt_object = datetime.fromtimestamp(timestamp)
        city[0] = dt_object.isoformat()

    weathers.insert(0,['日期','城市','緯度','經度','攝氏溫度'])

    with open("weathers.csv",mode="w",encoding="utf-8",newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(weathers)
    print("寫入成功")

if __name__ == "__main__":
    main()


