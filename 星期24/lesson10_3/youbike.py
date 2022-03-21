import requests

def download_youbike_data():
    # 下載資料
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json'
    try:
        response = requests.get(youbike_url)
        response.raise_for_status()
    except requests.Timeout:
        print("伺服器忙線中")
        return None
    except requests.ConnectionError:
        print("網路連線異常")
        return None
    except requests.HTTPError:
        print("網站有異常")
        return None
    except requests.RequestException:
        print("其它錯誤")
        return None
    else:
        print("下載成功")

    return response.json()

def parse_youbike_data(json):
    return "newData"

def get_youbike_info():
    allData = download_youbike_data()
    if allData is None:
        print("請等一下再試")
        return
    else:
        newData = parse_youbike_data(allData)
        return newData