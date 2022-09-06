#!/usr/bin/python3
'''
#這個應用程式是做什麼的
#要注意什麼
'''
import datasource
import pandas as pd

def doSomething(inputString):
    if inputString == '':
        return 0
    else:
        return int(inputString)

def main():
    data_list = datasource.get_pm25()
    dataFrame = pd.DataFrame(data=data_list,columns=["sitename","county","aqi","status","pm2.5","publishtime"])
    dataFrame["aqi"] = dataFrame["aqi"].map(doSomething)
    new_series = dataFrame["aqi"]
    zero_index = new_series[new_series==0].index
    dataFrame.drop(index=zero_index,inplace=True)
    delete_index = dataFrame[dataFrame["pm2.5"] == ""].index
    dataFrame.drop(index=delete_index,inplace=True)
    dataFrame['pm2.5'] = dataFrame['pm2.5'].astype(int)
    print(dataFrame)
    

if __name__ == "__main__":
    main()