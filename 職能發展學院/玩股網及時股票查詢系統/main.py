from datasource.source import getData

if __name__ == "__main__":
    stockID = input("請輸入股票代號:")
    data = getData(stockID)
    if not data.error:
        # 沒有錯誤
        print(f"股票代號:{data.id}")
        print(f"股票名稱:{data.name}")
        print(f"收盤價:{data.close}")
    else:
        print("資類取得錯誤", data.error)