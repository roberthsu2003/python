# python 程式結構
## 基礎IPython 
執行IPython Shell  

```python
$ ipython
Python 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.12.0 -- An enhanced Interactive Python. Type '?' for help.

#安裝Numpy
$ pip install numpy
Installing collected packages: numpy
Successfully installed numpy-1.18.1
```

- 測試執行

```python
In [1]: import numpy as np

In [2]: data = {i:np.random.randn() for i in range(7)}

In [3]: data #和python不一樣的地方在於不需使用print(),可以直接輸出
Out[3]: 
{0: 1.0818001033112679,
 1: 0.49458607582804615,
 2: 1.8100857118408913,
 3: 0.2622883403607118,
 4: 1.1194071376407313,
 5: -0.32337336747509127,
 6: -0.3376644252472849}

In [4]: 

```

- 利用Tab 完成整行敘述

```python
#提示
In [1]: an_apple = 27 
In [2]: an_example = 42
In [3]: an<Tab>
an_apple and an_example any


#提示
In [3]: b = [1, 2, 3]
In [4]: b.<Tab>
b.append b.count b.insert b.reverse b.clear b.extend b.pop b.sort b.copy b.index b.removeb

#提示
In [1]: import datetime
In [2]: datetime.<Tab>
datetime.date datetime.MAXYEAR datetime.datetime datetime.MINYEAR datetime.datetime_CAPI datetime.time
datetime.timedelta datetime.timezone datetime.tzinfo
```

- %run指令(IPython)
- %load指令(Jupyter)

```python
#ipython_script_test.py
a = 5
b = 6
c = 7.5

#IPython使用%run
In [16]: %run ipython_script_test.py

In [17]: a
Out[17]: 5

In [18]: b
Out[18]: 6

In [19]: c
Out[19]: 7.5

#使用jupyter notebook
In [16]: %run ipython_script_test.py

```

## 使用?檢查
```python
In[8]:b=[1,2,3]
In [9]: b?

Type: list
String Form:[1, 2, 3]
Length: 3
Docstring:
list() -> new empty list
list(iterable) -> new list initialized from iterable's items

In [10]: print?

Docstring:
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file: a file-like object (stream); defaults to the current sys.stdout. sep: stringinsertedbetweenvalues,defaultaspace.
end: stringappendedafterthelastvalue,defaultanewline.
flush: whether to forcibly flush the stream.
Type: builtin_function_or_method
```

## 註解
```python
>>> # 60 sec/min * 60 min/hr * 24 hr/day 
>>> seconds_per_day = 86400

>>> seconds_per_day = 86400 # 60 sec/min * 60 min/hr * 24 hr/day


#python不支援多行註解
>>> # I can say anything here, even if Python doesn't like it,
... # because I'm protected by the awesome
... # octothorpe. ...
>>>

>>> print("No comment: quotes make the # harmless.")
 No comment: quotes make the # harmless.

```

## Continue Lines with \

```python
>>> alphabet = ''
>>> alphabet += 'abcdefg'
>>> alphabet += 'hijklmnop'
>>> alphabet += 'qrstuv'
>>> alphabet += 'wxyz'

#連結字串
>>> alphabet = 'abcdefg' + \
... 'hijklmnop' + \
... 'qrstuv' + \
... 'wxyz'


>>> 1+2+
File "<stdin>", line 1
1+2+ ^
SyntaxError: invalid syntax 
>>>1+2+\
... 3
6
```
## 資料輸入
- input 代表資料輸入
- 輸入資料後可利用變數 .__class__ 方式查詢變數的資料型態。
- 預設輸入的資料型態為字串
	- 若是整數資料您必須加入 int( ) 轉換。
		- 如果輸入浮點數或者字串都會產生錯誤訊息。
	- 若是浮點數小數資料您必須加入 float( ) 轉換。
		- 如果輸入整數會當作浮點數處理，輸入字串會產生錯誤訊息。  

```python
資料輸出入:請動手操作，並留意輸出結果
# input01.py

a = input("輸入整數1a: ") 
b = input("輸入整數1b: ") 
c = int(input("int輸入c:")) 
d = int(input("int輸入d:")) 
f=a+b
g=c+d 
print(f)
print(g)
```

```python
資料輸出入:請動手操作，並留意輸出結果
# input02.py

c = int(input("int輸入c:"))
d = int(input("int輸入d:")) 
g=c+d
print(g)
h = float(input("float輸入h:"))
i = float(input("float輸入i:"))
j=h+d
print(j)
```

```python
資料輸出入:請動手操作，並留意輸出結果
# input03.py

a = input("輸入字串: ")
print(a,a.__class__ )
a = input("輸入整數: ")
print(a,a.__class__ )
a = float(input("float輸入浮點數: "))
print(a,a.__class__ )
a = int(input("int輸入整數:"))
print(a,a.__class__ )
a = int(input("int輸入字串:"))
print(a,a.__class__ )
```

## 數值運算子

