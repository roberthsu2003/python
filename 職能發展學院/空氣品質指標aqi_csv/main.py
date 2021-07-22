import data

if __name__ == "__main__":
    countyList = data.aqiData
    print(countyList)
    for county in countyList:
        print(county.siteName,county.name,county.AQI,county.status,county.publishTime)
