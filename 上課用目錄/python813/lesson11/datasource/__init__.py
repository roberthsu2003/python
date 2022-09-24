import requests

url = "https://data.epa.gov.tw/api/v2/aqx_p_133?limit=100&api_key=b8416fe0-3673-4eac-be88-7ac4bb9fce06"

def download_air_data():
    print("下載資料")