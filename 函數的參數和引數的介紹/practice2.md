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
def calculate_total(price, quantity, discount=0, tax_rate=0.05):
    """
    計算商品總價
    
    參數:
    price: 單價
    quantity: 數量  
    discount: 折扣金額 (預設值: 0)
    tax_rate: 稅率 (預設值: 0.05)
    """
    subtotal = price * quantity - discount
    total = subtotal * (1 + tax_rate)
    return total

print("=== 購物計算範例 ===")
print("1. 引數值呼叫:")
total1 = calculate_total(100, 3, 50, 0.1)
print(f"總價: ${total1:.2f}")

print("\n2. 引數名稱呼叫:")
total2 = calculate_total(tax_rate=0.08, discount=20, quantity=2, price=150)
print(f"總價: ${total2:.2f}")

print("\n3. 混合呼叫:")
total3 = calculate_total(120, 4, tax_rate=0.07)  # price, quantity用位置參數
print(f"總價: ${total3:.2f}")
```

## 使用的 Python 技術

- 自訂 function（`def`）
- 必需參數與預設參數（`=` 給預設值）
- docstring 說明文件
- 數學運算（乘法、減法、加法、百分比計算）
- f-string 字串格式化（含 `:.2f` 數字格式化）
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

請設計一個停車場的「停車費計算」功能。請撰寫一個 `calculate_parking_fee` function，接收每小時費率與停車時數（必需參數），以及折扣金額與服務費（有預設值的參數，折扣預設 0 元、服務費預設 10 元），function 需計算並回傳停車總費用（總費用 = 每小時費率 × 停車時數 − 折扣金額 + 服務費）。

接著請分別用「位置呼叫」「關鍵字呼叫」「混合呼叫」三種方式呼叫這個 function，計算三筆不同的停車費用，並將結果印出（結果請顯示到小數點後 2 位）。

## 與課堂範例的對應

- 沿用的語法/概念:自訂 function、必需參數、預設參數、docstring、數學運算、f-string 數字格式化、`return`、三種引數呼叫方式
- 換掉的部分:情境從「購物總價計算」換成「停車費計算」；參數從單價/數量/折扣/稅率換成費率/時數/折扣/服務費；總價公式也不同（原本是乘上稅率，這次是加上固定服務費）

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。

```python
def calculate_parking_fee(hourly_rate, hours, discount=0, service_fee=10):
    """
    計算停車費用
    
    參數:
    hourly_rate: 每小時費率
    hours: 停車時數
    discount: 折扣金額 (預設值: 0)
    service_fee: 服務費 (預設值: 10)
    """
    # 請完成: 計算 subtotal = 每小時費率 * 停車時數 - 折扣金額
    subtotal = 
    # 請完成: 計算 total = subtotal + 服務費,並 return total
    total = 


print("=== 停車費計算範例 ===")
print("1. 引數位置呼叫:")
# 請完成: 使用「位置呼叫」計算費率30、時數5小時、折扣20、服務費15的停車費,存到 fee1
fee1 = 
print(f"總費用: ${fee1:.2f}")

print("\n2. 引數名稱呼叫:")
# 請完成: 使用「關鍵字呼叫」計算費率25、時數8小時、服務費20、折扣10的停車費,存到 fee2,引數順序故意打亂
fee2 = 
print(f"總費用: ${fee2:.2f}")

