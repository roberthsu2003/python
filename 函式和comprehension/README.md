# 函式和Comprehension

## 良好函式設計的 5 個原則（簡化版 SOLID）
| **原則** | **說明**      |
| ------ | ----------- |
| 單一職責   | 每個函式只做一件事   |
| 易讀命名   | 使用有意義的名字    |
| 可測試    | 可以透過不同輸入做測試 |
| 可重用    | 通用邏輯、少用硬編碼  |
| 錯誤處理   | 適當處理例外狀況    |



## 自訂函數 Functions
- 自訂函數名稱與內容的安排:
	- 函數區塊以 def 開始，後接函數名稱和括號 ( )
	- 括號 ( ) 接上冒號後下一行縮排就是函數的內容
- 不支援多個同名的自訂函數:
	- 如果有同名的自訂函數則支援最後一個函數。
- 若對函數操作有任何疑問:
	- 可用 help(函數名稱) 取得說明文件。
- 自訂函數接收資料:
	- 傳入函數的參數放在 ( ) 內。
	- 可以接收多個，以逗點隔開。
	- 接收參數可以是變數，也可以是 list。
	- 函數若設定接收參數，呼叫函數時一定要給參數。
	- 接收參數可設定為不固定數量。
	- 若不接收則為空白。
- 自訂函數傳回資料:
	- 若要傳回資料，則請於函數最後一行執行 return()語法
	- return( ) 可以傳回一個運算式或者資料
	- 函數結束時不一定要傳回資料
	- 不傳回資料方式:
		- return( ) 內沒有資料
		- 省略 return( )
		- 寫成 return

## python函式設計練習表
| **題號** | **題目名稱**       | **題目說明**                   |
| ------ | -------------- | -------------------------- |
| 1      | say_hello      | 寫一個函式，輸入名字，輸出 Hello, 名字    |
| 2      | is_even        | 輸入一個整數，回傳是否為偶數（True/False） |
| 3      | sum_list       | 傳入一個數字串列，回傳總和              |
| 4      | find_max       | 輸入一串數字，找出最大值並回傳            |
| 5      | calculate_bmi  | 傳入身高（公尺）與體重（公斤），回傳 BMI 值   |
| 6      | convert_temp   | 攝氏與華氏互換（攝氏 → 華氏，華氏 → 攝氏）   |
| 7      | is_prime       | 判斷是否為質數（Prime Number）      |
| 8      | count_vowels   | 計算字串中有幾個母音（a, e, i, o, u）  |
| 9      | reverse_string | 回傳字串反轉結果                   |
| 10     | get_grade      | 傳入分數，根據標準回傳等級（A~F） |

### 1. 自訂函數沒有參數也沒有傳回值

```python
# 範例：定義一個印出歡迎詞的簡單函式
def say_welcome():
    print("歡迎光臨 Python 程式設計課！")

# 呼叫函式
say_welcome()
```

```python
# 範例：使用 pass 定義一個不做任何事的空函式
def do_nothing():
    pass

do_nothing()
```

#### Question: 請問執行後的結果哪一個是對的?(選擇題)
```python
def func_sum():
    print("A")
    return

print("B")
func_sum()
print("C")
```
(1) A, B, C  
(2) B, A, C  
(3) C, B, A  
(4) A, C, B  

> **答案：(2)**。Python 程式是由上而下執行的，但在執行到 `def` 時只是「定義」函式而未執行其內部程式。程式會先執行第 5 行的 `print("B")`，接著呼叫 `func_sum()` 執行內部的 `print("A")`，最後執行第 7 行的 `print("C")`。

#### Homework 實作練習：
請在 [function1.py](function1.py) 中定義一個無參數、無傳回值的函式，執行時能顯示「歡迎光臨」。
```python
#============================================================================
# Name        : function1.py
# 題目說明     : 定義函式，顯示「歡迎光臨」。
#============================================================================
```
[解題參考](function1.py)

