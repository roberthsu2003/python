#import tools.dataSource
#import tools.dataSource as ds
from tools import dataSource

def main():
    dataSource.downloadData() #下載資料
    data = dataSource.parseData() #解析資料
    for item in data:
        print(item)

if __name__ == "__main__":
    main()