# Python 課堂練習設計

## 今日教學重點

Python 檔案存取(讀取檔案、逐行處理、篩選資料、排序、寫入新檔案)

---

# 課堂範例回顧(學生剛才已練習)

## 原始程式

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

## 使用的 Python 技術

- `with open(...) as f:` 檔案存取語法
- `readlines()` 逐行讀取
- `for` 迴圈
- `strip()` 去除頭尾空白與換行
- `startswith()` 判斷字串開頭
- `if not line or ...:` 條件判斷(空字串與註解行判斷)
- `list.append()`
- `list.sort()`
- `'\n'.join(list)`
- 檔案寫入(`'w'` 模式)

## 學習目標

學生可以學會:

- 使用 `with open()` 安全地開啟與關閉檔案
- 逐行讀取檔案內容,並用 `strip()`、`startswith()` 篩選出需要的資料
- 將整理後的資料排序,並寫入一個新的檔案

---

# 本次練習題目(全新題目,與課堂範例不同)

> 說明:以下是針對相同教學重點設計的「新題目」,情境與資料和課堂範例不同,但用到的 Python 語法一致。

## 題目敘述

老師手上有一份水果庫存清單檔案 `fruit.txt`,內容像這樣:

```
蘋果
;以下是本週新進貨品項
香蕉
芭樂

;缺貨中,暫不列入
奇異果
葡萄
```

檔案中有些行是空白行,有些行是以分號 `;` 開頭的說明文字(不是真正的水果資料),必須排除。

請寫一支程式:

1. 讀取 `fruit.txt`
2. 排除空行,以及以 `;` 開頭的說明行
3. 把剩下的水果名稱依「筆劃/字母」排序(使用 `sort()` 即可,不用額外處理)
4. 把排序後的結果寫入新檔案 `sorted-fruit.txt`,每個水果一行
5. 印出「整理完成！結果已儲存至 sorted-fruit.txt」

## 與課堂範例的對應

- 沿用的語法/概念:`with open()`、`readlines()`、`strip()`、`startswith()`、空行判斷、`list.sort()`、`'\n'.join()`、寫入新檔案
- 換掉的部分:資料情境從「一般清單資料 + `#` 註解」改成「水果庫存清單 + `;` 說明行」,檔名與變數名稱也不同

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。

```python
fruit_list = []

# 讀取 fruit.txt，排除以 ; 開頭的說明行與空行
with open('fruit.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = # 請完成:去除頭尾空白與換行

        # 請完成:如果是空行，或是以 ; 開頭，就跳過這一行
        if # 請完成:
            continue

        fruit_list.append(line)

# 請完成:將 fruit_list 排序

# 將結果重新寫入新檔案
with open('sorted-fruit.txt', 'w', encoding='utf-8') as out_f:
    # 請完成:把 fruit_list 用換行符號連接後寫入 out_f

print("整理完成！結果已儲存至 sorted-fruit.txt")
```

學生需要完成:

1. 用 `strip()` 去除每行頭尾的空白與換行
2. 寫出判斷空行與 `;` 開頭說明行的條件式
3. 呼叫 `sort()` 排序,以及用 `join()` 組合字串後寫入檔案

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
fruit_list = []

# 讀取 fruit.txt，排除以 ; 開頭的說明行與空行
with open('fruit.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()

        # 跳過空行與說明行
        if not line or line.startswith(';'):
            continue

        fruit_list.append(line)

fruit_list.sort()

# 將結果重新寫入新檔案
with open('sorted-fruit.txt', 'w', encoding='utf-8') as out_f:
    out_f.write('\n'.join(fruit_list))

print("整理完成！結果已儲存至 sorted-fruit.txt")
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
# 步驟 1:建立一個空串列 fruit_list，用來存放整理後的水果名稱


# 步驟 2:使用 with open() 開啟 fruit.txt（讀取模式，編碼 utf-8）


    # 步驟 3:用 for 迴圈讀取檔案中的每一行（readlines）


        # 步驟 4:去除這一行頭尾的空白與換行


        # 步驟 5:如果是空行，或是以 ; 開頭的說明行，就跳過這一行（continue）


        # 步驟 6:把整理好的水果名稱加入 fruit_list


# 步驟 7:將 fruit_list 排序


# 步驟 8:使用 with open() 開啟 sorted-fruit.txt（寫入模式，編碼 utf-8）


    # 步驟 9:用 join() 把 fruit_list 的每個項目以換行符號組合，寫入檔案


# 步驟 10:印出「整理完成！結果已儲存至 sorted-fruit.txt」

```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
# 步驟 1:建立一個空串列 fruit_list，用來存放整理後的水果名稱
fruit_list = []

# 步驟 2:使用 with open() 開啟 fruit.txt（讀取模式，編碼 utf-8）
with open('fruit.txt', 'r', encoding='utf-8') as f:
    # 步驟 3:用 for 迴圈讀取檔案中的每一行（readlines）
    for line in f.readlines():
        # 步驟 4:去除這一行頭尾的空白與換行
        line = line.strip()
        # 步驟 5:如果是空行，或是以 ; 開頭的說明行，就跳過這一行（continue）
        if not line or line.startswith(';'):
            continue
        # 步驟 6:把整理好的水果名稱加入 fruit_list
        fruit_list.append(line)

# 步驟 7:將 fruit_list 排序
fruit_list.sort()

# 步驟 8:使用 with open() 開啟 sorted-fruit.txt（寫入模式，編碼 utf-8）
with open('sorted-fruit.txt', 'w', encoding='utf-8') as out_f:
    # 步驟 9:用 join() 把 fruit_list 的每個項目以換行符號組合，寫入檔案
    out_f.write('\n'.join(fruit_list))

# 步驟 10:印出「整理完成！結果已儲存至 sorted-fruit.txt」
print("整理完成！結果已儲存至 sorted-fruit.txt")
```

---

# 延伸挑戰題

## 題目

老師發現 `fruit.txt` 裡面,同一種水果可能重複出現好幾次(例如「蘋果」出現了 2 次)。請修改程式,讓 `sorted-fruit.txt` 裡的水果名稱**不重複**,並且在檔案最前面多寫一行,標明「總共 N 種水果」(N 為不重複的水果數量)。

## 提示

可以思考:

- 要如何檢查一個項目是否已經在串列裡了?(也可以想想 `set` 這個資料型態能不能幫上忙)
- 如果要在寫入的內容最前面加一行文字,`join()` 之後的字串要怎麼組合?
- 排序要在去重複之前做,還是之後做,結果會不會不一樣?

---

# 思考問題

1. 如果把 `if not line or line.startswith(';'):` 改成 `if not line and line.startswith(';'):`(把 `or` 改成 `and`),程式的篩選結果會有什麼不同?為什麼?
2. 這支程式用 `'w'` 模式開啟輸出檔案,如果這支程式被執行兩次,`sorted-fruit.txt` 的內容會變成什麼樣子?如果改成 `'a'` 模式呢?
3. 除了用 `readlines()` 搭配 `for` 迴圈,還有沒有其他方式可以逐行讀取檔案?這些方式在寫法或效能上有什麼不同?

---

# 建議查詢方向

學生可以搜尋:

1. Python `open()` 檔案模式 `r`、`w`、`a` 的差異
2. Python `strip()` 與 `startswith()` 用法
3. Python 如何用 `set` 或其他方法移除串列中重複的資料