---

### 2. 自訂函數有接收參數但無傳回值

```python
# 範例（對應題號 1: say_hello）：接收名字，並印出問候語
def say_hello(name):
    print(f"Hello, {name}!")

# 呼叫函式並傳入引數
say_hello("Alice")
say_hello("Bob")
```

#### Question: 請問執行後的結果哪一個是對的?(選擇題)
```python
def func_sum(a, b):
    c = a + b
    print(c)

print("1")
func_sum(3, 4)
print("2")
```
(1) 1, 7, 2  
(2) 1, 3, 4, 2  
(3) 3, 4, 1, 2  
(4) 7, 1, 2  

> **答案：(1)**。先印出 "1"，接著傳入 `3` 和 `4` 呼叫 `func_sum` 算出 `c = 7` 並印出，最後印出 "2"。

#### Question: 請問執行後的結果哪一個是對的?(選擇題)
```python
def func_sum(a, b):
    c = a + b
    print(c)

print("1")
func_sum()
print("2")
```
(1) 1, 0, 2  
(2) 1, 2  
(3) 0, 1, 2  
(4) 錯誤 (TypeError)  

> **答案：(4)**。因為 `func_sum` 定義了兩個必須傳入的參數 `a` 與 `b`，當呼叫 `func_sum()` 時未提供引數，Python 會拋出 `TypeError: func_sum() missing 2 required positional arguments` 錯誤。

---

### 3. 自訂函數有接收參數也有傳回值

使用 `return` 可以將運算結果傳回給呼叫端。這是最常用且最符合 SOLID 原則中「單一職責」與「可測試性」的函式設計方式（因為函式只專注於邏輯計算，將輸出/輸入的控制權留給呼叫端）。

```python
# 範例一（對應題號 2: is_even）：判斷整數是否為偶數並傳回 True/False
def is_even(number):
    return number % 2 == 0

# 呼叫函式並使用結果
result = is_even(7)
print(f"7 是偶數嗎？ {result}")  # 輸出: 7 是偶數嗎？ False

if is_even(10):
    print("10 是偶數")
```

```python
# 範例二（對應題號 5: calculate_bmi）：傳入身高（公尺）與體重（公斤），回傳 BMI
def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi

my_bmi = calculate_bmi(1.75, 70)
print(f"計算出的 BMI 為: {my_bmi:.2f}")
```

#### Question: 請問執行後的結果哪一個是對的?(選擇題)
```python
def func_sum(a, b):
    c = a + b * 2
    return c

print("1")
z = func_sum(3, 4)
print("2")
print(z)
```
(1) 1, 7, 2  
(2) 1, 11, 2  
(3) 1, 2, 11  
(4) 1, 2, 7  

> **答案：(3)**。執行順序為：先印出 "1"，接著呼叫 `func_sum(3, 4)`，在函式內部先計算乘法 `4 * 2 = 8` 再加 `3` 得到 `11`，透過 `return` 傳回並賦值給 `z`，接著印出 "2"，最後 `print(z)` 印出 11。因此輸出為：1, 2, 11。

#### Homework 實作練習（對應題號 6: convert_temp）：
請在 [function2.py](function2.py) 中利用自訂函式完成攝氏與華氏溫度的轉換。
公式：華氏溫度 = 攝氏溫度 * 9 / 5 + 32
```python
#============================================================================
# Name        : function2.py
# 題目說明     : 輸入攝氏溫度，使用自訂函式求華氏溫度並印出。
#============================================================================
# 期待執行效果:
# 請輸入攝氏溫度: 19
# 華氏溫度 = 66.2
```
[解題參考](function2.py)

