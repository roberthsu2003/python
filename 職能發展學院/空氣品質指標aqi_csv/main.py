import data

if __name__ == "__main__":
    countyList = data.aqiData
    for county in countyList:
        print(county.siteName,county.name,county.AQI,county.status,county.publishTime)
