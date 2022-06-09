#import tools.dataSource
import tools.dataSource as ds

def main():
    ds.downloadData() #下載資料
    data = ds.parseData() #解析資料
    for item in data:
        print(item)

if __name__ == "__main__":
    main()