#### Homework 進階練習（結合 while 迴圈）：
請在 [function3.py](function3.py) 中實作，讓程式可以重複詢問使用者溫度，直到輸入指定字元（例如 'N'）時結束。
```python
#============================================================================
# Name        : function3.py
# 題目說明     : 建立自訂的溫度轉換函式，並利用 while 迴圈持續讓使用者輸入，直到輸入 N 結束。
#============================================================================
# 期待執行效果:
# 請輸入攝氏溫度: 20
# 華氏溫度 = 68.0
# 程式還要繼續嗎?(輸入N結束): y
# 請輸入攝氏溫度: 10
# 華氏溫度 = 50.0
# 程式還要繼續嗎?(輸入N結束): N
# 程式結束
```
[解題參考](function3.py)

---

### 4. 傳入容器與字串的函式練習

函式的參數可以接收任何 Python 物件，包括串列（List）或字串（String）。

```python
# 範例一（對應題號 3: sum_list）：傳入數字串列，回傳總和
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

scores = [85, 90, 78, 92]
print(f"總分為: {sum_list(scores)}")  # 輸出: 總分為: 345
```

```python
# 範例二（對應題號 9: reverse_string）：傳入字串，回傳反轉字串
def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))  # 輸出: nohtyP
```

#### Homework 實作練習（對應題號 4: find_max）：
實作一個函式，接收一個數字串列，回傳其中的最大值（嘗試不使用內建的 `max()` 函式以練習邏輯）。
* 提示：定義 `find_max(numbers)`，遍歷串列比較大小。

#### Homework 實作練習（對應題號 8: count_vowels）：
實作一個函式，接收一個字串，回傳該字串中所包含的母音字母數量（母音為 a, e, i, o, u，不分大小寫）。
* 提示：定義 `count_vowels(text)`。

---

### 5. 複雜邏輯與條件分支練習

當函式內部包含較複雜的邏輯或多重條件分支時，早期回傳（Early Return）是保持程式碼乾淨的好方法。

```python
# 範例（對應題號 10: get_grade）：根據分數回傳等級 A~F
def get_grade(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

print(get_grade(85))  # 輸出: B
print(get_grade(105)) # 輸出: Invalid Score
```

#### Homework 實作練習（對應題號 7: is_prime）：
實作一個函式，傳入一個整數，判斷它是否為質數（Prime Number），回傳 `True` 或 `False`。
* 提示：質數是重大於 1 且除了 1 和自身外沒有其他因數的整數。可以使用 `for` 迴圈測試從 2 到 n-1 是否有因數。

---

### 6. 函數傳回多值

- Python 的函數可以傳回多值，這是透過將多個值自動打包成 `tuple` 實現的。
- 接收時，可以使用「多重賦值（Unpacking）」一次拆解給多個變數。

```python
# 範例：找出串列中的最大值與最小值並同時回傳
def get_min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)  # 自動打包成 tuple 回傳

scores = [85, 92, 78, 60, 99]
min_score, max_score = get_min_max(scores)  # 拆解 Tuple
print(f"最低分: {min_score}, 最高分: {max_score}")
```

#### Question: 請問執行後的結果哪一個是對的?(選擇題)
```python
def manyvalue(a, b):
    c = a * b
    return (a - 2, b + 3, c)

x, y, z = manyvalue(3, 5)
print(y)
```
(1) 8  
(2) 15  
(3) 1  
(4) 20  

> **答案：(1)**。呼叫 `manyvalue(3, 5)` 會回傳 `(3 - 2, 5 + 3, 3 * 5)` 也就是 `(1, 8, 15)`。在拆解賦值 `x, y, z = (1, 8, 15)` 後，`y` 的值為 `8`。

#### Homework 實作練習：
實作一個函式 `analyze_list(numbers)`，傳入一個數字串列，同時回傳其總和、平均值、最大值與最小值。


---

```python
#Name        : return1.py
#自鍵盤輸入一個數字n,顯示1...n。
#使用function()
#=============================

請輸入數字 n:10
1 2 3 4 5 6 7 8 9 10

#===============================
```
[解題](return1.py)

