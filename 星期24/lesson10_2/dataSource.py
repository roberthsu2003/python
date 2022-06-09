import requests
import csv

url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=642de4f4-cfdf-4c4c-a2f3-e6e6fe1d5343&rid=7d1c0b7a-ba82-445f-ba7c-563d8014b689"
filename = "桃園youbike.csv"

def downloadData():
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename,'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)



def parseData():
    with open(filename,'r',newline='') as file:
        reader = csv.reader(file)
        csvData = list(reader)
    return csvData