# 暱名函數與套件的使用
### Functions Are First-Class Citizens

```python
>>> def answer(): 
		print(42)

>>> answer()
42
```

```python

>>> def run_something(func): 
		func()

>>> run_something(answer) 
42
```


```python
def add_args(arg1, arg2): 
	print(arg1 + arg2)
	

>>> type(add_args)
<class 'function'>


def run_something_with_args(func, arg1, arg2):
	func(arg1, arg2)
	

>>> run_something_with_args(add_args, 5, 9) 
14

```

```python
def sum_args(*args): 
	return sum(args)
	

def run_with_positional_args(func, *args):
	return func(*args)


>>> run_with_positional_args(sum_args, 1, 2, 3, 4)
10	
```

### Inner Functions

```python
def outer(a, b):
	def inner(c, d): 
		return c+d
	return inner(a, b)


>>> outer(4, 7)
11


def knights(saying):
	def inner(quote):	
		return "We are the knights who say: '%s'" % quote
	return inner(saying)
	
	
>>> knights('Ni!')
    "We are the knights who say: 'Ni!'"
```

### Closures
```python
def knights2(saying):
	def inner2():
		return "We are the knights who say: '%s'" % saying
	return inner2

>>> a = knights2('Duck')
>>> b = knights2('Hasenpfeffer')

>>> type(a) <class 'function'> 
>>> type(b) <class 'function'>

>>> a
<function knights2.<locals>.inner2 at 0x10193e158> 
>>> b
<function knights2.<locals>.inner2 at 0x10193e1e0>

>>> a()
"We are the knights who say: 'Duck'"
>>> b()
"We are the knights who say: 'Hasenpfeffer'"
```

##  匿名函數
1. 不需要定義函數名稱的，只需要用運算式或表達分析語法。
2. Python 使用 lambda 語法定義匿名函數。
3. 匿名函數是一個表達式/計算式，並不是一個執行流程區塊。
4. 匿名函數可以出現在一般函數不允許的地方，例如像 list 內部或函數 呼叫參數的位置。

###  匿名函數說明
1. 匿名函數會自動返回計算式結果，一般函數必須進行規劃設計才能返回。
2. 匿名函數用於一個計算式的處理，而一般函數可以做更多複雜的事情。
3. 匿名函數語法:
	- lambda 參數: 運算式,資料來源
	- 參數-可能是多個值
	- 資料來源-於第一個之後的都是資料來源，這裏得對應資料輸入

#### 操作範例:請動手操作，並留意輸出結果
```python
#lam-1.py

#傳統函數 
def f(x, y, z):
	return x + y + z 
print("傳統函數處理") 
print(f(2, 30, 400)) 

#匿名函數
f = lambda x, y, z: x + y + z 
print("匿名函數處理") 
print(f(2, 30, 400))
```

#### 操作範例:請動手操作，並留意輸出結果
```python
#lam-2.py

#匿名函數當作參數傳入
print("匿名函數當作參數傳入")
mz = (lambda a = 'Wolfgangus', b = ' Theophilus', c = ' Mozart': a + b + c) 
print(mz('Wolfgang', ' Amadeus')) 
```

### 匿名函數說明
1. 匿名函數可用於 list 內，可以快速的處理各種數值計算結果，傳入資料與得到回應。
2. 匿名函數可用於條件分析表達上。

#### 操作範例 1-1:請動手操作，並留意輸出結果
```
try1 = [lambda x: x ** 2, lambda x: x ** 3,
lambda x: x ** 4] 
print(try1.__class__) 
for f in try1:
	print(f.__class__)
	print(f(3))
 
print(try1[0](11))
```

#### 操作範例 2-1:請動手操作，並留意輸出結果
```python
#lam-3a.py 

print("一般函數處理") 
def f1(x):
	return x ** 2 

def f2(x):
	return x ** 3 

def f3(x):
	return x ** 4 

try2 = [f1, f2, f3] 

for ff in try2:
	print(ff.__class__)
	print(ff(3)) 

print(try2[0](3))
```

#### 操作範例 3:請動手操作，並留意輸出結果
```python
#lam-4.py

print("匿名函數可用於條件分析表達上") 
findmin=(lambda x, y: x if x < y else y)
print(findmin(101*99, 102*98))  
print(findmin(102*98, 101*99))
```

#### 操作範例 4:請動手操作，並留意輸出結果
```python
# lam-5.py

#搭配字典，設計出分組挑選的流程 
score = int(input('please input:')) 
level = score // 10
{
10 : lambda: print('Perfect'),
9 : lambda: print('A'),
8 : lambda: print('B'),
7 : lambda: print('C'),
6 : lambda: print('D') }.get(level)()

```

