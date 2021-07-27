#data.py就是自訂的module
#空氣品質AQI的csv檔,線上下載
FILE_NAME = "aqi.csv"
aqiData = None


class County:
    def __init__(self):
        self.siteName = None
        self.name = None
        self.AQI = None
        self.status = None
        self.publishTime = None

def downloadAQIDataFromPlatForm():
    """
    從政府開放平台下載行政院aqi的資料，每1個小時，政府會更新一次
    """
    import requests
    downloadURL = "https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=csv"
    response = requests.get(downloadURL, stream=True)
    with open(FILE_NAME, 'wb') as fileObject:
        # 寫入檔案
        for chunk in response.iter_content(chunk_size=128):
            fileObject.write(chunk)


def readAndParseCSVFile():
    """
    解析下載完成的aqi.csv.
    傳出python的資料結構
    傳出list,list內的元素是County實體
    """

    #下載檔案
    import csv
    global aqiData
    downloadAQIDataFromPlatForm()
    #解析aqi.CSV
    with open(FILE_NAME, newline='',encoding='utf-8') as csvfile:
        #跳過第一行
        next(csvfile)
        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)
        # 以迴圈輸出每一列
        countyList = []
        for row in rows:
            item = County()
            item.siteName = row[0]
            item.name = row[1]
            try:
                item.AQI = int(row[2])
            except:
                item.AQI = 0

            item.status = row[4]
            item.publishTime = row[17]
            countyList.append(item)

        aqiData = countyList


def updateData():
    readAndParseCSVFile()

if __name__ != "__main__":
    readAndParseCSVFile()







