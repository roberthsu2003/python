# Python 課堂練習設計

## 今日教學重點

進階參數控制:僅限位置與僅限關鍵字參數(`/` 與 `*`)

---

# 課堂範例回顧(學生剛才已練習)

## 原始程式

```python
def configure_user(name, age, /, country="台灣", *, role="Member", debug=False):
    """
    name, age     -> 位於 / 左側,必須是位置引數。
    country       -> 夾在 / 與 * 之間,可使用位置或關鍵字傳遞。
    role, debug   -> 位於 * 右側,必須是關鍵字引數。
    """
    print(f"User: {name}, Age: {age}, Country: {country}, Role: {role}, Debug: {debug}")

# 1. 正確呼叫
configure_user("Alice", 25, "日本", role="Admin", debug=True)

# 2. ❌ 錯誤:對 name 或 age 使用關鍵字傳遞 (拋出 TypeError)
# configure_user(name="Alice", age=25, role="Admin")

# 3. ❌ 錯誤:對 role 使用位置傳遞 (拋出 TypeError)
# configure_user("Alice", 25, "日本", "Admin")
```

## 使用的 Python 技術

- function 定義(def)
- 預設參數值
- 僅限位置參數符號 `/`
- 僅限關鍵字參數符號 `*`
- 位置引數與關鍵字引數的呼叫方式
- f-string

## 學習目標

學生可以學會:

- 理解 `/` 左側的參數只能用位置方式傳入,不能用參數名稱
- 理解 `*` 右側的參數只能用參數名稱(關鍵字)傳入,不能用位置
- 能設計自己的 function,依據需求把參數分成「僅限位置」「一般」「僅限關鍵字」三種區塊

---

# 本次練習題目(全新題目,與課堂範例不同)

> 說明:以下是針對相同教學重點設計的「新題目」,情境與資料和課堂範例不同,但用到的 Python 語法一致。

## 題目敘述

請設計一個「會議室預約」的 function,名稱為 `schedule_meeting`。規則如下:

- `title`(會議主題)與 `duration_minutes`(會議時長,分鐘)這兩個參數,**必須用位置方式傳入**(放在 `/` 左側)
- `room`(會議室名稱,預設 `"A"`)夾在中間,可以用位置或關鍵字方式傳入
- `recurring`(是否為週期性會議,預設 `False`)與 `priority`(優先等級,預設 `"normal"`)這兩個參數,**必須用關鍵字方式傳入**(放在 `*` 右側)

呼叫時要示範:一次正確呼叫、並用註解標示出兩種會出現 `TypeError` 的錯誤呼叫方式(不要真的執行,用 `#` 註解掉)。

## 與課堂範例的對應

- 沿用的語法/概念:`/` 僅限位置參數、`*` 僅限關鍵字參數、預設參數值、f-string 輸出、以註解標示錯誤呼叫範例
- 換掉的部分:情境從「設定使用者資料」換成「會議室預約」,參數名稱、數量與型別(新增布林值 `recurring`)不同

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。

```python
def schedule_meeting(title, duration_minutes  # 請完成:在這裡加上 / 符號,讓 title 與 duration_minutes 變成僅限位置參數
                      room="A"  # 請完成:在這裡加上 * 符號,讓後面的參數變成僅限關鍵字參數
                      recurring=False, priority="normal"):
    """
    title, duration_minutes -> 僅限位置參數
    room                    -> 一般參數(可位置可關鍵字)
    recurring, priority     -> 僅限關鍵字參數
    """
    print(f"會議主題: {title}, 時長: {duration_minutes}分鐘, 會議室: {room}, 週期性: {recurring}, 優先等級: {priority}")


# 1. 正確呼叫
# 請完成:呼叫 schedule_meeting,title 與 duration_minutes 用位置傳入,
#         room 用位置或關鍵字皆可,recurring 與 priority 必須用關鍵字傳入


# 2. ❌ 錯誤:對 title 或 duration_minutes 使用關鍵字傳遞 (拋出 TypeError)
# 請完成:寫出一行示範這種錯誤呼叫的程式碼(記得用 # 註解掉,不要真的執行)


# 3. ❌ 錯誤:對 recurring 使用位置傳遞 (拋出 TypeError)
# 請完成:寫出一行示範這種錯誤呼叫的程式碼(記得用 # 註解掉,不要真的執行)
```

學生需要完成:

1. 在正確的位置加上 `/` 與 `*` 符號
2. 寫出一次正確的呼叫方式
3. 用註解寫出兩種會產生 `TypeError` 的錯誤呼叫範例

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
def schedule_meeting(title, duration_minutes, /, room="A", *, recurring=False, priority="normal"):
    """
    title, duration_minutes -> 僅限位置參數
    room                    -> 一般參數(可位置可關鍵字)
    recurring, priority     -> 僅限關鍵字參數
    """
    print(f"會議主題: {title}, 時長: {duration_minutes}分鐘, 會議室: {room}, 週期性: {recurring}, 優先等級: {priority}")


# 1. 正確呼叫
schedule_meeting("週會", 30, "302", recurring=True, priority="high")

# 2. ❌ 錯誤:對 title 或 duration_minutes 使用關鍵字傳遞 (拋出 TypeError)
# schedule_meeting(title="週會", duration_minutes=30, recurring=True)