### 傳不可變實體呼叫(call by value)
```python
# Name        : callByValue1.py
#callByValue

def turbo(speed):
    print('加速前速度:',speed)
    speed += 10
    return speed

if __name__ == '__main__':
    speed = int(input('請輸入初始速度:'))
    speed = turbo(speed)
    print('加速後的速度:',speed)
```

### 傳可變實體呼叫(call by reference)
```python
#Name: callByReference.py
#callByReference


def turbo(listSpeed):
    print('加速前速度',listSpeed[0])
    listSpeed[0] += 10

s = int(input('請輸入初始速度:'))
listS = [s]
turbo(listS)
print('加速後速度',listS[0])
```

###  變數影響範圍
函數外的變數:
- 函數內可以顯示該變數內容
- 不屬於函數的區域內都可以使用

函數內的變數:
- 只在函數內產生效果，不會影響函數外的變數
- 若函數內沒有進行變數宣告而進行改變內容動作將會產生錯誤訊息

#### 操作範例:請動手操作，並留意輸出結果
```python
#fun3.py

a=5
def func_sum( ):
	a=10 
	print("函數內:",a) 
	return( )
	
	
print("函數外1:", a) 
func_sum( ) 
print(func_sum.__class__) 
print("函數外2:", a)
```

#### 操作範例:請動手操作，並留意輸出結果

```python
#fun3-1.py

a=5
def func_sum( ):
	#a=10 
	print("函數內:",a) 
	return( )
	
print("函數外1:", a) 
func_sum( ) 
print("函數外2:", a)

```

####  Question:請問執行後的結果哪一個是對的?(選擇題)

```python
a=2
def func_sum( ):
	print(a)
	return( ) 

func_sum( )
```
(1) 2  
(2) 5  
(3) 7  
(4) 3  
 
---

#### 操作範例:請動手操作，並留意輸出結果
```python
#fun3-2.py

a=5
def func_sum( ):
	#a=0
	a=a+1 
	print("函數內:",a) 
	return( )
	
print("函數外1:", a) 
func_sum( ) 
print("函數外2:", a)

```

#### Question: 請問執行後的結果哪一個是對的?(選擇題)
```python
a=3
def func_sum( ):
	a=7 
	a=a+6 
	print(a) 
	return( )
	
a += 6 
func_sum( )
```
(1) 7   
(2) 3  
(3) 13  
(4) 9  

---

####  請問執行後的結果哪一個是對的?(選擇題)
```python
a=3
def func_sum( ):
	a=7 
	a=a+6 
	return( )
a += 6 
func_sum( ) 
print(a)
```
(1) 7   
(2) 3  
(3) 13  
(4) 9  

#### HomeWork:支出最大與最小
- 輸入四個月的支出金額後列出最多與最少的支出金額。

```python
請輸入第1個月的支出金額:5000
請輸入第2個月的支出金額:4000
請輸入第3個月的支出金額:3500
請輸入第4個月的支出金額:7000
支出最多的金額為:7000
支出最少的金額為:3500
支出的總額為:19500
支出金額由小到大排序為:[3500, 4000, 5000, 7000]
```

## None的使用

- None代表變數佔著一個記憶體空間，但沒有儲存任何東西
- None轉換為boolean值時代表為False

```python
>>> thing = None
>>> if thing:
			print("It's some thing")
		else:
			print("It's no thing")
			
輸出結果 =============
It's no thing
```

使用 is 檢查是否為None

```python
>>> if thing is None:
			print("It's nothing")
		else:
			print("It's something")
輸出結果 =============
It's no thing		
```

以下，代表是None

- '' 空字串
- [] 空陣列
- (,) 空tuple
- {} 空的dictionary
- set() 空的set