print("\n3. 混合呼叫:")
# 請完成: 使用「混合呼叫」計算費率40、時數3小時用位置參數,服務費25用關鍵字參數,折扣使用預設值,存到 fee3
fee3 = 
print(f"總費用: ${fee3:.2f}")
```

學生需要完成:

1. 補完 `calculate_parking_fee` function 內的 `subtotal` 與 `total` 計算及 `return`
2. 用位置呼叫方式計算 `fee1`
3. 用關鍵字呼叫、混合呼叫方式分別計算 `fee2`、`fee3`

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
def calculate_parking_fee(hourly_rate, hours, discount=0, service_fee=10):
    """
    計算停車費用
    
    參數:
    hourly_rate: 每小時費率
    hours: 停車時數
    discount: 折扣金額 (預設值: 0)
    service_fee: 服務費 (預設值: 10)
    """
    subtotal = hourly_rate * hours - discount
    total = subtotal + service_fee
    return total


print("=== 停車費計算範例 ===")
print("1. 引數位置呼叫:")
fee1 = calculate_parking_fee(30, 5, 20, 15)
print(f"總費用: ${fee1:.2f}")

print("\n2. 引數名稱呼叫:")
fee2 = calculate_parking_fee(service_fee=20, discount=10, hours=8, hourly_rate=25)
print(f"總費用: ${fee2:.2f}")

print("\n3. 混合呼叫:")
fee3 = calculate_parking_fee(40, 3, service_fee=25)
print(f"總費用: ${fee3:.2f}")
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
# 步驟 1: 定義 calculate_parking_fee function
#         必需參數: hourly_rate, hours
#         預設參數: discount 預設 0, service_fee 預設 10
#         並加上 docstring 說明每個參數用途


# 步驟 2: 在 function 內計算 subtotal = hourly_rate * hours - discount


# 步驟 3: 計算 total = subtotal + service_fee,並 return total


# 步驟 4: 印出標題「停車費計算範例」


# 步驟 5: 印出「1. 引數位置呼叫:」


# 步驟 6: 使用「位置呼叫」計算費率30、時數5小時、折扣20、服務費15的停車費,
#         結果存到 fee1,並用 f-string 印出(小數點後2位)


# 步驟 7: 印出「2. 引數名稱呼叫:」


# 步驟 8: 使用「關鍵字呼叫」計算費率25、時數8小時、服務費20、折扣10的停車費,
#         刻意打亂引數順序,結果存到 fee2,並印出


# 步驟 9: 印出「3. 混合呼叫:」


# 步驟 10: 使用「混合呼叫」計算費率40、時數3小時用位置參數,
#          服務費25用關鍵字參數,折扣使用預設值,結果存到 fee3,並印出

```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
# 步驟 1: 定義 calculate_parking_fee function
#         必需參數: hourly_rate, hours
#         預設參數: discount 預設 0, service_fee 預設 10
#         並加上 docstring 說明每個參數用途
def calculate_parking_fee(hourly_rate, hours, discount=0, service_fee=10):
    """
    計算停車費用
    
    參數:
    hourly_rate: 每小時費率
    hours: 停車時數
    discount: 折扣金額 (預設值: 0)
    service_fee: 服務費 (預設值: 10)
    """
    # 步驟 2: 在 function 內計算 subtotal = hourly_rate * hours - discount
    subtotal = hourly_rate * hours - discount
    # 步驟 3: 計算 total = subtotal + service_fee,並 return total
    total = subtotal + service_fee
    return total


# 步驟 4: 印出標題「停車費計算範例」
print("=== 停車費計算範例 ===")

# 步驟 5: 印出「1. 引數位置呼叫:」
print("1. 引數位置呼叫:")

# 步驟 6: 使用「位置呼叫」計算費率30、時數5小時、折扣20、服務費15的停車費,
#         結果存到 fee1,並用 f-string 印出(小數點後2位)
fee1 = calculate_parking_fee(30, 5, 20, 15)
print(f"總費用: ${fee1:.2f}")

# 步驟 7: 印出「2. 引數名稱呼叫:」
print("\n2. 引數名稱呼叫:")

# 步驟 8: 使用「關鍵字呼叫」計算費率25、時數8小時、服務費20、折扣10的停車費,
#         刻意打亂引數順序,結果存到 fee2,並印出
fee2 = calculate_parking_fee(service_fee=20, discount=10, hours=8, hourly_rate=25)
print(f"總費用: ${fee2:.2f}")

# 步驟 9: 印出「3. 混合呼叫:」
print("\n3. 混合呼叫:")

# 步驟 10: 使用「混合呼叫」計算費率40、時數3小時用位置參數,
#          服務費25用關鍵字參數,折扣使用預設值,結果存到 fee3,並印出
fee3 = calculate_parking_fee(40, 3, service_fee=25)
print(f"總費用: ${fee3:.2f}")
```

---

# 延伸挑戰題

## 題目

停車場想推出「過夜加成」：新增一個參數 `overnight`，預設值為 `False`（表示不是過夜停車）。當 `overnight=True` 時，總費用要再乘上 1.2 倍（加收 20% 過夜費）。請修改 `calculate_parking_fee` function，並用三種呼叫方式（位置、關鍵字、混合）各計算一筆過夜停車的費用。

## 提示

可以思考:

- 布林值 `True` / `False` 也可以當作參數的預設值
- 如何在計算 `total` 之後,依 `overnight` 的值決定要不要再乘上 1.2（可以想想 `if` 判斷）
- 新參數 `overnight` 應該放在參數列表的哪個位置比較合理？為什麼？

---

# 思考問題

1. 如果呼叫 `calculate_parking_fee(30)`，只給一個引數，程式會發生什麼事？為什麼會這樣？
2. 混合呼叫時，如果寫成 `calculate_parking_fee(discount=10, 30, 5)`，把關鍵字引數寫在位置引數前面，會發生什麼事？這說明了什麼規則？
3. 為什麼 `discount` 和 `service_fee` 適合設計成有預設值的參數，而 `hourly_rate` 和 `hours` 不適合？

---

# 建議查詢方向

學生可以搜尋:

1. Python function 必需參數與預設參數的差別
2. Python 關鍵字引數 (keyword arguments) 使用規則
3. Python 混合使用位置引數與關鍵字引數時的順序限制