運算子 | 描述  | 範例
-----| ------- | ----
| + | 加法 | 5+8=13
| - | 減法 | 90-10=80  
| * | 乘法 | 4*7=28
| / | 浮點數除法 | 7 / 2=3.5
| // | 整數除法 | 7 // 2 = 3
| % | 餘數  | 7 % 3 = 1
| ** | 次方 |  3 ** 4 = 81

### question: 請問計算後Z的內容哪一個是對的?(選擇題)
```python
x=5
y=7 
z=x+y+1
```
(1) 571  
(2) 1   
(3) 13  

---
### 數值計算:請動手操作，並留意輸出結果
```python
#num.py

a,b,c=4,2,5
d,f=3.25,5.5
print (a*b) 
print (a**b) 
print (a % 3) 
print (d + f) 
print (c//b) 
print (a/b)
```

### question: 請問執行後的說明哪一個是對的?(選擇題)
```python
g,h=9,3
print(g/h)
```
(1) 3
(2) 0 
(3) 3.0

---
### Homework(mathop.py):
- 讓使用者輸入被除數(整數)及除數(整數，不可以是零)
- 程式會顯示兩數相除的商及餘數。

```python
請輸入被除數(整數):45
請輸入除數(整數,不可以為0):4
商 11 餘數: 1
```
[解題](mathop.py)

### Homework(plus_s.py):
- 計算使用者輸入的2個任意數，程式會顯示2數相加的總和。  

```python
請輸入第一個數值:45.67
請輸入第二個數值:67.47
兩個數的和是xxx.xx
```
[解題](plus_s.py)

## 複合指定運算子
- 當「=」左右兩邊是相同資料時可以使用精簡方式:
	- 省略「=」右邊相同資料。
	- 將「=」右邊的計算符號移到「=」左邊。
- 例如以下操作方式可作變更
	- x=x+2，可精簡為 x+=2
	- y=y-3，可精簡為 y-=3

### 精簡計算式:請動手操作，並留意輸出結果
```python
#money.py
money = 50000 
cell = int(input("請輸入手機金額:"))
money -= cell
print("剩餘款為:" + str(money)) 
```

### Homework(complex.py):
- 請使用者輸入一個任意數，程式會顯示此數的平方值及立方值  

```python
請輸入任意數:3
此數的平方是:9.0
此數的立方是:27.0
```
[解題](complex.py)

### Homework(complex_s.py):
- 請以(複合指定運算子)設計程式,讓用者輸入三個任意數，程式會顯示3數相加的總和(float)

```python
請輸入第一個數:87.9
請輸入第二個數:45
請輸入等三個數:87.5
三個數的總和為:220.4
```
[解題](complex_s.py)
### Homework(ladder.py):
- 讓使用者輸入梯形的上底、下底及高，程式會計算梯形的面積(上底加下底乘以高除以2)

```python
請輸入梯形的上底(公分):5
請輸入梯形的下底(公分):10
請輸入梯形的高(公分):2
梯形的面積:15平方公分
```
[解題](ladder.py)

### Homework(circle_s.py)
- 使用者輸入圓柱體的半徑及高，程式會計算圓柱體的體積
- 圓柱體體積的公式為「圓週率乘以半徑平方再乘以高」。

```
請輸入圓柱體的半徑(公分):10
請輸入圓柱體的高(公分):5
圓柱體的體積:xxxx立方公分
```
[解題](circle_s.py)
##  條件分析
- 程式語言可以協助進行資料分析判斷，結果會有成立與不成立兩個方向。
- 條件分析語法計有:
	- 單一選擇
	- 雙向選擇
	- 多向選擇

##  關係運算子

| 符號 | 意義 |
|:--|:--|
| < | 小於 |
| <= | 小於等於 |
|  > | 大於 |
|  >= | 大於等於 |
|  == | 兩邊是否等於 |
|  != | 兩邊是否不等於 |

```python

>>> x=7
>>> x==5 
False 
>>> x==7
True 
>>> 5<x
True
>>> x<10 
True

>>> 5<x and x<10 
True

>>> (5<x) and (x<10)
True

>>> 5<x or x<10 
True 

>>> 5<x and x>10
False 

>>> 5 < x and not x > 10 
True

>>>5 < x < 10 
True

>>> some_list = []
>>> if some_list:
		print("There are something in here")
	else:
		print("Hey! It's empty")

Hey, it's empty!
```

##  單一選擇
- 單一選擇用於只有條件成立時，才會執行的敘述區塊。  

```python
語法:  
if [true|false]:
	true區塊

```
	
### 單一選擇:請動手操作，並留意輸出結果
```python
#if-1.py

a=21
if a>18:
	print("大於18")

print("執行結束")
```

###  請問執行後最後輸出的結果是哪一個?(選擇題)
```python
a = 15
if a >= 14:
	a -= 2 
	print(a)
```
(1) 14  
(2) 15  
(3) 13  

---

##  雙向選擇:if else
- 條件成立要執行某事情，而條件不成立則進行其他事情，可使用if else 語法。