```python
>>> def is_none(thing):
			if thing is None:
				print("It's None")
			elif thing:
				print("It's True")
			else:
				print("It's False")
```

 
## 使用Comprehensions語法快速簡潔方式建立list,dictionary,set,generator
- 搭配迴圈和條件式
- 語法:[ expression for item in iterable ]
- 語法:[ expression for item in iterable if condition ]
- 語法:[expression for item1 in iterable for item2 in iterable]

```python
#使用appen()方法建立
>>> number_list = []
>>> number_list.append(1)
>>> number_list.append(2) 
>>> number_list.append(3) 
>>> number_list.append(4) 
>>> number_list.append(5) 
>>> number_list 
[1,2,3,4,5]
 
```

```python

#使用range()方法加上for in迴圈建立
>>> number_list = []
>>> for number in range(1, 6):
			number_list.append(number) 
>>> number_list
[1,2,3,4,5]

```

```python

#使用list()和range()建立

>>> number_list = list(range(1, 6)) 
>>> number_list
[1,2,3,4,5]

```

```python

#使用list comprehension + for in建立
[ expression for item in iterable ]

>>> number_list = [number for number in range(1,6)] 
>>> number_list
[1,2,3,4,5]

```

```python

#使用list comprehension建立,可以用運算式靈活改變內容值

>>> number_list = [number-1 for number in range(1,6)] 
>>> number_list
[0,1,2,3,4]

```

```python

#使用list comprehension + for in + if
#語法:[ expression for item in iterable if condition ]

>>> a_list = [number for number in range(1,6) if number % 2 == 1] 
>>> a_list

[1, 3, 5]

```

```python

#上面的list comprehension建立的list,相當於基本的python語法如下:
>>> a_list = []
>>> for number in range(1,6):
		if number%2 == 1: 
			a_list.append(number)
>>> a_list
[1, 3, 5]

```

```python

#使用巢狀迴圈
>>> rows = range(1,4) 
>>> cols = range(1,3) 
>>> for row in rows:
		 for col in cols:
			print(row, col)

1 1 
1 2 
2 1 
2 2 
3 1 
3 2

```

```python

#使用list comprehension和巢狀迴圈
>>> rows = range(1,4)
>>> cols = range(1,3)
>>> cells = [(row, col) for row in rows for col in cols] 
>>> for cell in cells:
		print(cell)

(1, 1)
(1, 2)
(2, 1)
(2, 2)
(3, 1)
(3, 2)

>>> for row, col in cells:
		print(row, col)
		

```

### 詞典物件(Dictionary Comprehensions)
- 語法:{ key_expression : value_expression for expression in iterable }

```python
>>> word = 'letters'
>>> letter_counts = {letter: word.count(letter) for letter in word}
>>> letter_counts #key不會重覆
{'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

```

```python

#將word變為set
>>> word = 'letters'
>>> letter_counts = {letter: word.count(letter) for letter in set(word)} 
>>> letter_counts
{'t': 2, 'l': 1, 'e': 2, 'r': 1, 's': 1}
```

### Set Comprehensions
- 語法:{expression for expression in iterable }

```python
>>> a_set = {number for number in range(1,6) if number % 3 == 1} 
>>> a_set
{1, 4}

```

### Generator Comprehensions
- tuple沒有Comprehensions,使用括號()產生的是generator comprehension

```python
>>> number_thing = (number for number in range(1, 6))

#傳出的是generator物件
>>> type(number_thing)
<class 'generator'>

>>> for number in number_thing: 
		print(number)

1
2 
3 
4 
5

```

```python

>>> number_list = list(number_thing) 
>>> number_list
[1,2,3,4,5]

#generator只可以使用一次,使用完後就被消滅.
>>> try_again = list(number_thing) 
>>> try_again
[]


```


### 名稱空間和使用範圍(Namespaces and Scope)
- 名稱代表的就是變數名稱，function名稱
- 一個名稱空間內不可以有設定相同的名稱
- 不同的名稱空間內可以設定相同的名稱，不會衝突
- function內的程式區塊就是建立一個function的名稱空間
- 主程式py(__ name __ )是 __ main __就是全域的名稱空間，在全域名稱空間內定義的變數稱為全域變數
- function內如果要改變全域變數的值，建議使用關鍵字「global 全域變數」
- 使用locals(),globals()