# 3. ❌ 錯誤:對 recurring 使用位置傳遞 (拋出 TypeError)
# schedule_meeting("週會", 30, "302", True, "high")
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
# 步驟 1:定義一個名稱為 schedule_meeting 的 function
#         參數依序為:title、duration_minutes(這兩個要設為僅限位置參數)、
#                     room(預設 "A",一般參數)、
#                     recurring(預設 False)、priority(預設 "normal")(這兩個要設為僅限關鍵字參數)
#         記得在正確位置加上 / 與 * 符號


    # 步驟 2:撰寫 Docstring,說明哪些參數是僅限位置、哪些是僅限關鍵字


    # 步驟 3:用 f-string 印出 title、duration_minutes、room、recurring、priority 五個值


# 步驟 4:寫一次正確的呼叫,title 與 duration_minutes 用位置傳入,recurring 與 priority 用關鍵字傳入


# 步驟 5:用註解寫出一種「對僅限位置參數使用關鍵字傳遞」而導致 TypeError 的錯誤呼叫範例(不要真的執行)


# 步驟 6:用註解寫出一種「對僅限關鍵字參數使用位置傳遞」而導致 TypeError 的錯誤呼叫範例(不要真的執行)

```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
# 步驟 1:定義一個名稱為 schedule_meeting 的 function
#         參數依序為:title、duration_minutes(這兩個要設為僅限位置參數)、
#                     room(預設 "A",一般參數)、
#                     recurring(預設 False)、priority(預設 "normal")(這兩個要設為僅限關鍵字參數)
#         記得在正確位置加上 / 與 * 符號
def schedule_meeting(title, duration_minutes, /, room="A", *, recurring=False, priority="normal"):
    # 步驟 2:撰寫 Docstring,說明哪些參數是僅限位置、哪些是僅限關鍵字
    """
    title, duration_minutes -> 僅限位置參數
    room                    -> 一般參數(可位置可關鍵字)
    recurring, priority     -> 僅限關鍵字參數
    """
    # 步驟 3:用 f-string 印出 title、duration_minutes、room、recurring、priority 五個值
    print(f"會議主題: {title}, 時長: {duration_minutes}分鐘, 會議室: {room}, 週期性: {recurring}, 優先等級: {priority}")


# 步驟 4:寫一次正確的呼叫,title 與 duration_minutes 用位置傳入,recurring 與 priority 用關鍵字傳入
schedule_meeting("週會", 30, "302", recurring=True, priority="high")

# 步驟 5:用註解寫出一種「對僅限位置參數使用關鍵字傳遞」而導致 TypeError 的錯誤呼叫範例(不要真的執行)
# schedule_meeting(title="週會", duration_minutes=30, recurring=True)

# 步驟 6:用註解寫出一種「對僅限關鍵字參數使用位置傳遞」而導致 TypeError 的錯誤呼叫範例(不要真的執行)
# schedule_meeting("週會", 30, "302", True, "high")
```

---

# 延伸挑戰題

## 題目

請設計一個「線上訂購飲料」的 function,名稱為 `order_drink`。規則如下:

- `drink_name`(飲品名稱)與 `size`(杯型,例如 "M"、"L")必須是**僅限位置參數**
- `sugar`(糖度,預設 `"正常"`)與 `ice`(冰塊,預設 `"正常"`)為一般參數(可位置可關鍵字)
- `toppings`(加料項目,使用 `*toppings` 讓使用者可以傳入 0 到多個加料,例如 `"珍珠"`、`"椰果"`)與 `member_discount`(是否會員折扣,預設 `False`,**僅限關鍵字**)放在最後

提示:這一題會用到 `*args`(不定長度參數,例如 `*toppings`)和「僅限關鍵字」的概念一起搭配,思考看看 `*toppings` 出現之後,後面的參數是不是自動就變成僅限關鍵字了,還需不需要再額外加一個單獨的 `*`。

## 提示

可以思考:

- `*toppings` 本身能不能同時也順便達到「後面參數僅限關鍵字」的效果?跟單獨寫一個 `*` 有什麼不同?
- 如果 `toppings` 想要限制使用者最多只能加 3 種加料,程式要怎麼修改?
- 呼叫這個 function 時,加料項目要放在呼叫的哪個位置?

---

# 思考問題

1. 為什麼 Python 要特別設計 `/` 和 `*` 這兩個符號,讓某些參數「只能用位置」或「只能用關鍵字」?這對「函式設計者」和「函式使用者」分別有什麼好處?
2. 如果拿掉範例中的 `/`,原本必須用位置傳入的 `title` 和 `duration_minutes`,現在還能不能用關鍵字傳入?這會對呼叫者的使用方式造成什麼影響?
3. 觀察課堂範例與本次練習題目,`/` 和 `*` 中間的參數(如 `country`、`room`)有什麼共同特性?為什麼 Python 允許它們「兩種方式都可以」?

---

# 建議查詢方向

學生可以搜尋:

1. Python 僅限位置參數 positional-only parameters 用法
2. Python 僅限關鍵字參數 keyword-only parameters 用法
3. Python function 參數 `/` 與 `*` 差異

