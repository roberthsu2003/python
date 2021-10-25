def download_youbike_data():
    import requests
    youbike_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
    response = requests.get(youbike_url)
    if response.status_code == 200:
        print("下載成功")
        #print(response.encoding)
        return response.json()
    else:
        print("下載失敗")
        return None



def get_youbike_data():
    #下載youbike會傳出原生的json結構物件
    origanJSON = download_youbike_data()
    #origanJSON下載失敗會是None
    if(origanJSON):
        print(origanJSON)
    else:
        print("下載失敗")
