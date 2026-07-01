# 檔案存取 (File Access)

## 課程學習重點
1. **檔案基本讀寫與關閉**：掌握 `open()` 函數、檔案存取模式，以及最佳實踐 `with` 語句的運用。
2. **檔案例外處理**：利用 `try...except` 結構優雅處理讀寫過程中常見的例外錯誤。
3. **CSV 結構化資料操作**：學會使用 `csv` 模組寫入與讀取 CSV 檔案（包含 `csv.reader` 與 `csv.DictReader` 的篩選應用）。
4. **JSON 資料處理**：掌握 Python 與 JSON 資料型態的映射，以及序列化（`dump/dumps`）與反序列化（`load/loads`）的操作。
5. **綜合實戰**：透過 `requests` 套件從政府開放 API 下載氣象 JSON 資料，解析後轉存為 CSV 格式。

---


## 第一章：基礎檔案讀寫與關閉

### 1. 檔案存取基本概念
在讀取或寫入檔案之前，必須使用 Python 內建的 `open()` 函數開啟檔案。這個函數會建立一個「檔案物件」（File Object），作為程式與硬碟檔案之間的溝通橋樑。

**基本語法：**
```python
file_object = open(file_name, access_mode, encoding='utf-8')
```
> [!IMPORTANT]
> **中文編碼設定**：處理包含中文字元的文字檔時，務必加上 `encoding='utf-8'` 參數，否則在不同作業系統（如 Windows）上容易產生亂碼。

### 2. 檔案存取模式對照表

| 存取模式 | 描述 |
| :--- | :--- |
| **`r`** | **唯讀模式（預設）**。僅能讀取檔案。若檔案不存在會拋出錯誤。 |
| **`rb`** | **二進位唯讀模式**。用於讀取圖片、音訊或壓縮檔等非文字檔案。 |
| **`r+`** | **讀寫模式**。檔案指標在檔頭，可讀可寫，若檔案不存在會拋出錯誤。 |
| **`w`** | **覆寫模式**。僅供寫入。若檔案存在會**清空原檔案內容**；若檔案不存在則建立新檔。 |
| **`wb`** | **二進位覆寫模式**。以二進位格式清空覆寫或建立新檔。 |
| **`w+`** | **讀寫覆寫模式**。可讀可寫，並會清空檔案。 |
| **`a`** | **附加模式（Append）**。僅供寫入，資料會接在檔案末尾。若檔案不存在會建立新檔。 |
| **`ab`** | **二進位附加模式**。以二進位格式將資料附加至檔案末尾。 |
| **`a+`** | **讀寫附加模式**。可讀可寫，寫入時資料會接在檔案末尾。 |

---

### 3. 手動關閉檔案的風險
當我們以傳統方式開啟檔案時，必須手動呼叫 `close()` 關閉檔案。
```python
# 傳統方式（不推薦）
file = open('sample1.txt', 'w', encoding='utf-8')
file.write("寫入測試內容")
file.close()
```
> [!WARNING]
> **手動關閉的風險**：如果在 `open()` 和 `close()` 之間發生錯誤（例外），程式會提前中斷，導致 `close()` 無法執行。這會導致檔案一直被作業系統鎖定、佔用系統資源，甚至造成緩衝區內的資料未能正確寫入硬碟中。

### 4. 最佳實踐：使用 `with` 語句（Context Manager）
使用 `with` 語句來操作檔案是 Python 的標準最佳實踐。當程式離開 `with` 程式區塊時，Python 會**自動且安全地關閉檔案**，即使中途發生例外錯誤也一樣。
```python
# 現代推薦寫法
with open('sample1.txt', 'w', encoding='utf-8') as file:
    file.write("使用 with 語句安全寫入")
# 離開此區塊後，檔案已自動關閉
```

---

### 5. 檔案寫入範例

#### 範例 1：使用 `print()` 函數寫入
`print()` 可以透過指定 `file` 參數，將輸出的內容直接寫入開啟的檔案中。
```python
text = """python與中文
1. 我們來試試看中文儲存能力。
2. 許這個字會有編碼衝突風險。
3. 犇這個字必須是utf8編碼才有。"""

# 將 print 輸出的內容導向到檔案
with open('data.txt', 'w', encoding='utf-8') as f:
    print(text, file=f)
```

#### 範例 2：使用 `write()` 方法寫入
使用檔案物件的 `.write()` 方法可以精確寫入字串，它不會自動在末尾加上換行符，需要自行控制。
```python
text_to_write = "這是第一行。\n這是第二行。"

with open('sample1.txt', 'w', encoding='utf-8') as file:
    file.write(text_to_write)
```

