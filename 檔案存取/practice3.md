# Python 課堂練習設計

## 今日教學重點

JSON 處理(`json.load`、巢狀資料存取、`try/except` 例外處理、篩選與計數迴圈)

---

# 課堂範例回顧(學生剛才已練習)

## 原始程式

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

## 使用的 Python 技術

- `import json`
- `try / except FileNotFoundError` 例外處理
- `with open(...) as file:` 檔案存取語法
- `json.load(file)` 將 JSON 檔案內容讀成 Python 字典
- 巢狀資料存取(`bike_data['result']['records']`)
- `dict.get()` 取得欄位值(含預設值)
- `in` 判斷字串是否包含關鍵字
- `for` 迴圈搭配計數器與 `break` 提早結束迴圈
- f-string 格式化輸出

## 學習目標

學生可以學會:

- 使用 `json.load()` 讀取 JSON 檔案並轉換成 Python 字典/串列
- 存取巢狀結構中的資料(字典包字典、字典包串列)
- 用 `try/except` 處理檔案不存在的情況
- 依條件篩選資料,並用計數器搭配 `break` 只取前幾筆結果

---

# 本次練習題目(全新題目,與課堂範例不同)

> 說明:以下是針對相同教學重點設計的「新題目」,情境與資料和課堂範例不同,但用到的 Python 語法一致。

## 題目敘述

老師手上有一份台北市公有停車場即時資訊檔 `台北市公有停車場.json`,格式像這樣:

```json
{
    "success": true,
    "result": {
        "records": [
            {
                "id": "1",
                "name": "大安森林公園地下停車場",
                "area": "大安區",
                "address": "台北市大安區新生南路二段1號",
                "tot": 550,
                "availablecar": 120
            },
            {
                "id": "2",
                "name": "信義區公所停車場",
                "area": "信義區",
                "address": "台北市信義區松仁路100號",
                "tot": 300,
                "availablecar": 45
            }
        ]
    }
}
```

請寫一支程式:

1. 使用 `try/except FileNotFoundError` 讀取 `台北市公有停車場.json`,若檔案不存在,印出「找不到『台北市公有停車場.json』檔案！」
2. 確認 `success` 欄位為 `True` 後,取出 `result` 底下的 `records` 串列
3. 篩選出「area」欄位中含有「大安區」的停車場資料
4. 印出「======== 大安區停車場即時狀態 (前3筆) ========」
5. 每筆資料印出「【停車場】名稱」「【地址】地址」「【車位】總車位: X / 可用: Y」,並用 `"-" * 40` 分隔
6. 只印出前 3 筆,超過就用 `break` 結束迴圈

## 與課堂範例的對應

- 沿用的語法/概念:`json.load()`、`try/except FileNotFoundError`、巢狀資料存取(`['result']['records']`)、`dict.get()`、`in` 篩選關鍵字、計數器搭配 `break`、f-string 輸出
- 換掉的部分:資料情境從「YouBike 站點資料」改成「公有停車場資料」,篩選關鍵字從「新店區」改成「大安區」,欄位名稱與輸出格式也不同

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。

```python
import json

try:
    with open('台北市公有停車場.json', 'r', encoding='utf-8') as file:
        parking_data = # 請完成:用 json.load() 讀取檔案內容

    if parking_data.get('success'):
        records = # 請完成:取出 result 底下的 records 串列
        print("======== 大安區停車場即時狀態 (前3筆) ========")
        count = 0
        for record in records:
            # 請完成:篩選「area」欄位中含有「大安區」的資料
            if # 請完成:
                print(f"【停車場】{record.get('name')}")
                print(f"【地址】{record.get('address')}")
                print(f"【車位】總車位: {record.get('tot')} / 可用: {record.get('availablecar')}")
                print("-" * 40)
                count += 1
                # 請完成:當 count 達到 3 時，用 break 結束迴圈
except FileNotFoundError:
    print("找不到『台北市公有停車場.json』檔案！")
```

學生需要完成:

1. 用 `json.load(file)` 把檔案內容讀成 Python 字典
2. 寫出存取巢狀資料 `result` → `records` 的語法
3. 寫出篩選「area」含有「大安區」的條件式,以及計數達 3 筆後 `break` 的判斷式

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
import json

try:
    with open('台北市公有停車場.json', 'r', encoding='utf-8') as file:
        parking_data = json.load(file)

    if parking_data.get('success'):
        records = parking_data['result']['records']
        print("======== 大安區停車場即時狀態 (前3筆) ========")
        count = 0
        for record in records:
            if '大安區' in record.get('area', ''):
                print(f"【停車場】{record.get('name')}")
                print(f"【地址】{record.get('address')}")
                print(f"【車位】總車位: {record.get('tot')} / 可用: {record.get('availablecar')}")
                print("-" * 40)
                count += 1
                if count >= 3:
                    break
