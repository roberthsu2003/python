import requests

urlPathApi = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=rdec-key-123-45678-011121314&format=JSON"

def get_weather_of_taiwan():
    try:
        response = requests.get(urlPathApi)
        response.raise_for_status()
    except requests.ConnectionError as e:
        print(e)
        return None
    except requests.HTTPError as e:
        print(e)
        return None
    except requests.Timeout as e:
        print(e)
        return None
    except requests.exceptions.RequestException as e:
        print(e)
        return None

    allData = response.json()
    locations = allData["records"]['location']
    return locations
