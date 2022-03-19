import requests

urlPathApi = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=rdec-key-123-45678-011121314&format=JSON"

def get_weather_of_taiwan():
    response = requests.get(urlPathApi)
    if response.status_code == 200:
        print('下載成功')
    else:
        print('下載失敗')
        return None

    return response.json()
