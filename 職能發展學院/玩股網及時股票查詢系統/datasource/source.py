import requests
from .stockInfo import StockInfo
from requests import HTTPError, ConnectionError, Timeout


def getData(stock):
    stockInfo = StockInfo()
    stockInfo.id = stock
    url = "https://www.wantgoo.com/investrue/" + stock + "/daily-candlestick"
    infoURL = "https://www.wantgoo.com/stock/" + stock + "/company-profile-data"
    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    try:
        response = requests.get(url, headers=header)
        infoResponse = requests.get(infoURL, headers=header)
        response.raise_for_status()
    except HTTPError as e:
        print("伺服器錯誤")
        stockInfo.error = e
    except ConnectionError as e:
        print("連線錯誤")
        stockInfo.error = e
    except Timeout as e:
        print("伺服器忙錄")
        stockInfo.error = e
    else:
        try:
            json = response.json()
            if not json is None: #如果使用者傳入的資料
                stockInfo.time = json["time"]
                stockInfo.open = json["open"]
                stockInfo.close = json["close"]
                stockInfo.volume = json["volume"]
                stockInfo.millionAmount = json["millionAmount"]
                stockInfo.high = json["high"]
                stockInfo.low = json["low"]
            else:
                stockInfo.error = "無法解析資料"

            infoJson = infoResponse.json()
            if not infoJson is None:
                stockInfo.name = infoJson["name"]
            else:
                stockInfo.error = "無法解析資料"
        except requests.exceptions.JSONDecodeError as e:
            print("json解析錯誤")
            stockInfo.error = "json解析錯誤"
    return stockInfo