### Anonymous Functions: the lambda() Function
```python
def edit_story(words, func):
	for word in words:
		print(func(word))


>>> stairs = ['thud', 'meow', 'thud', 'hiss']


def enliven(word): # give that prose more punch 
	return word.capitalize() + '!'
	
>>> edit_story(stairs, enliven) 
Thud!
Meow!
Thud!
Hiss!


>>> edit_story(stairs, lambda word: word.capitalize() + '!') 
Thud!
Meow!
Thud!
Hiss!
```

###  map 與 filter
1. 用法:map(function, sequence)
2. 將複合性資料逐一取出項目再傳入到 function 操作，最後以 list 作為回傳值。
3. filter( ) 函數用於過濾 list，過濾掉不符合條件的元素，返回由符合條件元素組 成的新 list。
4. filter 接收兩個參數，第一個為函數，第二個為 list，list 的每個元素作為參數 傳遞給函數進行分析，然後返回 True 或 False，最後將返回 True 的元素放 到新list中。

#### 操作範例 1:請動手操作，並留意輸出結果
```python
#map-1.py

def multiply2(x): 
	return x * 2
	
a = map(multiply2, [1, 2, 3, 4])
list1=list(a)
print(list1)

a=map(lambda x : x*2, [1, 2, 3, 4])
list2=list(a)
print(list2)
b=[1, 2, 3, 4] 
c=b*2 
print(c) 
```

#### 操作範例 2:請動手操作，並留意輸出結果
```python
#map-2.py

 dict1 = [{'name': 'python', 'points': 10},
  {'name': 'java','points': 8}] 

print(type(dict1))
list3=map(lambda x : x['name'], dict1)
print(list(list3))

list4=map(lambda x : x['points']*10, dict1) print(list(list4))

list5=map(lambda x : x['name'] == "python", dict1) print(list(list5))

list6a = [1, 2, 3]
list6b = [10, 20, 30]
list6=map(lambda x, y: x + y, list6a, list6b) print(list(list6))
```

#### 操作範例 3:請動手操作，並留意輸出結果
```python
#filter-1.py
a = [1, 2, 3, 4, 5, 6]
list7=filter(lambda x : x % 2 == 0, a)
print(list(list7))

dict8 = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
list8=filter(lambda x : x['name'] == 'python', dict8)
print(list(list8))

```






##  使用模組
1. 可透過 import 引用其他檔案，就可以使用其他檔案內的類別與函數進行功能擴充。

2. Python 檔案命名時不要與其他已知模組名稱相同，名稱相同時預設 呼叫自己的檔案。

###  使用模組
引用 python 檔案就以檔案的主檔案名稱作為模組名稱， 共有以下三種方式:   
 
1. import 模組
2. import 模組 as 新模組名稱
3. from 模組 import 模組內方法
	- 不建議 from 模組 import *，易造成名稱衝突

#### 操作範例:請動手操作，並留意輸出結果
```python
#modu.py
class test1:
	def __init__(self):
		print("create") 
	
def fun1( ):
	print("function")
	return( ) 

#如果主程式不放在條件分析內呢? 
if __name__ == '__main__':
	print("testmu!")
```

```python
import modu
ob1=modu.test1( ) #create object 
modu.fun1( )
 
```

####  請問以下這一行語法解釋哪一個錯誤?(選擇題)
```python
import math1
```
(1) math1 是模組   
(2) 引用 math1.py 內容  
(3) math1.py 與主程式放在一起  
(4) math1.py 與主程式不放在一起

## 自製套件  
1. 套件內可以有多個模組。
2. 套件名稱是資料夾名稱。
3. 建立一個叫做 happy 的資料夾，裡面放了一個 __init__.py 的空檔案。
4. 每個套件裡都必須存在 __init__.py 這個檔案，它的目的就是告訴 Python 說這個資料夾請把它當做套件來對待。
5. __init__.py 可以是空的，也可以放一些變數或程式在裡面。
6. happy 的資料夾內放了一個 __init__.py 的空檔案，請加入一個名為 my_mod.py 檔案，其內容為:

```python
def happy_python( ):
	print ("Happy Python")
```

7. 呼叫語法可以這樣規劃:

```python
import happy.my_mod
happy.my_mod.happy_python( )
```

8. 呼叫語法也可以這樣規劃:

```
from happy.my_mod import happy_python
happy_python( )

```

#### Question: 請問以下語法所代表的檔案哪一個錯誤?(選擇題)
```python
__init__.py
```
(1) 每個套件都要有這個檔案  
(2) 每個套件都不要有這個檔案  
(3) 可以是空的  
(4) 也可以加入語法進行互動

## 呼叫內建模組函數
###  Import 這個功能的使用:以亂數為例
1. 必須加入import random語法。
2. 隨機整數:0 到 100 之間(包含100)，請加入andom.randint(0,100) 語法。
3. 隨機數值:請加入random.random ( ) 語法。
4. 隨機選取 0 到100 間的偶數(固定間隔)，請加入random.randrange(0, 101, 2) 語法。

#### 操作範例:請動手操作，並留意輸出結果
```python
#rand1.py
import random 
a=random.randint(0,100) 
print(a) 

b=random.randrange(0, 101, 2) 
print(b)

c=random.random( )
print(c)
```

