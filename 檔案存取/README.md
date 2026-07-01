# Python 檔案存取完整指南

在實際開發中，我們經常需要將程式產生的資料永久儲存於硬碟，或是讀取外部的設定檔與資料集。Python 提供了直觀且安全的檔案存取機制，本指南將由淺入深帶領您掌握文字檔、例外處理、CSV 與 JSON 的操作方法。

---

## 1. 檔案存取特性對比

在進入實作前，我們先通過這張表了解各檔案格式的存取特性與適用場景：

| 檔案格式 | 適用場景 | Python 處理模組 | 讀寫主要方式 | 特性與限制 |
| :--- | :--- | :--- | :--- | :--- |
| **文字檔 (.txt)** | 簡單日誌、純文字備忘、設定檔 | 內建 `open()` | `read()`, `write()` | 資料無結構，僅能以字串存取 |
| **CSV 檔 (.csv)** | 表格式資料、資料庫匯出、輕量試算表 | 內建 `csv` 模組 | `csv.reader()`, `csv.writer()` | 欄位以逗號分隔，讀出皆為字串 |
| **JSON 檔 (.json)** | 網路 API 交換格式、複雜配置、巢狀結構 | 內建 `json` 模組 | `json.load()`, `json.dump()` | 支援鍵值對與陣列，極為通用 |

---

## 2. 基礎檔案讀寫與關閉

處理任何檔案的基礎三步驟為：**開啟 ➡️ 讀寫 ➡️ 關閉**。

### 2.1 檔案存取模式對照表
```python
# 基本開啟語法
file_object = open(file_name, access_mode, encoding='utf-8')
```
> [!IMPORTANT]
> **處理中文字元**時，務必帶上 `encoding='utf-8'`，否則在不同作業系統（如 Windows）上容易因系統預設編碼（如 ANSI/CP950）產生編碼錯誤或亂碼。

常見模式：
* **`r`**：唯讀模式（預設）。若檔案不存在會拋出錯誤。
* **`w`**：覆寫模式。會清空原檔案內容；若檔案不存在則建立新檔。
* **`a`**：附加模式（Append）。資料會附加在檔案末尾。

### 2.2 最佳實踐：使用 `with` 語句
傳統使用 `close()` 手動關閉檔案，一旦在讀寫中途出錯，程式提前中斷，會導致檔案資源無法關閉而被鎖定。使用 `with` 語句（Context Manager）能確保不論中途是否發生錯誤，離開區塊時 Python 都會**自動且安全地關閉檔案**。
```python
# 推薦寫法：自動安全關閉
with open('sample.txt', 'w', encoding='utf-8') as f:
    f.write("使用 with 語句安全寫入")
```

### 2.3 檔案寫入與讀取小範例
```python
# 1. 寫入多行文字
with open('sample.txt', 'w', encoding='utf-8') as f:
    f.write("Python 程式設計\n")
    f.write("輕鬆學會檔案存取。")

# 2. 讀取整個文字檔案
with open('sample.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("【檔案內容】:\n", content)
```

### 💡 實戰生活主題範例：過濾日誌檔案
> **為什麼此場景需要文字檔處理？**  
> 在分析系統日誌或清洗純文字檔案時，我們常需要排除雜訊（如空行或註解行），並將篩選後的資料整理排序儲存。
```python
cleaned_data = []

# 讀取 data1.txt，排除以 # 開頭的註解行與空行
with open('data1.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        # 跳過空行與註解行
        if not line or line.startswith('#'):
            continue
        cleaned_data.append(line)

cleaned_data.sort()

# 將結果重新寫入新檔案
with open('result-readlines.txt', 'w', encoding='utf-8') as out_f:
    out_f.write('\n'.join(cleaned_data))
print("整理完成！結果已儲存至 result-readlines.txt")
```

---

## 3. 檔案例外處理

在讀寫檔案時，難免會遇到「找不到檔案」、「權限不足」等異常。為了避免程式直接崩潰當機，必須使用 `try...except` 結構進行防禦性例外處理。