---

### 6. 檔案讀取方式

#### 讀取方法說明：
- **`read([size])`**：讀取指定數量的字元，若未帶參數則讀取整份檔案。
- **`readline()`**：每次只讀取一行，記憶體佔用極小，適合處理超大型檔案。
- **`readlines()`**：讀取整份檔案，並以每一行為元素，返回一個清單（List）。

#### 常用字串清理方法：
- `strip()`：去除字串前後的空白與換行符（`\n`）。
- `lstrip()` / `rstrip()`：去除字串左邊 / 右邊的空白。
- `startswith('字元')`：判斷字串是否以特定字元開頭。

#### 範例：逐行讀取、清理並過濾資料
讀取 `data1.txt`，排除註解行（以 `#` 開頭）與空白行，並將內容進行排序後另存新檔：
```python
result = []

# 讀取並過濾
with open('data1.txt', 'r', encoding='UTF-8') as f:
    for line in f.readlines():
        cleaned_line = line.strip()
        # 如果是空行或註解行，則略過
        if not cleaned_line or cleaned_line.startswith('#'):
            continue 
        result.append(cleaned_line)

# 排序處理
result.sort()
print("整理後的檔案內容：", result)

# 將結果重新寫入新檔案
with open('result-readlines.txt', 'w', encoding='UTF-8') as out_file:
    out_file.write('\n'.join(result))
```

[進階練習：文字檔讀取、逐行處理與篩選排序](practice1.md)

---

## 第二章：檔案例外處理

在讀寫檔案時，難免會遇到許多不可預期的錯誤（例如：找不到檔案、沒有權限讀取、磁碟空間不足等）。為了避免程式因為這些異常而直接崩潰，必須使用 `try...except` 結構來進行例外處理。

### 1. 常見檔案例外類型
- **`FileNotFoundError`**：找不到指定的檔案。
- **`PermissionError`**：權限不足（例如嘗試寫入唯讀檔案）。
- **`IOError`**：通用的輸入輸出錯誤。

### 2. 例外處理範例
將 `try...except` 與 `with` 語句完美結合的範例：
```python
try:
    with open('data.txt', 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print("【錯誤】找不到指定的檔案，請確認路徑是否正確。")
except PermissionError:
    print("【錯誤】沒有權限存取該檔案。")
except IOError:
    print("【錯誤】檔案輸入輸出發生異常。")
except Exception as e:
    print(f"【錯誤】發生未知的異常：{e}")
```

---

## 第三章：結構化資料 - CSV 處理

**CSV（Comma-Separated Values，逗號分隔值）** 是一種簡單的文字檔案格式，通常以逗號來分隔不同的欄位資料。它廣泛用於資料庫的匯入、匯出與不同軟體間的資料交換。

> [!NOTE]
> **CSV 格式的限制**：
> 1. CSV 沒有資料類型，讀取出來的資料**一律是字串**，需手動轉型。
> 2. CSV 沒有字型、顏色或單元格寬度等外觀樣式設定。

### 1. 寫入 CSV 檔案
使用內建的 `csv` 模組可以輕鬆處理 CSV。在 `open()` 中設定 `newline=''` 能有效避免在 Windows 系統上寫入時產生多餘的空行。

#### 範例：隨機生成 50 位學生的成績單並寫入 CSV
```python
import csv
import random

with open('students.csv', 'w', newline='', encoding='UTF-8') as file:
    csv_writer = csv.writer(file)
    
    # 寫入標頭列
    csv_writer.writerow(['學號', '國文', '英文', '數學', '自然', '社會'])
    
    # 寫入 50 位學生的成績
    for i in range(1, 51):
        # 學號格式為 student_01, student_02 ...
        student_id = f"student_{i:02d}"
        scores = [random.randint(50, 100) for _ in range(5)]
        csv_writer.writerow([student_id] + scores)

print("學生資料已成功寫入 students.csv")
```

### 2. 讀取 CSV 檔案