### 以亂數為例
1. 重新調整順序:random.shuffle(items)
2. 隨機字元:請加入 random.choice('abcdefg&#%^*f') 語法。
3. 多個字元中選取特定數量的字元:例如加入以下語法:

```python
 random.sample('abcdefghij',3)
 ```
 
4. 隨機選取字串:例如加入以下語法:

```python
random.choice ( ['apple', 'pear', 'peach', 'orange', 'lemon'] )
```

#### 操作範例:請動手操作，並留意輸出結果
```python

#rand2.py
import random
a=random.sample('abcdefghij',3)
print(a)

b=random.choice( ['apple', 'pear', 'peach', 'orange', 'lemon'] ) 
print(b)

items = [1, 2, 3, 4, 5, 6]
random.shuffle(items)
print(items) 
```

#### Question: 請問以下語法執行後結果哪一個錯誤?(選擇題)
```python
import random 
a=random.randint(0,100) 
print(a)
```
(1) 0  
(2) 100   
(3) 99   
(4) 101  

---

###  數學函數
以下幾個函數必須引用 math 模組: 

|--:|--:|
| sqrt(x) | x的平方根(x>0) |
| pow(x, y) | x的y次方 的值 |
|  ceil(x) | 取出不小於 x 的最小整數 |
| floor(x) | 取出不大於 x 的最大整數 |

####  Question:請問以下語法執行後結果哪一個正確?(選擇題)
```python 
a=round(80.456, 2) 
print(a)
```
(1) 80    
(2) 81  
(3) 80.45   
(4) 80.46  

---

####  請問以下語法執行後結果哪一個正確?(選擇題)
```python
import math 
a=math.floor(80.456) 
print(a)
```

(1) 80  
(2) 81   
(3) 80.45  
(4) 80.46  

---

####  請問以下語法執行後結果哪一個正確?(選擇題)

```python
import math

a=math.ceil(80.456) 
print(a)
```
(1) 80  
(2) 81   
(3) 80.45   
(4) 80.46  

---
####  Homework:匿名函數操作
- 目前有一個list，內容為"apple", "banana", "papaya", "watermelon"
- 請利用匿名函數於這些資料後面加上!!!
- 輸出為

```python
['apple!!!', 'banana!!!', 'papaya!!!', 'watermelon!!!']
```

--- 
## Modules, Packages, and Programs
### Standalone Programs
```python
#test.py

>>> print("This interactive snippet works.") 
This interactive snippet works.


$ python test1.py
This standalone program works!
```

### Command-Line Arguments

```python
# test2.py 

import sys
print('Program arguments:', sys.argv)


$ python test2.py
Program arguments: ['test2.py']
$ python test2.py tra la la
Program arguments: ['test2.py', 'tra', 'la', 'la']

```

### Modules and the import Statement

```python
#A module is just a file of Python code.
```

### Import a Module
```python
#module is the name of another Python file, without the .py extension

# weatherman.py

import report
description = report.get_description() 
print("Today's weather:", description)

# report.py

def get_description(): # see the docstring below? 
	"""Return random weather, just like the pros""" 

	from random import choice
	possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows'] 
	return choice(possibilities)



$ python weatherman.py 
Today's weather: who knows 
$ python weatherman.py 
Today's weather: sun
$ python weatherman.py 
Today's weather: sleet



def get_description(): 
	import random
	possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows'] 
	return random.choice(possibilities)


```

```python
>>> import random
>>> def get_description():
...possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows'] 
...return random.choice(possibilities)

>>> get_description()
'who knows'
>>> get_description() 
'rain'

```

### Import a Module with Another Name

```python
import report as wr
description = wr.get_description() 
print("Today's weather:", description)

```

### Import Only What You Want from a Module

```python
from report import get_description
description = get_description()
print("Today's weather:", description)




from report import get_description as do_it 
description = do_it()
print("Today's weather:", description)

```

### Module Search Path

```python
>>> import sys
>>> for place in sys.path: 
... print(place)



/Library/Frameworks/Python.framework/Versions/3.3/lib/python33.zip
/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3 
/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/plat-darwin 
/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/lib-dynload 
/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/site-packages
```

## Packages

```python
#Main program: boxes/weather.py.

from sources import daily, weekly
print("Daily forecast:", daily.forecast()) 
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
	print(number, outlook)


#Module 1: boxes/sources/daily.py.
def forecast():
	'fake daily forecast' 
	return 'like yesterday'
	

#Module 2: boxes/sources/weekly.py.

def forecast():
	"""Fake weekly forecast"""
	return ['snow', 'more snow', 'sleet','freezing rain', 'rain', 'fog', 'hail']
	

$ python weather.py
Daily forecast: like yesterday Weekly forecast:
1 snow
2 more snow
3 sleet
4 freezing rain
5 rain
6 fog
7 hail
```

