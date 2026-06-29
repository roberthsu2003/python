# Python 課堂練習設計

## 今日教學重點

參數使用 `傳送可變實體`

---

# 課堂範例回顧(學生剛才已練習)

## 原始程式

```python
def turbo(listSpeed):
    print('加速前（函式內）速度:', listSpeed[0])
    listSpeed[0] += 10  # 直接修改傳入之列表物件的內容
    print('加速後（函式內）速度:', listSpeed[0])

if __name__ == '__main__':
    s = 80
    listS = [s]  # 將整數打包進可變的列表 (List) 中
    
    # 呼叫函式：傳入列表
    turbo(listS)
    
    # 由於列表是可變的，外部的列表內容已經被函式直接改變了！
    print('加速後（函式外）速度:', listS[0])  # 輸出: 90
```

## 使用的 Python 技術

例如:

- function
- list
- list index
- parameter
- print()
- `if __name__ == '__main__':`
- 修改可變物件內容

## 學習目標

學生可以學會:

- 將資料放入列表中，再把列表傳入函式。
- 在函式內修改列表內容，觀察函式外資料也跟著改變。
- 理解「傳入可變實體」時，函式可以直接改變原本的物件內容。

---

# 本次練習題目(全新題目,與課堂範例不同)

> 說明:以下是針對相同教學重點設計的「新題目」,情境與資料和課堂範例不同,但用到的 Python 語法一致。

## 題目敘述

設計一個「點數加值」程式。主程式中有一位會員目前點數為 `120`，請將這個點數放入列表 `listPoint` 中，再把列表傳入函式 `addPoint()`。

函式內要先印出加值前的點數，接著將列表中的點數增加 `50`，再印出加值後的點數。回到函式外後，也要印出目前會員點數，確認函式內修改列表後，函式外的列表內容也已經改變。

## 與課堂範例的對應

- 沿用的語法/概念:函式參數、列表、使用 `list[0]` 取值與修改值、傳入可變物件後在函式內直接改變內容
- 換掉的部分:原本是車速加速，改成會員點數加值；原本增加速度 `10`，改成增加點數 `50`

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。

```python
def addPoint(listPoint):
    print('加值前（函式內）點數:', listPoint[0])
    
    # 請完成: 將列表中的點數增加 50
    
    print('加值後（函式內）點數:', listPoint[0])

if __name__ == '__main__':
    point = 120
    
    # 請完成: 將 point 放入列表 listPoint 中
    
    
    # 請完成: 呼叫 addPoint()，並傳入 listPoint
    
    
    print('加值後（函式外）點數:', listPoint[0])
```

學生需要完成:

1. 在函式內修改 `listPoint[0]` 的值，讓點數增加 `50`。
2. 在主程式中建立列表 `listPoint`，把 `point` 放進列表。
3. 呼叫 `addPoint(listPoint)`，觀察函式外的列表內容是否被改變。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
def addPoint(listPoint):
    print('加值前（函式內）點數:', listPoint[0])
    
    listPoint[0] += 50
    
    print('加值後（函式內）點數:', listPoint[0])

if __name__ == '__main__':
    point = 120
    
    listPoint = [point]
    
    addPoint(listPoint)
    
    print('加值後（函式外）點數:', listPoint[0])
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
# 定義 addPoint 函式，參數名稱為 listPoint

# 印出加值前（函式內）的點數，點數存在 listPoint[0]

# 將 listPoint[0] 的點數增加 50

# 印出加值後（函式內）的點數，點數存在 listPoint[0]

# 判斷目前程式是否為主程式

# 建立變數 point，設定會員目前點數為 120

# 建立列表 listPoint，將 point 放入列表中

# 呼叫 addPoint 函式，並傳入 listPoint

# 印出加值後（函式外）的點數，觀察 listPoint[0] 是否已經改變
```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
# 定義 addPoint 函式，參數名稱為 listPoint
def addPoint(listPoint):

    # 印出加值前（函式內）的點數，點數存在 listPoint[0]
    print('加值前（函式內）點數:', listPoint[0])

    # 將 listPoint[0] 的點數增加 50
    listPoint[0] += 50

    # 印出加值後（函式內）的點數，點數存在 listPoint[0]
    print('加值後（函式內）點數:', listPoint[0])

# 判斷目前程式是否為主程式
if __name__ == '__main__':

    # 建立變數 point，設定會員目前點數為 120
    point = 120

    # 建立列表 listPoint，將 point 放入列表中
    listPoint = [point]

    # 呼叫 addPoint 函式，並傳入 listPoint
    addPoint(listPoint)

    # 印出加值後（函式外）的點數，觀察 listPoint[0] 是否已經改變
    print('加值後（函式外）點數:', listPoint[0])
```

---

# 延伸挑戰題

## 題目

將主練習題改成「扣除兌換點數」程式。會員原本有 `200` 點，請把點數放入列表後傳入函式 `usePoint()`。函式內先印出兌換前點數，再扣除 `80` 點，最後印出兌換後點數。回到函式外後，也要印出目前剩餘點數。

## 提示

可以思考:

- 函式名稱可以改成 `usePoint`。
- 如果要扣點數，可以使用 `listPoint[0] -= 80`。
- 函式內修改列表內容後，函式外再印出 `listPoint[0]` 會看到什麼結果？

---

# 思考問題

1. 為什麼函式內修改 `listPoint[0]` 之後，函式外印出的點數也會改變？
2. 如果把 `listPoint[0] += 50` 改成 `listPoint = [170]`，函式外的 `listPoint[0]` 還會改變嗎？為什麼？
3. 如果一開始不使用列表，只傳入整數 `point`，函式內能不能直接改變函式外的 `point`？

---

# 建議查詢方向

學生可以搜尋:

1. Python list 如何修改元素
2. Python 函式參數 可變物件
3. Python list index 用法

