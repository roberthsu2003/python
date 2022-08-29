import requests
import csv
import pandas as pd
def loadData():
    url = 'https://od.cdc.gov.tw/eic/covid19/covid19_global_cases_and_deaths.csv'
    response = requests.get(url)
    if response.ok:
        print("下載成功")

    response.encoding = "utf-8"
    return response.text.splitlines()

def get_df(csv_text):
    csv_reader = csv.reader(csv_text)
    df = pd.DataFrame(csv_reader)
    df = df.iloc[1:]
    df.columns = ['國家', 'country', '確診', '死亡']
    df.set_index('國家', inplace=True)
    df['確診'] = df['確診'].str.replace(",", "")
    df['死亡'] = df['死亡'].str.replace(",", "")
    df['確診'] = df['確診'].astype(int)
    df['死亡'] = df['死亡'].astype(int)
    df["死亡比例"] = df["死亡"] / df["確診"] * 100
    return df

def main():
    all_text = loadData()
    df = get_df(all_text)
    for code in df.index:
        print(code,end=',')
    print()
    countries_str = input("請輸入國家:範例(xxx,xxxx,xxx):")
    countries_list = countries_str.split(",")
    country_df = df.loc[countries_list]
    with pd.ExcelWriter(f"{countries_str}_covid19.xlsx") as writer:
        country_df.to_excel(writer,sheet_name=countries_str)

if __name__ == "__main__":
    main()