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




## python數學運算子

運算子 | 描述  | 範例
-----| ------- | ----
| + | 加法 | 5+8=13
| - | 減法 | 90-10=80  
| * | 乘法 | 4*7=28
| / | 浮點數除法 | 7 / 2=3.5
| // | 整數除法 | 7 // 2 = 3
| % | 餘數  | 7 % 3 = 1
| ** | 次方 |  3 ** 4 = 81

--- 
## python的整數

```python
>>> 5
5

>>> 0
0

#數字前不可以加0
>>> 05
      File "<stdin>", line 1
05
^
SyntaxError: invalid token #python的語法錯誤


#正整數
>>> 123
    123
>>> +123
    123
    
#負整數
>>> -123 
-123

#整數運算
>>>5+9 
   14 
>>>100-7 
   93 
>>>4-10 
   -6
   
#多個數值運算
>>>5+9+3
17 
>>>4+3-2-1+6 
	 10
	 
#乘法運算
>>>6*7
42
>>>7*6
42 
>>>6*7*2*3 
   252
   
#浮點數除法
>>>9/5 
   1.8

#整數除法
>>>9//5 
   1
#除數不可以為零
>>>5/0
Traceback (most recent call last):
File "<stdin>", line 1, in <module> ZeroDivisionError: division by zero >>>7//0
Traceback (most recent call last):
File "<stdin>", line 1, in <module> ZeroDivisionError: integer division or modulo by z


#變數可以運算
>>>a=95 
>>> a
95 
>>>a-3 
   92

#將變數自已的內容減3   
>>>a=a-3 
>>> a
92

>>>a=95 
>>>temp=a-3 
>>>a=temp

#上面敘述式，可以使用下面這行替代
>>>a=a-3

#餘數
>>>9%5 
   4
   
>>> divmod(9,5)
    (1, 4)

>>> 9//5 
   1 
>>> 9%5 
   4



```

## 數學運算子優先順序

```python
優先順序由上而下
()
**
正負
* / % //
+ -
=

>>>2+3*4 
   14
   
>>>(2+3)*4
   20

>>> 2 * (1 + 2) ** 2 - 2 ** 2 * 2 
	10
```

## 2,8,16進位
表示 | 進位
--- | ---
0b 0B | 2進位
0o 0O | 8進位
0x 0X | 16進位

```python
#10進位
>>> 10 
10

#2進位
>>> 0b10
2

#8進位
>>> 0o10
8

#16進位
>>> 0x10
16

```

## 類型轉換

```python
>>> int(True)
    1
>>> int(False)
    0
 
 
    
>>> int(98.6) 
    98
>>> int(1.0e4) 
    10000
 
  
    
>>> int('99') 
    99
>>> int('-23') 
    -23
>>> int('+12')
    12


>>> int(12345)
    12345



>>> int('99 bottles of beer on the wall')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '99 bottles of beer on the wall' >>> int('')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: ''



>>> int('98.6')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '98.6' >>> int('1.0e4')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '1.0e4'



>>>4+7.0 
   11.0
   

>>>True+2
    3
>>> False + 5.0 
    5.0
```

## int的範圍

```python
>>>
>>> googol = 10**100
>>> googol
   100000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000

>>> googol * googol
    100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000


    
```

## float浮點數

```python
>>> float(True) 
    1.0
>>> float(False)
    0.0

>>> float(98) 
    98.0
>>> float('99') 
    99.0

    

>>> float('98.6')
    98.6
>>> float('-1.5')
    -1.5
>>> float('1.0e4')
    10000.0


```

## 字串

```python
>>> 'Snap'
    'Snap'
    
>>> "Crackle"
    'Crackle'

>>> "'Nay,' said the naysayer."
"'Nay,' said the naysayer."

>>> 'The rare double quote in captivity: ".'
'The rare double quote in captivity: ".'

>>> 'A "two by four" is actually 1 1⁄2" × 3 1⁄2".'
'A "two by four is" actually 1 1⁄2" × 3 1⁄2".'

>>> "'There's the man that shot my paw!' cried the limping hound." "'There's the man that shot my paw!' cried the limping hound."
 
```

### 多行文字

