import requests
from requests import ConnectionError,HTTPError,Timeout

url = "https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&format=json"
newRecords = [] # 建立要傳出的list
def getAirData():
    global newRecords
    newRecords = []  #由於有更新的動作，所以要全部清空，重新再抓一次
    try:
        response = requests.get(url)
        response.raise_for_status()
    except ConnectionError:
        print('找不到伺服器')
        return None
    except HTTPError:
        print('網頁找不到')
        return None
    except Timeout:
        print('超過時間沒有回應')
        return None
    else:
        if response.status_code == 200:
            print("下載成功")
        else:
            print("失敗")
            return None



    allData = response.json()  # dictinary
    records = allData['records']  # list
    for record in records:  # record是dictionary
        newItem = {}
        newItem["監測點"] = record["SiteName"]
        newItem["城市"] = record['County']
        newItem["AQI"] = record['AQI']
        newItem["狀態"] = record['Status']
        newItem["時間"] = record['ImportDate']
        newRecords.append(newItem)

    return newRecords

def getPositionList():
    positionList = []
    for itemDic in newRecords:
        positionList.append(itemDic['監測點'])
    return tuple(positionList)

def getOneSiteData(name):
    for itemDic in newRecords:
        if itemDic['監測點'] == name:
            return itemDic



__all__ = ["newRecords", "getAirData","getPositionList", "getOneSiteData"]