#### 方法 A：使用 `csv.reader`（讀取為二維清單）
讀取後利用 `next()` 跳過標頭，再將讀取到的分數轉換為整數型態以利後續計算：
```python
import csv

students_list = []

with open('students.csv', 'r', encoding='UTF-8') as file:
    csv_reader = csv.reader(file)
    
    # 跳過並取得首行的標頭列
    header = next(csv_reader)
    
    # 逐行讀取並轉型
    for row in csv_reader:
        # row[0] 為學號（維持字串），row[1:] 為分數（轉為整數）
        converted_row = [row[0]] + list(map(int, row[1:]))
        students_list.append(converted_row)

print("前三筆學生資料：", students_list[:3])

# 成績查詢功能
query_id = input('請輸入欲查詢的學號 (格式如 student_01): ').strip()
found = False
for student in students_list:
    if student[0] == query_id:
        print(f"查詢結果：學號 {query_id} 的成績為 {student[1:]}")
        found = True
        break
if not found:
    print("找不到該學生的資料。")
```

#### 方法 B：使用 `csv.DictReader`（讀取為字典清單）
適合用來讀取結構複雜且含有欄位名稱的 CSV。以下示範讀取 `各鄉鎮市區人口密度.csv`，跳過第一列說明文字後，篩選出「新北市」的行政區資料：
```python
import csv

nptc_pop_data = []

with open('各鄉鎮市區人口密度.csv', 'r', encoding='UTF-8') as file:
    # 該 CSV 首行可能是非欄位說明文字，先將其跳過
    next(file)
    
    # 以第二行作為鍵（Keys）來讀取資料
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        # 篩選「區域別」中包含「新北市」的資料
        if '新北市' in row.get('區域別', ''):
            nptc_pop_data.append({
                '統計年': row.get('統計年'),
                '區域別': row.get('區域別'),
                '年底人口數': row.get('年底人口數'),
                '土地面積': row.get('土地面積'),
                '人口密度': row.get('人口密度')
            })

# 顯示前三筆篩選結果
print(f"篩選出新北市的行政區共 {len(nptc_pop_data)} 筆：")
for item in nptc_pop_data[:3]:
    print(item)
```

[進階練習：使用 csv.DictReader 篩選行政區人口資料](practice2.md)

---

## 第四章：結構化資料 - JSON 處理

**JSON（JavaScript Object Notation）** 是網路上最通用的輕量級資料交換格式。在 Python 中，我們可以非常方便地將 Python 的 Dict 或 List 轉為 JSON 格式，反之亦然。

### 1. Python 與 JSON 型態對照表

| Python 資料型態 | JSON 資料型態 | 說明 |
| :--- | :--- | :--- |
| `dict` | object | `{}` 鍵值對 |
| `list`, `tuple` | array | `[]` 陣列清單 |
| `str` | string | `""` 字串 |
| `int`, `float` | number | 數值 |
| `True` | true | 布林值真 |
| `False` | false | 布林值假 |
| `None` | null | 空值 |

---

### 2. 從 Python 轉成 JSON（序列化）
- **`json.dumps()`**：將 Python 物件轉換為 JSON 格式的**字串**。
- **`json.dump()`**：將 Python 物件轉換並寫入 JSON **檔案**中。

> [!IMPORTANT]
> **中文處理關鍵參數**：在轉換含有中文的資料時，必須加上 `ensure_ascii=False`，否則中文會自動被轉換為 Unicode 逸出碼（如 `\u53f0\u7063`）。

#### 範例：將字典儲存為 JSON 檔案
```python
import json

country_codes = {'tw': '台灣', 'jp': '日本', 'hk': '香港', 'us': '美國'}

# 1. 轉換為 JSON 格式字串（使用 indent 讓排版更易讀）
json_string = json.dumps(country_codes, ensure_ascii=False, indent=4)
print("產生的 JSON 字串：\n", json_string)

# 2. 直接寫入成 JSON 檔案
with open('codes.json', 'w', encoding='utf-8') as file:
    json.dump(country_codes, file, ensure_ascii=False, indent=4)
print("JSON 檔案 codes.json 儲存完成。")
```

---

### 3. 從 JSON 轉回 Python（反序列化）
- **`json.loads()`**：將 JSON 格式的**字串**載入為 Python 物件。
- **`json.load()`**：將 JSON **檔案**載入為 Python 物件。

#### 範例：讀取 JSON 檔案並解析
```python
import json

# 載入 JSON 檔案並轉換為 Python 字典
with open('codes.json', 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)

print("讀取出來的 Python 物件型態：", type(loaded_data))
print("台灣的對應英文代碼值：", loaded_data.get('tw'))
```

---

