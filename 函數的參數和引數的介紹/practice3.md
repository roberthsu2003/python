# Python 課堂練習設計

## 今日教學重點

function 的說明文件(Docstrings)

---

# 課堂範例回顧(學生剛才已練習)

## 原始程式

```python
def calculate_triangle_area(base, height):
    """
    計算直角三角形的面積。
    
    參數:
    base (float): 三角形的底邊長度 (公分)
    height (float): 三角形的高 (公分)
    
    回傳:
    float: 計算出的三角形面積 (平方公分)
    """
    return (base * height) / 2


print(calculate_triangle_area.__doc__)
help(calculate_triangle_area)
```

## 使用的 Python 技術

- function 定義(def)
- 參數(parameters)
- return
- Docstring(三個雙引號 `"""..."""`)
- `__doc__` 屬性
- `help()` 內建函式

## 學習目標

學生可以學會:

- 知道 Docstring 要放在 function 內的第一行
- 能撰寫包含「功能說明、參數說明、回傳說明」三個部分的 Docstring
- 知道可以透過 `函式名稱.__doc__` 或 `help(函式名稱)` 查看說明文件

---

# 本次練習題目(全新題目,與課堂範例不同)

> 說明:以下是針對相同教學重點設計的「新題目」,情境與資料和課堂範例不同,但用到的 Python 語法一致。

## 題目敘述

請設計一個計算「BMI 身體質量指數」的 function,名稱為 `calculate_bmi`,需要兩個參數:體重(公斤)與身高(公尺)。這個 function 要有一份**完整的 Docstring**,內容需包含「功能說明」「參數說明」「回傳說明」三個部分。撰寫完成後,分別用 `print(calculate_bmi.__doc__)` 與 `help(calculate_bmi)` 印出說明文件來確認結果。

BMI 計算公式為:BMI = 體重(公斤) ÷ 身高(公尺)²

## 與課堂範例的對應

- 沿用的語法/概念:function 定義、參數、return、Docstring 三段式寫法(功能/參數/回傳)、`__doc__`、`help()`
- 換掉的部分:情境從「三角形面積」換成「BMI 計算」,參數名稱與計算公式不同

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。程式的計算邏輯已經寫好,你要做的是**把 Docstring 補完整**。

```python
def calculate_bmi(weight, height):
    """
    # 請完成:寫一句話說明這個 function 的功能

    參數:
    # 請完成:說明 weight 這個參數(型別、代表意義、單位)
    # 請完成:說明 height 這個參數(型別、代表意義、單位)

    回傳:
    # 請完成:說明回傳值的型別與代表意義
    """
    return weight / (height ** 2)


# 請完成:用 __doc__ 印出這個 function 的說明文件
print(  )

# 請完成:用 help() 印出這個 function 的說明文件
help(  )
```

學生需要完成:

1. Docstring 開頭的功能說明(一句話講清楚這個 function 在做什麼)
2. 兩個參數(weight、height)的說明文字,包含型別與單位
3. 回傳值的說明文字,以及 `print()` 和 `help()` 兩行程式碼

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
def calculate_bmi(weight, height):
    """
    計算 BMI(身體質量指數)。

    參數:
    weight (float): 體重 (公斤)
    height (float): 身高 (公尺)

    回傳:
    float: 計算出的 BMI 數值
    """
    return weight / (height ** 2)


print(calculate_bmi.__doc__)
help(calculate_bmi)
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
# 步驟 1:定義一個名稱為 calculate_bmi 的 function,參數為 weight 和 height


# 步驟 2:在 function 內第一行,撰寫三個雙引號的 Docstring,內容依序包含:
#         (1) 一句話說明這個 function 的功能
#         (2) 「參數:」段落,說明 weight 與 height 各自的型別、意義、單位
#         (3) 「回傳:」段落,說明回傳值的型別與意義


# 步驟 3:在 Docstring 之後,撰寫計算 BMI 的公式並 return 結果


# 步驟 4:呼叫 __doc__ 屬性,印出 calculate_bmi 的說明文件


# 步驟 5:呼叫 help() 函式,印出 calculate_bmi 的說明文件

```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
# 步驟 1:定義一個名稱為 calculate_bmi 的 function,參數為 weight 和 height
def calculate_bmi(weight, height):
    # 步驟 2:在 function 內第一行,撰寫三個雙引號的 Docstring,內容依序包含:
    #         (1) 一句話說明這個 function 的功能
    #         (2) 「參數:」段落,說明 weight 與 height 各自的型別、意義、單位
    #         (3) 「回傳:」段落,說明回傳值的型別與意義
    """
    計算 BMI(身體質量指數)。

    參數:
    weight (float): 體重 (公斤)
    height (float): 身高 (公尺)

    回傳:
    float: 計算出的 BMI 數值
    """
    # 步驟 3:在 Docstring 之後,撰寫計算 BMI 的公式並 return 結果
    return weight / (height ** 2)


# 步驟 4:呼叫 __doc__ 屬性,印出 calculate_bmi 的說明文件
print(calculate_bmi.__doc__)

# 步驟 5:呼叫 help() 函式,印出 calculate_bmi 的說明文件
help(calculate_bmi)
```

---

# 延伸挑戰題

## 題目

請設計一個計算「網路購物運費」的 function,名稱為 `calculate_shipping_fee`,參數為商品重量(公斤)與是否為偏遠地區(布林值 True/False)。規則:基本運費 60 元,重量超過 3 公斤,每超過 1 公斤加收 20 元;若是偏遠地區,總金額再加收 50 元。這個 function 一樣要撰寫完整的 Docstring,並且在「回傳」說明中,清楚描述回傳值會依照不同情況而不同(例如是否加收偏遠地區費用)。

## 提示

可以思考:

- 當參數不只兩個、且有布林值參數時,Docstring 的「參數」段落要如何分別說明清楚
- 如果計算過程中有「條件判斷」(if),要不要在 Docstring 裡稍微提到計算規則,還是只需要說明功能?
- 撰寫完後用 `help()` 印出來看看,說明文件是否讓別人一看就懂,不用讀程式碼也能知道怎麼用這個 function

---

# 思考問題

1. Docstring 是寫在 function 裡面的第一行,但程式執行時並不會被印出來或影響計算結果,那撰寫 Docstring 對「使用這個 function 的人」和「未來的自己」有什麼幫助?
2. 如果把 Docstring 裡的參數說明寫錯(例如把公斤誤寫成公克),但程式碼的計算邏輯是對的,會發生什麼問題?這件事說明了什麼?
3. `print(function.__doc__)` 和 `help(function)` 印出來的內容差在哪裡?為什麼會有兩種不同的顯示方式?

---

# 建議查詢方向

學生可以搜尋:

1. Python docstring 撰寫格式與慣例
2. Python `__doc__` 屬性是什麼
3. Python help() 函式的用法