```python
>>> animal = 'fruitbat'
def print_global():
	print('inside print_global:', animal)
	
	
>>> print('at the top level:', animal)
at the top level: fruitbat
>>> print_global()
inside print_global: fruitbat


#會出錯，同時使用全域變數，又建立同名的區域變數
def change_and_print_global(): 	
print('inside change_and_print_global:', animal)
	animal = 'wombat'
	print('after the change:', animal)


>>> change_and_print_global()
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	File "<stdin>", line 2, in change_and_report_it
UnboundLocalError: local variable 'animal' referenced before assignment


#不會出錯，因為在function內沒有使用全域變數，所以可以建立區域變數animal

def change_local():
	animal = 'wombat'
	print('inside change_local:', animal, id(animal))


>>> change_local()
inside change_local: wombat 4330406160 
>>> animal
'fruitbat'

>>> id(animal)
4330390832


>>> animal = 'fruitbat'

# 宣告animal是全域變數的animal,便可以在區域空間內改變全域變數的值
def change_and_print_global():
	global animal
	animal = 'wombat'
	print('inside change_and_print_global',animal)
	
>>> animal
'fruitbat'
>>> change_and_print_global()
inside change_and_print_global: wombat 
>>> animal
'wombat'


>>> animal = 'fruitbat'
	def change_and_print_global():
		animal = 'wombat'
		print('locals:',locals())
	
>>> animal
'fruitbat'
>>> change_local()
locals: {'animal': 'wombat'}

>>> print('globals',globals()) # reformatted a little for presentation
globals: {'animal': 'fruitbat',
'__doc__': None,
'change_local': <function change_it at 0x1006c0170>,
'__package__': None,
'__name__': '__main__',
'__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__builtins__': <module 'builtins'>}
>>> animal
'fruitbat'

```

### 使用__name__, __doc__

- function.__name__(輸出function name)
- function.__doc__(輸出function說豆)

```python

#建立function的說明
def amazing():
	'''This is the amazing function.
	Want to see it again?'''
	print('This function is named:', amazing.__name__)
	print('And its docstring is:', amazing.__doc__)
	
>>> amazing()
This function is named: amazing
And its docstring is: This is the amazing function.
Want to see it again?
```

### 使用try...except處理錯誤

```python
>>> short_list = [1, 2, 3]
>>> position = 5
>>> short_list[position] 
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: list index out of range



short_list = [1, 2, 3] 
position = 5
try:
	short_list[position] 
except:
	print('Need a position between 0 and', len(short_list)-1, ' but got',position)
	
	
Need a position between 0 and 2 but got 5



short_list = [1, 2, 3] 
	while True:
		value = input('Position [q to quit]? ')
		if value == 'q':
			break 
		try:
			position = int(value)
			print(short_list[position]) 
		except IndexError as err:
			print('Bad index:', position) 
		except Exception as other:
			print('Something else broke:', other)

Position [q to quit]? 1
2
Position [q to quit]? 0
1
Position [q to quit]? 2
3
Position [q to quit]? 3
Bad index: 3
Position [q to quit]? 2
3
Position [q to quit]? two
Something else broke: invalid literal for int() with base 10: 'two'
Position [q to quit]? q
```

### 建立自已的Exception

```python
class UppercaseException(Exception): 
	pass

>>> words = ['eeenie', 'meenie', 'miny', 'MO'] 
for word in words:
	if word.isupper():
		raise UppercaseException(word)
	
Traceback (most recent call last):
File "<stdin>", line 3, in <module>
__main__.UppercaseException: MO



try:
	raise OopsException('panic')
except OopsException as exc:
	print(exc)


```