### 4. JSON 實戰：新北市公共自行車租賃系統
讀取本地的 JSON 檔案，解析後查詢並篩選出「新店區」的所有 YouBike 站點資訊：
```python
import json

try:
    with open('新北市公共自行車租賃系統.json', 'r', encoding='utf-8') as file:
        bike_data = json.load(file)
        
    if bike_data.get('success'):
        records = bike_data['result']['records']
        print("======== 新店區 YouBike 站點狀態 ========")
        for record in records:
            if '新店區' in record.get('sarea', ''):
                print(f"【站名】{record.get('sna')}")
                print(f"【位置】{record.get('ar')}")
                print(f"【座標】緯度: {record.get('lat')}, 經度: {record.get('lng')}")
                print(f"【車位數】可借: {record.get('sbi')} / 可還空位: {record.get('bemp')} (總車位: {record.get('tot')})")
                print("-" * 50)
    else:
        print("資料讀取失敗：JSON 中的 success 狀態不為 True")
except FileNotFoundError:
    print("錯誤：找不到『新北市公共自行車租賃系統.json』檔案！")
```

[進階練習：JSON 巢狀資料存取與 YouBike 站點查詢](practice3.md)

---

## 第五章：綜合實戰：網路 API 下載 JSON 並轉存 CSV

本章展示一個完整的實務應用：
1. 使用 `requests` 模組，呼叫氣象署開放資料 API 下載「今明 36 小時天氣預報」 JSON。
2. 解析複雜的嵌套 JSON 欄位，萃取出各縣市的最高溫、最低溫與舒適度。
3. 使用 `csv.DictWriter` 將處理後的乾淨資料寫入為 `目前天氣.csv`。

> [!NOTE]
> 執行此範例前，請確保已安裝 `requests` 套件：
> ```bash
> pip install requests
> ```

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
        else:
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
            # 擷取預報要素的第 0 個時間區間資料 (今明 36 小時的第一個區間)
            # Element 1: MaxT (最高溫度)
            # Element 2: MinT (最低溫度)
            # Element 3: CI (舒適度感覺)
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
        except (IndexError, KeyError, ValueError) as e:
            print(f"解析 {city_name} 資料時發生異常，已跳過：{e}")
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
            
            # 寫入標頭
            writer.writeheader()
            # 寫入資料列
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
    print("程式結束。")

if __name__ == '__main__':
    main()
```

---

## 💡 AI 賦能：利用 AI 將此範例升級為 Tkinter 桌面 App

學會了「呼叫 API 下載天氣 JSON」、「解析巢狀資料」、「寫入 CSV」這三個核心技能後，我們就可以請 AI 助手（如 Gemini、Claude 或 ChatGPT）幫我們快速加上圖形化視窗介面（GUI），把終端機腳本升級為一個精美的桌面 App。

只需將下方的 **AI Prompt 提示詞** 完整複製，並把上方的原始程式碼貼入「---貼上程式碼---」處後送出，AI 便會產生完整的 Tkinter 應用程式。

> [!TIP]
> **可直接複製使用的 AI Prompt 提示詞：**
> 
> ```text
> 我有一個 Python 腳本，功能是呼叫氣象署開放 API 下載今明 36 小時天氣預報的 JSON 資料，
> 解析後取出每個城市的最高溫度、最低溫度和舒適度，並儲存為 CSV 檔案。
> 程式碼如下：
> 
> ---貼上程式碼---
> 
> 請以此程式碼為基礎，使用 Python 內建的 tkinter 與 ttk 模組，幫我改寫成一個桌面視窗應用程式（GUI App）。
> 
> 視窗介面需求如下：
> 1. 視窗標題為「今明 36 小時天氣預報」，視窗大小設為 600x450。
> 2. 最上方放一個「下載最新天氣資料」按鈕；按下後呼叫 API，若成功則彈出成功提示框，若網路錯誤則彈出警告對話框（使用 messagebox）。
> 3. 資料下載成功後，自動更新一個「城市」下拉選單（ttk.Combobox），選項來自解析後的城市名稱清單。
> 4. 使用者切換城市後，下方的文字區域即時顯示該城市的天氣預報：
>    - 預報時段（啟始時間 ～ 結束時間）
>    - 最高溫度 / 最低溫度（°C）
>    - 舒適度感覺
> 5. 最下方放一個「儲存為 CSV」按鈕；按下後呼叫原有的 save_to_csv() 函式儲存目前所有城市資料，完成後彈出成功對話框。
> 6. 若尚未下載資料就按「城市切換」或「儲存 CSV」，需彈出提示要求先下載。
> 7. 程式碼結構清晰，使用類別（class WeatherApp）封裝視窗邏輯，並附上完整的繁體中文註解。
> ```