except FileNotFoundError:
    print("找不到『台北市公有停車場.json』檔案！")
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
# 步驟 1:匯入 json 模組


# 步驟 2:用 try 開始，準備處理檔案可能不存在的例外


    # 步驟 3:使用 with open() 開啟 台北市公有停車場.json（讀取模式，編碼 utf-8）


        # 步驟 4:用 json.load() 讀取檔案內容，轉成 Python 字典，存入 parking_data


    # 步驟 5:判斷 parking_data 的 success 欄位是否為 True


        # 步驟 6:取出 parking_data['result']['records']，存入 records


        # 步驟 7:印出標題「======== 大安區停車場即時狀態 (前3筆) ========」


        # 步驟 8:建立計數器 count，初始值為 0


        # 步驟 9:用 for 迴圈逐筆讀取 records 裡的資料


            # 步驟 10:判斷這筆資料的 area 欄位是否含有「大安區」


                # 步驟 11:印出【停車場】名稱、【地址】地址、【車位】總車位與可用車位（用 f-string）


                # 步驟 12:印出 "-" * 40 作為分隔線


                # 步驟 13:count 加 1


                # 步驟 14:如果 count 已經達到 3，用 break 結束迴圈


# 步驟 15:用 except FileNotFoundError 處理檔案不存在的狀況，印出「找不到『台北市公有停車場.json』檔案！」

```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
# 步驟 1:匯入 json 模組
import json

# 步驟 2:用 try 開始，準備處理檔案可能不存在的例外
try:
    # 步驟 3:使用 with open() 開啟 台北市公有停車場.json（讀取模式，編碼 utf-8）
    with open('台北市公有停車場.json', 'r', encoding='utf-8') as file:
        # 步驟 4:用 json.load() 讀取檔案內容，轉成 Python 字典，存入 parking_data
        parking_data = json.load(file)

    # 步驟 5:判斷 parking_data 的 success 欄位是否為 True
    if parking_data.get('success'):
        # 步驟 6:取出 parking_data['result']['records']，存入 records
        records = parking_data['result']['records']

        # 步驟 7:印出標題「======== 大安區停車場即時狀態 (前3筆) ========」
        print("======== 大安區停車場即時狀態 (前3筆) ========")

        # 步驟 8:建立計數器 count，初始值為 0
        count = 0

        # 步驟 9:用 for 迴圈逐筆讀取 records 裡的資料
        for record in records:
            # 步驟 10:判斷這筆資料的 area 欄位是否含有「大安區」
            if '大安區' in record.get('area', ''):
                # 步驟 11:印出【停車場】名稱、【地址】地址、【車位】總車位與可用車位（用 f-string）
                print(f"【停車場】{record.get('name')}")
                print(f"【地址】{record.get('address')}")
                print(f"【車位】總車位: {record.get('tot')} / 可用: {record.get('availablecar')}")
                # 步驟 12:印出 "-" * 40 作為分隔線
                print("-" * 40)
                # 步驟 13:count 加 1
                count += 1
                # 步驟 14:如果 count 已經達到 3，用 break 結束迴圈
                if count >= 3:
                    break
# 步驟 15:用 except FileNotFoundError 處理檔案不存在的狀況，印出「找不到『台北市公有停車場.json』檔案！」
except FileNotFoundError:
    print("找不到『台北市公有停車場.json』檔案！")
```

---

# 延伸挑戰題

## 題目

請修改程式,計算「大安區」所有停車場的**可用車位總和**,並找出可用車位數量最多的那一個停車場,印出它的名稱與可用車位數。這次不限制只看前 3 筆,而是要檢查「大安區」所有的停車場資料。

## 提示

可以思考:

- 累加總和需要先建立一個變數並在迴圈中不斷相加,這個變數要放在迴圈外面還是裡面初始化?
- 要找出「最多可用車位」的那一筆,除了自己寫比較邏輯,也可以想想 `max()` 搭配 `key` 參數怎麼用
- 如果不再需要只取前 3 筆,原本程式中的 `count`、`break` 還需要保留嗎?

---

# 思考問題

1. 為什麼要先檢查 `parking_data.get('success')` 是不是 `True`,才去讀取 `records`?如果不檢查,直接讀取可能會發生什麼問題?
2. `parking_data['result']['records']` 和 `parking_data.get('result').get('records')` 這兩種寫法有什麼不同?哪一種比較安全?為什麼?
3. 如果把 `if count >= 3: break` 拿掉,程式的執行結果會有什麼不同?

---

# 建議查詢方向

學生可以搜尋:

1. Python `json.load()` 與 `json.loads()` 的差異
2. Python 巢狀字典與串列的存取方式(dict 裡面包 list,list 裡面包 dict)
3. Python `try/except` 處理 `FileNotFoundError` 的寫法

