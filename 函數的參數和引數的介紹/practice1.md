# Python 課堂練習設計

## 今日教學重點

自訂 function 的三種引數呼叫方式：
- 引數位置呼叫（Positional Arguments）
- 引數名稱呼叫（Keyword Arguments）
- 混合呼叫（Mixed Arguments）

---

# 課堂範例回顧(學生剛才已練習)

## 原始程式

```python
def introduce_person(name, age, city="台北", hobby="閱讀"):
    """
    介紹一個人的基本資訊
    
    參數:
    name: 姓名 (必需參數)
    age: 年齡 (必需參數)
    city: 居住城市 (預設值: "台北")
    hobby: 興趣 (預設值: "閱讀")
    """
    return f"大家好，我是{name}，今年{age}歲，住在{city}，我喜歡{hobby}。"

print("=== 1. 引數值呼叫 (Positional Arguments) ===")
print("按照參數定義的順序傳遞值")
result1 = introduce_person("小明", 25, "台中", "游泳")
print(result1)
print()

print("=== 2. 引數名稱呼叫 (Keyword Arguments) ===")  
print("使用參數名稱來指定值，順序可以不同")
result2 = introduce_person(hobby="畫畫", city="高雄", age=30, name="小華")
print(result2)
print()

print("=== 3. 混合呼叫 (Mixed Arguments) ===")
print("位置參數必須在前，關鍵字參數在後")
result3 = introduce_person("小美", 28, hobby="旅遊")  # name, age用位置參數，hobby用關鍵字參數
print(result3)
print()
```

## 使用的 Python 技術

- 自訂 function（`def`）
- 必需參數與預設參數（`=` 給預設值）
- docstring 說明文件
- f-string 字串格式化
- `return` 回傳值
- 函式呼叫時的三種引數傳遞方式

## 學習目標

學生可以學會:

- 分辨「必需參數」與「有預設值的參數」的差異
- 使用位置呼叫、關鍵字呼叫、混合呼叫三種方式呼叫同一個 function
- 理解混合呼叫時「位置參數一定要放在關鍵字參數前面」的規則

---

# 本次練習題目(全新題目,與課堂範例不同)

> 說明:以下是針對相同教學重點設計的「新題目」,情境與資料和課堂範例不同,但用到的 Python 語法一致。

## 題目敘述

請設計一個手搖飲料店的「訂單建立」功能。請撰寫一個 `order_drink` function，接收顧客姓名與杯型大小（必需參數），以及甜度與冰塊量（有預設值的參數，預設皆為「正常」），function 需回傳一句完整的訂單說明文字。

接著請分別用「位置呼叫」「關鍵字呼叫」「混合呼叫」三種方式呼叫這個 function，建立三筆不同的訂單，並將結果印出。

## 與課堂範例的對應

- 沿用的語法/概念:自訂 function、必需參數、預設參數、docstring、f-string、`return`、三種引數呼叫方式
- 換掉的部分:情境從「自我介紹」換成「手搖飲料訂購」；參數從姓名/年齡/城市/興趣換成顧客姓名/杯型/甜度/冰塊量

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。

```python
def order_drink(customer_name, cup_size, sugar_level="正常糖", ice_level="正常冰"):
    """
    建立手搖飲料的訂單資訊
    
    參數:
    customer_name: 顧客姓名 (必需參數)
    cup_size: 杯型大小 (必需參數)
    sugar_level: 甜度 (預設值: "正常糖")
    ice_level: 冰塊量 (預設值: "正常冰")
    """
    # 請完成: 回傳一句訂單說明文字,格式參考:
    # "訂單成立：小明訂了一杯大杯，正常糖、正常冰。"
    # 請完成


print("=== 1. 引數位置呼叫 (Positional Arguments) ===")
print("按照參數定義的順序傳遞值")
# 請完成: 使用「位置呼叫」建立一筆訂單,姓名"小明",杯型"大杯",甜度"半糖",冰塊"少冰"
result1 = 
print(result1)
print()

print("=== 2. 引數名稱呼叫 (Keyword Arguments) ===")
print("使用參數名稱來指定值，順序可以不同")
# 請完成: 使用「關鍵字呼叫」建立一筆訂單,姓名"小華",杯型"中杯",甜度"無糖",冰塊"去冰",引數順序故意打亂
result2 = 
print(result2)
print()

print("=== 3. 混合呼叫 (Mixed Arguments) ===")
print("位置參數必須在前，關鍵字參數在後")
# 請完成: 姓名"小美"、杯型"小杯"用位置參數,甜度"微糖"用關鍵字參數,冰塊量使用預設值
result3 = 
print(result3)
print()
```

