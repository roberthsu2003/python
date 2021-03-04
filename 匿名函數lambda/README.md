# 暱名函數與套件的使用
### 函數 Are First-Class Citizens

```python
#定義和呼叫function
>>> def answer(): 
		print(42)

>>> answer()
42
```

```python
#將function當作參數
>>> def run_something(func): 
		func()

>>> run_something(answer) 
42
```


```python
#有引數的參數
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
#沒有限定參數的數量
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


####  Homework:匿名函數操作
- 目前有一個list，內容為"apple", "banana", "papaya", "watermelon"
- 請利用匿名函數於這些資料後面加上!!!
- 輸出為

```python
['apple!!!', 'banana!!!', 'papaya!!!', 'watermelon!!!']
```

--- 






