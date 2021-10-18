import requests
youbikeURL = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json'
res = requests.get(youbikeURL)
youbikeData = res.json()
allSiteDic = youbikeData['retVal']
allStations = list(allSiteDic.values())
for station in allStations:
    print(f"站名:{station['sna']}")
    print(f"時間:{station['mday']}")
    print(f"總車數:{station['tot']}")
    print(f"可還數:{station['bemp']}")
    print(f"可借數:{station['sbi']}")
    print('-----------------------')