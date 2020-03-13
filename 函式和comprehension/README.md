# 函式和Comprehension
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

### 自訂函數沒接收沒傳回

```python
def func_sum():
	print("呼叫函式")
	return()

func_sum()

```

```python
>>> def do_nothing(): 
		pass

>>> do_nothing() 
>>>

```

```python

>>> def make_a_sound():
		print('quack')
		
>>> make_a_sound()
quack

```

#### Question: 請問執行後的結果哪一個是對的?(選擇題)
```python
def func_sum( ):
	print("A") 
	return( )
	
print("B") 
func_sum( ) 
print("C")
```
(1) A,B,C  
(2) B,A,C  
(3) C,B,A  
(4) A,C,B

#### Homework:
```python
#============================================================================
# Name        : function1.py
#定義函式，顯示「歡迎光臨」。
#============================================================================
```
[解題](function1.py)

###  自訂函數有接收沒傳回
```python
def func_sum(a, b):
	c = a + b
	print(c)
	return()

func_sum(3, 5)
```

####  Question:請問執行後的結果哪一個是對的?(選擇題)
```python
def func_sum(a, b): 
	c=a+b
	print(c)
	return( ) 
	
print("1") 
func_sum(3, 4) 
print("2")
```
(1) 1,7,2  
(2) 1,3,4,2  
(3) 3,4,1,2  
(4) 7,1,2

####  Question:請問執行後的結果哪一個是對的?(選擇題)
```python
def func_sum(a, b): 
	c=a+b
	print(c)
	return( ) 
	
print("1") 
func_sum( ) 
print("2")
```
(1) 1,0,2   
(2) 1,2  
(3) 0,1,2  
(4) 錯誤  

### 自訂函數有接收有傳回
```python
def func_sum(a, b):
	c = a + b
	return(c)
	
z = func_sum(10, 15)
```

```python

>>> def agree(): 
		return True 

>>> if agree():
		print('Splendid!')
	else:
		print('That was unexpected.')

Splendid!

>>> def echo(anything):
		return anything + ' ' + anything 
...
>>>

>>> echo('Rumplestiltskin')
'Rumplestiltskin Rumplestiltskin'

>>> def commentary(color):
		if color == 'red':
			return "It's a tomato."
		elif color == "green":
			return "It's a green pepper."
		elif color == 'bee purple':
			return "I don't know what it is, but only bees can see it."
		else:
			return "I've never heard of the color " + color + "."

>>> comment = commentary('blue')
>>> print(comment)

I've never heard of the color blue.
```

#### 操作範例:請動手操作，並留意輸出結果
```python
#fun2.py

def func_sum(a, b): 
	c=a+b
	return (c)
z = func_sum(10, 15) 
print(z)
``` 

####  請問執行後的結果哪一個是對的?(選擇題)
```python
def func_sum(a, b): 
	c = a + b * 2 
	return (c)
	
print("1")
z = func_sum(3, 4) 
print("2")
print(z)

```
(1) 1,7,2  
(2) 1,11,2  
(3) 1,2,11   
(4) 1,2,7  

#### Homework:
```python
#Name        : function2.py
#輸入攝氏溫度，求華氏溫度
#使用function
#=============================

攝氏10度轉華氏溫度=50
#==========================
請輸入攝氏溫度:19
華氏溫度=66.2

#===============================
```

#### Homework:
```python
#Name        : function3.py
#輸入攝氏溫度，求華氏溫度
#function 的原型宣告
#加上do...while()

#=============================

攝氏10度轉華氏溫度=50
#==========================
請輸入攝氏溫度:20
華氏溫度=68
程式還要繼續嗎?(輸入N....結束):h
請輸入攝氏溫度:40
華氏溫度=104
程式還要繼續嗎?(輸入N....結束):a
請輸入攝氏溫度:10
華氏溫度=50
程式還要繼續嗎?(輸入N....結束):N
程式結束

#===============================
```
[解題](function3.py)

###  函數傳回多值
- Python 的函數可以傳回多值。
- 傳回多值的做法是將傳回值轉為 tuple 型態，接收後再一一分配。

#### 操作範例 :請動手操作，並留意輸出結果
```python
#fun6.py

def func_a( ): 
	return 1, 2, 3, 4
	
temp = func_a( ) 
print(type(temp))
```

####  Question:請問執行後的結果哪一個是對的?(選擇題)
```python
def manyvalue(a, b): 
	c=a*b
	return (a-2, b+3, c)
	
x, y, z = manyvalue(3, 5) 
print(y)
```
(1) 8   
(2) 15   
(3) 1   
(4) 20   

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


def turbo(speed):
    print(id(speed))
    print('加速前速度:',speed[0])
    speed[0] += 10

if __name__ == '__main__':
    speed = list()
    print(id(speed))
    startSpeed = int(input('請輸入初始速度:'))
    speed.append(startSpeed)
    turbo(speed)
    print('加速後的速度:',speed[0])
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

 
## 使用Comprehensions語法快速簡潔方式建立tuple,list,dictionary,set
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

#使用list comprehension建立,可以有運算式靈活改變內容值

>>> number_list = [number-1 for number in range(1,6)] 
>>> number_list
[0,1,2,3,4]

```

```python

#使用lsit comprehension + for in + if
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



### Generators

```python
>>> sum(range(1, 101))
5050


def my_range(first=0, last=10, step=1):
	number = first
	while number < last:
		yield number
		number += step

>>> my_range
<function my_range at 0x10193e268>

>>> ranger = my_range(1, 5)
>>> ranger
<generator object my_range at 0x101a0a168>

for x in ranger: 
	print(x)

1
2 
3 
4
```

### Decorators
```python
def document_it(func):
	def new_function(*args, **kwargs):
		print('Running function:', func.__name__) 
		print('Positional arguments:', args) 
		print('Keyword arguments:', kwargs) 
		result = func(*args, **kwargs) 
		print('Result:', result)
		return result
	return new_function



def add_ints(a, b): 
returna+b

>>> add_ints(3, 5)
8

>>> cooler_add_ints = document_it(add_ints) # manual decorator assignment
>>> cooler_add_ints(3, 5) 
Running function: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
8


@document_it
def add_ints(a, b):
	returna+b

>>> add_ints(3, 5)
Start function add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
8



def square_it(func):
	def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
		return result * result
	return new_function


@document_it
@square_it
def add_ints(a, b):
	return a+b

>>> add_ints(3, 5)
Running function: new_function
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 64
64


@square_it
@document_it
def add_ints(a, b):
return a+b 

>>> add_ints(3, 5) 
Running function: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
64

```

### 命名空間和使用範圍(Namespaces and Scope)

```python
>>> animal = 'fruitbat'
def print_global():
	print('inside print_global:', animal)
	
	
>>> print('at the top level:', animal)
at the top level: fruitbat
>>> print_global()
inside print_global: fruitbat



def change_and_print_global():
	print('inside change_and_print_global:', animal)
	animal = 'wombat'
	print('after the change:', animal)


>>> change_and_print_global()
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	File "<stdin>", line 2, in change_and_report_it
UnboundLocalError: local variable 'animal' referenced before assignment



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

### 使用__name__,__doc__

```python

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



