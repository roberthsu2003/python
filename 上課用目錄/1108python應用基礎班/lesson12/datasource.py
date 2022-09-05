#!/usr/bin/python.3
'''
專門負責下載資料
'''
import requests

def download_pm25():
    url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=json"

    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)