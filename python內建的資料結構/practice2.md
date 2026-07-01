# Python 課堂練習設計

## 今日教學重點

Tuple(元組)— 不可變性(immutable)與安全的資料解包(unpacking)

---

# 課堂範例回顧(學生剛才已練習)

## 原始程式

```python
# 台北 101 的經緯度座標 (緯度, 經度)
taipei_101_coords = (25.0339, 121.5645)

# 嘗試修改緯度值
try:
    taipei_101_coords[0] = 35.1234  # ❌ 嘗試修改
except TypeError as e:
    print("【修改失敗】提示:", e)  # 輸出: 'tuple' object does not support item assignment

# 正確且安全地解包讀取
lat, lon = taipei_101_coords
print(f"地標座標安全讀取 -> 緯度: {lat}, 經度: {lon}")
```

## 使用的 Python 技術

- tuple 初始化(小括號建立元組)
- tuple 的不可變性(嘗試用索引賦值會丟出 `TypeError`)
- `try / except` 攔截並顯示錯誤訊息
- tuple 解包(unpacking)一次取出多個值
- f-string 格式化輸出

## 學習目標

學生可以學會:

- 理解為什麼有些資料(固定不變的設定值)適合用 tuple 而不是 list
- 驗證 tuple 一旦建立就無法用索引方式修改內容
- 使用 `try / except` 攔截修改 tuple 時產生的 `TypeError`
- 使用 tuple 解包一次取出多個相關聯的值到不同變數

---

# 本次練習題目(全新題目,與課堂範例不同)

> 說明:以下是針對相同教學重點設計的「新題目」,情境與資料和課堂範例不同,但用到的 Python 語法一致。

## 題目敘述

小華買了一台新螢幕,它的原生解析度(寬, 高)是出廠就固定的規格,不應該被程式意外修改。請你設計一支程式,模擬讀取並保護這組螢幕解析度資料:

1. 建立一個 tuple `screen_resolution`,存放螢幕的「寬度」與「高度」,例如 `(1920, 1080)`。
2. 使用 `try / except` 嘗試把寬度改成 `2560`,並攔截修改失敗時丟出的 `TypeError`,印出提示訊息。
3. 使用 tuple 解包,把 `screen_resolution` 安全地拆成 `width` 與 `height` 兩個變數,並用 f-string 印出「螢幕規格 -> 寬度: OOO, 高度: OOO」。

## 與課堂範例的對應

- 沿用的語法/概念:tuple 初始化、tuple 不可變性、`try / except` 攔截 `TypeError`、tuple 解包、f-string 輸出
- 換掉的部分:情境從「地標經緯度座標」換成「螢幕解析度規格」,資料內容從(緯度, 經度)換成(寬度, 高度)

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。

```python
# 螢幕原生解析度 (寬度, 高度)
screen_resolution = (1920, 1080)

# 嘗試修改寬度值
try:
    # 請完成:嘗試把 screen_resolution 的第一個值(索引 0)改成 2560


except TypeError as e:
    print("【修改失敗】提示:", e)

# 正確且安全地解包讀取
# 請完成:把 screen_resolution 解包成 width 與 height 兩個變數


print(f"螢幕規格 -> 寬度: {width}, 高度: {height}")
```

學生需要完成:

1. 在 `try` 區塊中,用索引賦值的方式嘗試修改 `screen_resolution[0]` 為 `2560`
2. 用 tuple 解包語法 `width, height = screen_resolution` 一次取出寬度與高度
3. 確認 `except` 區塊與最後的 `print()` 能正確顯示攔截到的錯誤訊息與解包後的結果

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
# 螢幕原生解析度 (寬度, 高度)
screen_resolution = (1920, 1080)

# 嘗試修改寬度值
try:
    screen_resolution[0] = 2560  # ❌ 嘗試修改
except TypeError as e:
    print("【修改失敗】提示:", e)

# 正確且安全地解包讀取
width, height = screen_resolution
print(f"螢幕規格 -> 寬度: {width}, 高度: {height}")
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
# 步驟 1:建立 tuple 變數 screen_resolution,存放 (1920, 1080) 代表(寬度, 高度)


# 步驟 2:使用 try 區塊,嘗試把 screen_resolution 的索引 0(寬度)改成 2560


# 步驟 3:使用 except TypeError as e 攔截錯誤,並印出「【修改失敗】提示:」與錯誤訊息 e


# 步驟 4:使用 tuple 解包,把 screen_resolution 拆成 width 與 height 兩個變數


# 步驟 5:用 f-string 印出「螢幕規格 -> 寬度: {width}, 高度: {height}」

```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
# 步驟 1:建立 tuple 變數 screen_resolution,存放 (1920, 1080) 代表(寬度, 高度)
screen_resolution = (1920, 1080)

# 步驟 2:使用 try 區塊,嘗試把 screen_resolution 的索引 0(寬度)改成 2560
try:
    screen_resolution[0] = 2560

# 步驟 3:使用 except TypeError as e 攔截錯誤,並印出「【修改失敗】提示:」與錯誤訊息 e
except TypeError as e:
    print("【修改失敗】提示:", e)

# 步驟 4:使用 tuple 解包,把 screen_resolution 拆成 width 與 height 兩個變數
width, height = screen_resolution

# 步驟 5:用 f-string 印出「螢幕規格 -> 寬度: {width}, 高度: {height}」
print(f"螢幕規格 -> 寬度: {width}, 高度: {height}")
```

---

# 延伸挑戰題

## 題目

小華後來又買了一台印表機,規格資訊除了「寬度、高度」以外,還多了「型號名稱」這個文字資料,例如 `("EcoPrint-200", 210, 297)`(型號, 寬度mm, 高度mm)。請你建立這個 tuple,並用解包一次取出三個值分別存成 `model`、`width_mm`、`height_mm`,再印出完整規格說明;接著請你思考:如果解包時變數數量與 tuple 元素個數「對不上」(例如只寫兩個變數去接三個值),程式會發生什麼結果?請實際寫寫看並觀察錯誤訊息。

## 提示

可以思考:

- tuple 解包時,左邊變數的「數量」必須和右邊 tuple 的「元素個數」相同,否則會發生什麼錯誤?
- 型號名稱是文字(字串),寬度高度是數字,tuple 可以同時存放不同型別的資料嗎?
- 這種錯誤和修改 tuple 內容時的 `TypeError` 是同一種錯誤嗎?

---

# 思考問題

1. 這個情境為什麼要用 tuple 存放螢幕解析度,而不是用 list?如果改用 list,程式在「保護資料不被修改」這件事上會有什麼差異?
2. `try / except` 攔截的是「修改 tuple 失敗」這件事,如果拿掉 `try / except` 直接執行 `screen_resolution[0] = 2560`,程式會發生什麼結果?
3. tuple 解包 `width, height = screen_resolution` 和直接用索引寫 `width = screen_resolution[0]`、`height = screen_resolution[1]` 兩種寫法,結果一樣嗎?哪一種比較適合這個情境?為什麼?

---

# 建議查詢方向

學生可以搜尋:

1. 搜尋 Python tuple 與 list 的差異(可變 vs 不可變)
2. 搜尋 Python tuple 解包(unpacking)變數數量不符時會發生什麼錯誤
3. 搜尋 Python 為什麼要用 tuple 儲存固定不變的設定值或座標資料

