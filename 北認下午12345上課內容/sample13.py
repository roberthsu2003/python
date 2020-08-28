import csv

with open('空氣品質指標.csv','r',encoding='UTF-8') as file:
    rows=csv.reader(file)
    airList = []
    for row in rows:
        cityAir = []
        cityAir.append(row[0])
        cityAir.append(row[1])
        cityAir.append(row[2])
        cityAir.append(row[17])
        airList.append(cityAir)
    airList.pop(0)
    for air in airList:
        print(air)
print("程式結束")