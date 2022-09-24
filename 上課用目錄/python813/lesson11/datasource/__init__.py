import requests



def download_air_data():
    url = "https://data.epa.gov.tw/api/v2/aqx_p_133?limit=150&api_key=b8416fe0-3673-4eac-be88-7ac4bb9fce06"
    res = requests.request('GET',url)
    if res.ok:
        allData = res.json()
    return allData['records']  

def download_github_csv():
    url = "https://raw.githubusercontent.com/roberthsu2003/python/master/%E4%B8%8A%E8%AA%B2%E7%94%A8%E7%9B%AE%E9%8C%84/python813/%E5%8F%B0%E5%8C%97%E5%B8%82youbike2.csv"
    print("下載csv")
    print(url)