### 3.1 結合 with 語句的例外處理
```python
try:
    with open('non_exist_file.txt', 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print("【錯誤】找不到指定的檔案，請確認檔案路徑是否正確。")
except PermissionError:
    print("【錯誤】沒有權限存取該檔案。")
except Exception as e:
    print(f"【錯誤】發生未知的異常：{e}")
```

### 💡 實戰生活主題範例：防禦性載入與建立設定檔
```python
# 當設定檔不存在時，自動建立並寫入預設設定，避免程式因此中斷
default_config = "theme=dark\nfontsize=14"

try:
    with open('config.txt', 'r', encoding='utf-8') as f:
        config_data = f.read()
        print("讀取設定檔成功。")
except FileNotFoundError:
    print("找不到設定檔，正在建立預設設定檔...")
    with open('config.txt', 'w', encoding='utf-8') as f:
        f.write(default_config)
    config_data = default_config

print("載入的配置內容:\n", config_data)
```

---

## 4. 結構化資料 - CSV 處理

CSV（逗號分隔值）是一種簡單的表格純文字格式，欄位間以逗號區隔，常用於資料庫與試算表資料的交換。

### 4.1 寫入 CSV 檔案
使用內建的 `csv` 模組，並在 `open()` 中設定 `newline=''` 參數，以防止在 Windows 系統上寫入時產生多餘的空白行。
```python
import csv

# 寫入簡單學生成績
with open('scores.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # 寫入表頭
    writer.writerow(['學號', '國文', '數學'])
    # 寫入多列資料
    writer.writerows([
        ['S001', 95, 88],
        ['S002', 82, 90]
    ])
```

### 4.2 讀取 CSV 檔案
* **`csv.reader`**：將每行讀取為二維清單（List of Lists），適合簡單結構。
* **`csv.DictReader`**：將每行讀取為 OrderedDict（字典），可以利用欄位名稱直接存取。

### 💡 實戰生活主題範例：過濾特定區域人口密度 (使用 DictReader)
> **為什麼此場景需要 DictReader？**  
> 政府開放資料的 CSV 欄位極多。使用欄位名稱作為鍵值（如 `row.get('區域別')`）讀取資料，可讀性高且不易對錯欄位。
```python
import csv

nptc_data = []

# 讀取各鄉鎮市區人口密度 CSV 檔 (跳過第一行非欄位說明文字)
with open('各鄉鎮市區人口密度.csv', 'r', encoding='utf-8') as file:
    next(file)  # 跳過第一列說明
    
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        # 篩選「區域別」中含有「新北市」的資料列
        if '新北市' in row.get('區域別', ''):
            nptc_data.append({
                '統計年': row.get('統計年'),
                '區域別': row.get('區域別'),
                '年底人口數': row.get('年底人口數'),
                '土地面積': row.get('土地面積'),
                '人口密度': row.get('人口密度')
            })

print("新北市前兩筆行政區人口密度:")
for item in nptc_data[:2]:
    print(item)
```

---

## 5. 結構化資料 - JSON 處理

JSON（JavaScript Object Notation）是網路上最通用的輕量級資料交換格式，支援巢狀物件與陣列。

### 5.1 Python 與 JSON 轉換
* **序列化（轉為 JSON 字串/檔案）**：`json.dumps()` / `json.dump()`。
* **反序列化（將 JSON 載入為 Python 物件）**：`json.loads()` / `json.load()`。
> [!IMPORTANT]
> 處理含有中文字的 JSON 時，必須指定 `ensure_ascii=False`，否則中文會被自動轉換為 Unicode 逸出碼（如 `\u53f0\u7063`）。

### 5.2 JSON 序列化與寫檔小範例
```python
import json

info = {'name': '張三', 'skills': ['Python', 'SQL']}

# 轉換為 JSON 格式字串 (使用 indent 美化排版)
json_str = json.dumps(info, ensure_ascii=False, indent=4)
print(json_str)
```

