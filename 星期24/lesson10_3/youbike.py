import requests
def get_youbike_info():
    #下載資料
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json'

    response = requests.get(youbike_url)
    return "info"