import csv

with open('空氣品質指標.csv','r',encoding='UTF-8') as file:
    rows=csv.reader(file)
       # for row in rows:
        #print(row)
    airList = list(rows)
    airList.pop(0)
    print(airList)



print("程式結束")