#!/usr/bin/python3
'''
#這個應用程式是做什麼的
#要注意什麼
'''
import datasource
import pandas as pd

def main():
    data_list = datasource.get_pm25()
    dataFrame = pd.DataFrame(data=data_list)
    print(dataFrame)

if __name__ == "__main__":
    main()