```python
語法:  
if [True|False]:
	true區塊
else:
	false區塊
```

### 雙向選擇 if else:請留意輸出結果  

```python
# if2.py

a=21
if a>18:
	print("大於18") 
else:
	print("小於18") 

print("執行結束") 

```

### 請問執行後的結果哪一個是對的?(選擇題)
```python
a=12
if a!=12:
	print("不等於12") 
else:
	print("等於12") 
print("執行結束")
```
(1)  
等於12  
執行結束

(2)  
不等於12  
執行結束

(3)  
等於12 
不等於12  
執行結束

---

### Homework(password.py):
- 讓使用者輸入密碼,如果輸入的密碼正確(1234), 要顯示「密碼正確!歡迎光臨!」。
- 如果不正確就顯示密碼錯誤訊息

```python
請輸入密碼:2345
密碼錯誤
請重新輸入
```
[解題](password.py)

##  多向選擇:if elif else
- 條件成立要執行某事情，而條件不成立則要進行另外一個分析，請使 用 if elif 語法。

```python
語法:  
if [True|False]:
	true區塊
elif [True | False]:
	true區塊
else:
	false區塊
```

```python
# if3.py

a=21
if a>18:
	print("大於18") 
elif a>12:
	print("大於12") 
else:
	print("小於12")
```

### 多向選擇 if elif:請留意輸出結果

```python
# if3-2.py
#有問題的設計
a=21
if a>12:
	print("大於12")
elif a>18:
	print("大於18") 
else:
	print("小於12")
```

###  請問執行後的結果哪一個是對的?(選擇題)
```
a=11
if a>18:
	print("大於18")
elif a>12:
	print("大於12")
else:
	print("小於12")
```
(1) 大於 18  
(2) 大於 12  
(3) 小於 12 

---

### Homework(discount.py):
輸入顧客購買金額，若金額在
- 100000元打8折
- 50000打85折
- 30000打9折
- 10000打95折

```python
請輸入購買金額:130000
實付金額是: 104000.0 元
```
[解題](discount.py)

## 判斷流程控制 if, elif, and else
```python
#雙向選擇
>>> disaster = True 
>>> if disaster:
		print("Woe!") 
	else:
		print("Whee!")
Woe!

```

```python
#巢狀選擇
furry = True 
small = True 
if furry:
	if small:
		print("它是貓!")
	else:
		print("它是熊!")
else:
	if small:
		print("它是小蜥蜴")
	else:
		print("它是人類或是沒毛的熊")

It's a cat.

```

```python
#多項選擇
color = "紫褐色"
if color == "紅色":
    print("It's a 蕃茄")
elif color == "green":
    print("It's a 青椒")
elif color == "蜂密青":
    print("我不知道蜂密青, 我只知道蜂密")
else:
    print("我沒有聽過這個顏色", color)


I've never heard of the color puce
```

##  邏輯運算符號
- 針對條件進行邏輯判斷時用到  

| 符號 | 意義 |
|:--|:--|
| and | 左右兩個條件若都為真則為真，否則為假。 |
| or | 左右兩個條件只要一個為真就是真，否則為假。 |
| not |  條件若為真則改為假，若為假則改為真。 |

```python
語法:  
[boolean and boolean]
[boolean or boolean]
[not boolean]
```

### 邏輯運算子:請留意輸出結果
```python
#if4.py
a=14
if a>=12 and a<18 :
	print("ok-1")
else:
	print("cancel- 1") 
	
if 12<=a<18:
	print("ok-2") 
else:
	print("cancel- 2")
	
if not a>18:
	print("ok-3") 
else:
	print("cancel- 3")
```

### ‌ question:請問執行後的結果哪一個是對的?(選擇題)
```python
a=11
if a>=12 or a<18 :
	print("ok-1") 
else:
	print("cancel-1")
```
(1) ok-1  
(2) cancel-1  
(3) ( 空內容 )

---
###  請問執行後的結果哪一個是對的?(選擇題)

```python
a=14
if a>=12 and a<18:
	print("1") 
else:
	print("2")

if 12<=a<18:
	print("3")
else:
	print("4")

```
(1) 1 3  
(2) 1 4  
(3) 2 3  
(4) 2 4

---

###  請問執行後的結果哪一個是對的?(選擇題) 

```python
a=24
if a>=12:
	print("1") 
else:
	print("2")
	
if not a>=12:
	print("3")
else:
	print("4")
	
```
(1) 1 3   
(2) 1 4  
(3) 2 3  
(4) 2 4

### HomeWork:BMI 計算後分析
- 請依據 BMI 值分析他人的身體狀況。

| BMI值 | < 18.5 | 18.5-25 | 25-30 | >30 |
|:--|:--|:--|:--|:--|
| 身體狀態 | 太輕 | 正常 | 過重 | 肥胖 |
 
 ```
 #bmi.py
 請輸入身高,單位為(公分):177
 請輸入體重,單位為(公斤):80
 
 您的BMI是25.53544
 「您的體重過重」
 ```
 [解題](bmi.py)
 