學生需要完成:

1. 補完 `order_drink` function 的 `return` 內容，組出正確的訂單說明字串
2. 用位置呼叫方式建立 `result1`
3. 用關鍵字呼叫、混合呼叫方式分別建立 `result2`、`result3`

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
def order_drink(customer_name, cup_size, sugar_level="正常糖", ice_level="正常冰"):
    """
    建立手搖飲料的訂單資訊
    
    參數:
    customer_name: 顧客姓名 (必需參數)
    cup_size: 杯型大小 (必需參數)
    sugar_level: 甜度 (預設值: "正常糖")
    ice_level: 冰塊量 (預設值: "正常冰")
    """
    return f"訂單成立：{customer_name}訂了一杯{cup_size}，{sugar_level}、{ice_level}。"


print("=== 1. 引數位置呼叫 (Positional Arguments) ===")
print("按照參數定義的順序傳遞值")
result1 = order_drink("小明", "大杯", "半糖", "少冰")
print(result1)
print()

print("=== 2. 引數名稱呼叫 (Keyword Arguments) ===")
print("使用參數名稱來指定值，順序可以不同")
result2 = order_drink(ice_level="去冰", sugar_level="無糖", cup_size="中杯", customer_name="小華")
print(result2)
print()

print("=== 3. 混合呼叫 (Mixed Arguments) ===")
print("位置參數必須在前，關鍵字參數在後")
result3 = order_drink("小美", "小杯", sugar_level="微糖")
print(result3)
print()
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
# 步驟 1: 定義 order_drink function
#         必需參數: customer_name, cup_size
#         預設參數: sugar_level 預設 "正常糖", ice_level 預設 "正常冰"
#         並加上 docstring 說明每個參數用途


# 步驟 2: 在 function 內,用 f-string 組出訂單說明文字並 return
#         格式參考: "訂單成立：小明訂了一杯大杯，正常糖、正常冰。"


# 步驟 3: 印出標題「1. 引數位置呼叫」,並說明按照順序傳值


# 步驟 4: 使用「位置呼叫」建立一筆訂單(姓名"小明", 杯型"大杯", 甜度"半糖", 冰塊"少冰"),
#         結果存到 result1 並印出


# 步驟 5: 印出標題「2. 引數名稱呼叫」,並說明可用參數名稱指定值、順序可不同


# 步驟 6: 使用「關鍵字呼叫」建立一筆訂單(姓名"小華", 杯型"中杯", 甜度"無糖", 冰塊"去冰"),
#         刻意打亂引數順序,結果存到 result2 並印出


# 步驟 7: 印出標題「3. 混合呼叫」,並說明位置參數要放在關鍵字參數前面


# 步驟 8: 使用「混合呼叫」建立一筆訂單:姓名"小美"、杯型"小杯"用位置參數,
#         甜度"微糖"用關鍵字參數,冰塊量使用預設值,結果存到 result3 並印出

