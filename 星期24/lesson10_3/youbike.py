import requests
def get_youbike_info():
    #下載資料
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