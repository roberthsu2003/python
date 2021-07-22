import data

if __name__ == "__main__":
    countyList = data.readAndParseCSVFile()
    for county in countyList:
        print(county.siteName)