```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
# 步驟 1: 定義 order_drink function
#         必需參數: customer_name, cup_size
#         預設參數: sugar_level 預設 "正常糖", ice_level 預設 "正常冰"
#         並加上 docstring 說明每個參數用途
def order_drink(customer_name, cup_size, sugar_level="正常糖", ice_level="正常冰"):
    """
    建立手搖飲料的訂單資訊
    
    參數:
    customer_name: 顧客姓名 (必需參數)
    cup_size: 杯型大小 (必需參數)
    sugar_level: 甜度 (預設值: "正常糖")
    ice_level: 冰塊量 (預設值: "正常冰")
    """
    # 步驟 2: 在 function 內,用 f-string 組出訂單說明文字並 return
    #         格式參考: "訂單成立：小明訂了一杯大杯，正常糖、正常冰。"
    return f"訂單成立：{customer_name}訂了一杯{cup_size}，{sugar_level}、{ice_level}。"


# 步驟 3: 印出標題「1. 引數位置呼叫」,並說明按照順序傳值
print("=== 1. 引數位置呼叫 (Positional Arguments) ===")
print("按照參數定義的順序傳遞值")

# 步驟 4: 使用「位置呼叫」建立一筆訂單(姓名"小明", 杯型"大杯", 甜度"半糖", 冰塊"少冰"),
#         結果存到 result1 並印出
result1 = order_drink("小明", "大杯", "半糖", "少冰")
print(result1)
print()

# 步驟 5: 印出標題「2. 引數名稱呼叫」,並說明可用參數名稱指定值、順序可不同
print("=== 2. 引數名稱呼叫 (Keyword Arguments) ===")
print("使用參數名稱來指定值，順序可以不同")

# 步驟 6: 使用「關鍵字呼叫」建立一筆訂單(姓名"小華", 杯型"中杯", 甜度"無糖", 冰塊"去冰"),
#         刻意打亂引數順序,結果存到 result2 並印出
result2 = order_drink(ice_level="去冰", sugar_level="無糖", cup_size="中杯", customer_name="小華")
print(result2)
print()

# 步驟 7: 印出標題「3. 混合呼叫」,並說明位置參數要放在關鍵字參數前面
print("=== 3. 混合呼叫 (Mixed Arguments) ===")
print("位置參數必須在前，關鍵字參數在後")

# 步驟 8: 使用「混合呼叫」建立一筆訂單:姓名"小美"、杯型"小杯"用位置參數,
#         甜度"微糖"用關鍵字參數,冰塊量使用預設值,結果存到 result3 並印出
result3 = order_drink("小美", "小杯", sugar_level="微糖")
print(result3)
print()
```

---

# 延伸挑戰題

## 題目

老闆想在訂單中加入「外帶袋」選項：新增一個參數 `bag`，預設值為 `False`（表示不需要外帶袋）。當顧客需要外帶袋時（`bag=True`），訂單說明文字最後要多加一句「（需要外帶袋）」。請修改 `order_drink` function，並用三種呼叫方式（位置、關鍵字、混合）各建立一筆需要外帶袋的訂單。

## 提示

可以思考:

- 布林值 `True` / `False` 也可以當作參數的預設值
- 在 f-string 裡如何依條件加上不同的文字（可以想想 `if` 判斷或字串串接）
- 新參數 `bag` 應該放在參數列表的哪個位置比較合理？為什麼？

---

# 思考問題

1. 如果呼叫 `order_drink("小明")`，只給一個引數，程式會發生什麼事？為什麼會這樣？
2. 混合呼叫時，如果把關鍵字引數寫在位置引數前面（例如 `order_drink(sugar_level="半糖", "小明", "大杯")`），會發生什麼事？這說明了什麼規則？
3. 為什麼 `sugar_level` 和 `ice_level` 適合設計成有預設值的參數，而 `customer_name` 和 `cup_size` 不適合？

---

# 建議查詢方向

學生可以搜尋:

1. Python function 必需參數與預設參數的差別
2. Python 關鍵字引數 (keyword arguments) 使用規則
3. Python 混合使用位置引數與關鍵字引數時的順序限制

---