```python

>>> '''Boom!'''
    'Boom'
    
>>> """Eek!"""
    'Eek!'

#單行文字    
>>> poem = "Apple Arcade 推出的最新遊戲《Next Stop Nowhere》，由位於洛杉磯的開發商 Night School Studio 出品。這款遊戲是太空公路之旅的夥伴冒險，其中不同角色間展開了一些精彩的劇情。在銀河系的外圍，每個人和所有事物之間都有充分的空間，Night School 希望這款遊戲可為近來可能感到孤立的玩家提供一些慰藉。"

#單行文字
>>>"Apple Arcade 推出的最新遊戲《Next Stop Nowhere》，\
由位於洛杉磯的開發商 Night School Studio 出品。\
這款遊戲是太空公路之旅的夥伴冒險，其中不同角色間展開了一些精彩的劇情。\
在銀河系的外圍，每個人和所有事物之間都有充分的空間，Night School\
希望這款遊戲可為近來可能感到孤立的玩家提供一些慰藉。"


>>> poem2 = '''Apple Arcade 推出的最新遊戲《Next Stop Nowhere》，由位於洛杉磯的開發商 Night School Studio 出品。

這款遊戲是太空公路之旅的夥伴冒險，其中不同角色間展開了一些精彩的劇情。

在銀河系的外圍，每個人和所有事物之間都有充分的空間，Night School 希望這款遊戲可為近來可能感到孤立的玩家提供一些慰藉。 '''

>>> print(poem2)
Apple Arcade 推出的最新遊戲《Next Stop Nowhere》，由位於洛杉磯的開發商 Night School Studio 出品。

這款遊戲是太空公路之旅的夥伴冒險，其中不同角色間展開了一些精彩的劇情。

在銀河系的外圍，每個人和所有事物之間都有充分的空間，Night School 希望這款遊戲可為近來可能感到孤立的玩家提供一些慰藉。



>>> print(99, 'bottles', 'would be enough.') 
    99 bottles would be enough.
    
    

>>> ''
    ''
>>> ""
    ''
>>> ''''''
    ''
>>> """"""
    ''
>>>


#使用str()轉換為字串型別
>>> str(98.6) 
    '98.6'
>>> str(1.0e4) 
    '10000.0'
>>> str(True)
    'True'
  
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



#字串使用加法運算
#字串無法自動加數值
>>> bottles = 99
>>> base = ""
>>> base = base + 'current inventory:'
>>> base = base + str(bottles)
'current inventory:99'

#脫溢字元(特殊字元)
- 反斜線作為跳脫字元，可用於引用特殊字元。
	- \\ 反斜線
	- \’ 單引號
	- \” 雙引號
	- \n 換行
	- \t 固定間隔




>>> games = '遊戲：《鬼靈精大腳怪》\n說明：今天的遊戲更新為玩家開啟了一個全新的探索環境。從城鎮下方的新碼頭出發，乘渡輪前往新的小島，然後乘坐四輪驅動車四處巡遊，或者在衝浪遊戲中盡情衝浪。玩家還可以購買新船進行升級與比賽，或是出海捕捉鹹水魚。這是調皮大腳怪的暑假！\n\n遊戲：《迷你公路》\n說明：《迷你公路》推出了一項新更新，以透過 Fast Forward 模式協助加快道路網絡的建立，使玩家能選擇其遊戲速度。' 

>>> print(games)
遊戲：《鬼靈精大腳怪》
說明：今天的遊戲更新為玩家開啟了一個全新的探索環境。從城鎮下方的新碼頭出發，乘渡輪前往新的小島，然後乘坐四輪驅動車四處巡遊，或者在衝浪遊戲中盡情衝浪。玩家還可以購買新船進行升級與比賽，或是出海捕捉鹹水魚。這是調皮大腳怪的暑假！

遊戲：《迷你公路》
說明：《迷你公路》推出了一項新更新，以透過 Fast Forward 模式協助加快道路網絡的建立，使玩家能選擇其遊戲速度。



>>> print('\tabc') 
    abc
>>> print('a\tbc') 
    a bc
>>> print('ab\tc') 
    ab c
>>> print('abc\t') 
    abc



>>> testimony = "\"I did nothing!\" he said. \"Not that either! Or the other thing.\""

>>> print(testimony)
"I did nothing!" he said. "Not that either! Or the other thing."

>>> fact = "The world's largest rubber duck was 54'2\" by 65'7\" by 105'"
 
>>> print(fact)
The world's largest rubber duck was 54'2" by 65'7" by 105'

>>> speech = 'Today we honor our friend, the backslash: \\.' 
>>> print(speech)
Today we honor our friend, the backslash: \.



# 使用 + 運算子
>>> 'Release the kraken! ' + 'At once!'
    'Release the kraken! At once!'

>>> a = 'Duck.' 
    b=a
    
>>> c = 'Grey Duck!' 

>>>a+b+c 
   'Duck.Duck.Grey Duck!'



>>> print(a, b, c) 
    Duck. Duck. Grey Duck!
    
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




### question:以下的資料輸出哪一個是錯的?(選擇題)
(1) "I can add integers, like " + str(5) + " to strings."  
(2) "Isaid"+("Hey"*2)+"Hey!"  
(3) "The correct answer to this multiple choice exercise is answer number" + 2  
(4) True + False  

---
 
### question:請問執行後的說明哪一個是對的?(選擇題)
```python
a,b,c="pcschool",2016,3.41
print(b)
```
(1) 2016  
(2) 3.41  
(3) pcschool  

---


###  請問執行後的說明哪一個是對的?(選擇題)
```python
test=("abc"+"!")*2
print(test)
```
(1) abc!2  
(2) abc! abc!
(3) abc+!*2

---


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

---

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
 