### 💡 實戰生活主題範例：YouBike 站點狀態查詢
> **為什麼此場景需要 JSON？**  
> 城市租賃系統資料多為多層嵌套結構，使用 JSON 轉換成 Python 字典後，可以非常直覺地利用鍵值（Key）來過濾出所需行政區的站點狀態。
```python
import json

try:
    with open('新北市公共自行車租賃系統.json', 'r', encoding='utf-8') as file:
        bike_data = json.load(file)
        
    if bike_data.get('success'):
        records = bike_data['result']['records']
        print("======== 新店區 YouBike 站點狀態 (前3筆) ========")
        count = 0
        for record in records:
            if '新店區' in record.get('sarea', ''):
                print(f"【站名】{record.get('sna')}")
                print(f"【位置】{record.get('ar')}")
                print(f"【車位】可借: {record.get('sbi')} / 可還: {record.get('bemp')}")
                print("-" * 40)
                count += 1
                if count >= 3:
                    break
except FileNotFoundError:
    print("找不到『新北市公共自行車租賃系統.json』檔案！")
```

---

## 6. 綜合實戰：網路 API 天氣資料下載並轉存 CSV

本實戰展示一個完整的資料流管道（Data Pipeline）：
1. 使用 `requests` 模組，呼叫氣象署開放資料 API 下載「今明 36 小時天氣預報」 JSON。
2. 解析複雜嵌套的 JSON 欄位，擷取各城市的預報起訖時間、最高溫、最低溫與舒適度感覺。
3. 使用 `csv.DictWriter` 將處理後的乾淨資料寫入為 `目前天氣.csv`。

```python
import requests
import csv

def download_weather_raw_json():
    """發送網路請求下載天氣資料"""
    url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=rdec-key-123-45678-011121314&format=JSON'
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("API 資料下載成功。")
            return response.json()
        print(f"下載失敗，HTTP 狀態碼：{response.status_code}")
        return None
    except requests.RequestException as e:
        print(f"連線發生錯誤：{e}")
        return None

def parse_weather_data(raw_json):
    """解析巢狀 JSON 資料，轉換成乾淨的字典清單"""
    if not raw_json:
        return []
    
    try:
        locations = raw_json['cwbopendata']['dataset']['location']
    except KeyError:
        print("JSON 資料結構不符，無法解析。")
        return []
        
    weather_list = []
    for loc in locations:
        city_name = loc['locationName']
        elements = loc['weatherElement']
        try:
            # 擷取預報要素的第一個時間區間資料
            start_time = elements[1]['time'][0]['startTime']
            end_time = elements[1]['time'][0]['endTime']
            max_temp = float(elements[1]['time'][0]['parameter']['parameterName'])
            min_temp = float(elements[2]['time'][0]['parameter']['parameterName'])
            feeling = elements[3]['time'][0]['parameter']['parameterName']
            
            weather_list.append({
                '城市': city_name,
                '啟始時間': start_time,
                '結束時間': end_time,
                '最高溫度': max_temp,
                '最低溫度': min_temp,
                '感覺': feeling
            })
        except (IndexError, KeyError, ValueError):
            continue
            
    return weather_list

def save_to_csv(data_list, filename='目前天氣.csv'):
    """使用 csv.DictWriter 將解析資料儲存成 CSV 檔"""
    if not data_list:
        print("無資料可供儲存。")
        return
        
    fieldnames = ['城市', '啟始時間', '結束時間', '最高溫度', '最低溫度', '感覺']
    try:
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_list)
        print(f"CSV 檔案儲存成功！檔案名稱：{filename}")
    except IOError as e:
        print(f"檔案寫入失敗：{e}")

def main():
    print("正在啟動天氣資料下載與轉存工具...")
    weather_json = download_weather_raw_json()
    if weather_json:
        parsed_data = parse_weather_data(weather_json)
        save_to_csv(parsed_data)
    print("下載與轉換作業結束。")

if __name__ == '__main__':
    main()
```
