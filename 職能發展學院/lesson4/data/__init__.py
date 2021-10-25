
def get_youbike_data():
    import requests
    youbike_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
    response = requests.get(youbike_url)
    if response.status_code == 200:
        print("下載成功")
        print(response.encoding)
        print(response.text)
    else:
        print("下載失敗")
