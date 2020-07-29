# 數值與函式的進階運用
###  輸出資料格式化
- 數值資料若要與字串一併輸出，必須加上 str( ) 進行轉換才可以。
- 各種資料輸出可透過格式代碼進行輸出多少位數資料的格式化設定。
- 格式可區分為整數、浮點數與文字三種。
- 資料輸出時可指定格式。

### 整數資料格式代碼可以分為十進位、八進位與十六進位:

| 整數資料格式代碼 | 輸出方式 |
|:--|:--|
| %d、%i | 以十進位方式輸出 |
| %o | 以八進位方式輸出 |
| %x、%X | 以十六進位方式輸出 |

### 浮點數的格式代碼

| 格式代碼 | 說明 |
|:--|:--|
| %f、%F | 輸出浮點數 |
| %e、%E | 科學記數法 |
| %g、%G | 自己判斷 %f 或者 %e 輸出 |

### 文字資料的格式代碼
| 整數資料格式代碼 | 輸出方式 |
|:--|:--|
| %s | 以字串方式輸出 |
| %c | 以字元方式輸出 |

###  輸出資料格式化
格式化輸出方式:   

- print("輸出字串與格式代碼"%(變數))
- 若是兩個變數則用逗點隔開。

例如要輸出 123 這個整數值，輸出樣式為:  

- print( “%d” % ( 123 ) )

###  整數與字元與字串的輸出
%d、%c 與 %s 的 % 符號與後面格式代碼之間可以加入一個整數值， 代表資料輸出位數:

- 若整數的絕對值小於現有資料輸出位數，則資料仍依照現有位數進行輸出。
- 若整數的絕對值大於現有資料輸出位數:
	- 若是正數則向右對齊。
	- 若是負數則向左對齊。

#### 字串的輸出:請留意輸出結果
```python
#format2.py


c='我' 
print("1*%c*" % (c))
print("2*%5s*" % (c))
print("3*%-5s*" % (c))
print("4*%2s*" % (c))
 
```

###  浮點數資料輸出
%f 的 % 符號與後面代碼之間可以加入兩個整數值，我們以「n.m」 來表示，代表資料輸出位數:

- m 代表小數位數:
	- 大於實際小數位數，比如說我們規劃 6 個位置，但小數實際上只有 3 個位置，補0。
	- 小於實際小數位數，比如說我們規劃 3 個位置，但小數實際上有 6 個位置，下 一位數的值若大於等於 6 進位。
	- n 的絕對值代表整數加上小數加上「.」的總和:
	- 若 n 的絕對值小於現有資料輸出位數，則資料仍依照現有位數進行輸出。
	- 若 n 的絕對值大於現有資料輸出位數:
		- 若是正數則向右對齊。
		- 若是負數則向左對齊。

#### 浮點數資料輸出:請留意輸出結果
```python
# format3.py

 b=123.926 
 print("5*%d*" % (b)) 
 print("6*%7.2f*" % (b)) 
 print("7*%-9.4f*" % (b)) 
 print("8*%.2f*" % (b))
```

#### Question: 請問如何產生以下結果?(選擇題)

| * |  |  | 2 | 3 | . | 4 | 6 | * |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

```python
(1) print("*%7.2f*"%(23.462))  
(2) print("*%6.2f*"%(23.462))
(3) print("*%6.3f*"%(23.462))
```

###  浮點數的問題
- 浮點數為二進位環境下的處理，數值資料無法精準處理。
- 之前的格式化動作是希望資料能以我們設定的位數顯示。
- 建議可引用 decimal 模組，改為十進位的方式操作。
	- from decimal import *

#### 操作範例:請動手操作，並留意輸出結果
```python
# floata1.py

from decimal import *
print(1.1 + 2.2)
print(Decimal('1.1') + Decimal('2.2'))

print(0.1 + 0.1 + 0.1 - 0.3)
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

print(1.20 + 1.30)
print(Decimal('1.20') + Decimal('1.30'))
```

##  list 傳送與接收
- 傳送與接收資料可以使用 list。
- 傳送與接收都是相同的位址上的資料。
- list 內可以更新單一資料或著調整(append、extend、insert、remove、pop、del) 資料。
- list 若以指派方式設定為新的list:
	- list 若以指派方式設定為新的list.
	- 原來 list 沒有變更.

#### 操作範例 1:請動手操作，並留意輸出結果  
```python
#fun4.py

def changeme( mylist ): 
	print(id(mylist)) 
	mylist[2]='a' 
	print(id(mylist))
	print ("函數內: ", mylist) 
	return( )
	
mylist = [10,20,30] 
print(id(mylist))
changeme( mylist )
print ("執行完函數:", mylist)
 
```

#### 操作範例 2:請動手操作，並留意輸出結果
```python
#fun4-1.py

def changeme( mylist ): 
	print(id(mylist)) 
	mylist = [1,2,3,4] 
	print(id(mylist))
	print ("函數內: ", mylist) 
	return( )
	
mylist = [10,20,30] 
print(id(mylist))
changeme( mylist )
print ("執行完函數:", mylist) 
```

#### 操作範例 3:請動手操作，並留意輸出結果
```python
#fun4-2.py

def changeme( mylist ): 
	print(id(mylist)) 
	mylist.append([1, 2]) 
	print(id(mylist))
	print ("函數內: ", mylist) 
	return( )

mylist = [10,20] 
print(id(mylist))
changeme( mylist )
print ("執行完函數:", mylist) 
```

###  list 計算式與固定間隔取值
- 於 list 使用上，+= 與 = 代表意義不同。
- += 於使用上具有修改資料結構本身，而 = 是重新分配資料內容。
- 所以 x+=1 會在*原本的位置上進行修改*，但 x=x+1 則是*分配到新的位置*。
- List 的取值動作除了起始與結束，也可以加入第三個參數:固定間隔。

#### 操作範例:請動手操作，並留意輸出結果
```python
#list-add1.py

x=y=[0,1,2] 
print(x,y) 
print(id(x)) 
print(id(y))
 
x=x+[89,99] 
print(x,y) 
print(id(x)) 
print(id(y)) 
print(x is y)
```

#### 操作範例:請動手操作，並留意輸出結果
```python
#list-add2.py

a=b=[0,1,2]
print(a,b) 
print(id(a)) 
print(id(b))
 
a+=[89,99] 
print(a,b) 
print(id(a)) 
print(id(b)) 
print(a is b)
```

#### 操作範例:請動手操作，並留意輸出結果

```python

#list-try.py

x=range(100) 
for i in x[::-1]:
	print(i)

for i in x[::2]:
	print(i)

for i in x[::3]: 
	print(i)
	
for i in x[10:40:6]:
	print(i)
```

## 趨向於函數導向的設計方式
- 專注於功能的操作，而不需要考慮資料放外面或著放裡面。
- 每一個函數都是獨立的，也可以透過 import 方式引用。
- list 區塊內可以加入迴圈與條件分析語法，讓 list 專注於產生自己所 需資料，不需要連結到其他區塊進行作業。

#### 操作範例 1-1:請動手操作，並留意輸出結果
```python
# fun9.py

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
y = [x + 10 for x in values]
print(y)
z = [x for x in values if x % 2 == 0] 
print(z)
```

###  關於函數的後續思考
1. 如果呼叫函數時忽略傳遞參數資料，該如何避免錯誤產生?
	- Python 可建立接收初始值設定。  

2. 由於呼叫函數時可以傳遞參數，但執行函數時可能會有不同的參數數量傳遞，但執行相同事情，需要建立不同的函數嗎?  
	- Python 可使用不定接收參數方式設計函數。 

3. 若只有一個計算式或表達分析語法，若定義一個函數後再呼叫執行顯得沒有效率，那如何規劃進行呢?  
	- Python 可使用匿名函數方式進行規劃。



### 引數位置呼叫

```python
>>> def menu(wine, entree, dessert):
    return {'wine': wine, 'entree':entree, 'dessert': dessert}

>>> menu('白酒', '牛排', '蛋糕')
{'wine': '白酒', 'entree': '牛排', 'dessert': '蛋糕'}

>> menu('紅酒', '雞排', '冰淇淋')
{'wine': '紅酒', 'entree': '雞排', 'dessert': '冰淇淋'}

```

### 引數名稱名稱呼叫

```python
#引數名稱呼叫
#可以不依照順序
>>> menu(entree='牛排', dessert='冰淇淋', wine='白酒')
{'dessert': 'bagel', 'wine': 'bordeaux', 'entree': 'beef'}
```

### 引數位置和引數名稱混合呼叫  
```
#前面一定先用引數位置,後面使用引數名稱
#使用引數名稱後,就不可以再使用引數位置

>>> menu('紅酒', dessert='蛋糕', entree='雞排')
{'wine': '紅酒', 'entree': '雞排', 'dessert': '蛋糕'}

```

### 指定預設參數的值

```python
>>> def menu(wine, entree, dessert='奶昔'):
	    return {'wine': wine, 'entree':entree, 'dessert': dessert}

#呼叫時,可省略有預設參數的值
>>> menu('紅酒','雞排')
{'wine': '紅酒', 'entree': '雞排', 'dessert': '奶昔'}

#呼叫時,不省略預設的參數值
>>> menu('紅酒','雞排','蛋糕')
{'wine': '紅酒', 'entree': '雞排', 'dessert': '蛋糕'}

>>> menu('紅酒','雞排',dessert='蛋糕')
{'wine': '紅酒', 'entree': '雞排', 'dessert': '蛋糕'}
```

```python

>>> def buggy(arg, result=[]):
		result.append(arg)
		print(result) 
		...
>>> buggy('a')
['a']
>>> buggy('b') # expect ['b'] 
['a', 'b']

```

```python

>>> def works(arg):
		result = []
		result.append(arg)
		return result
...
>>> works('a')
['a']
>>> works('b')
['b']

```

```python

>>> def nonbuggy(arg, result=None):
		if result is None:
			result = []
		result.append(arg)
		print(result) 
...
>>> nonbuggy('a') 
['a']
>>> nonbuggy('b')
['b']

```



###  接收參數設定
1. 函數若有接收參數，執行時就必須給他參數。
2. 函數接收資料時參數若有初始值，執行時若沒有給值就會使用那些初始值。
3. 如果函數接收資料時參數沒有初始值，執行時就必須給他參數，且參 數數量必須相同。

#### 操作範例 :請動手操作，並留意輸出結果
```python
# fun5-2.py

def printinfo( name="may", age=20 ): 
	print ("Name: ", name)
	print ("Age ", age)
	print("-----------")
	return( )

printinfo(50,"miki" ) 
printinfo( ) 
printinfo("John") 
printinfo(300) 
printinfo('max',45) 
```

####  Question:請問執行後的結果哪一個是對的?(選擇題)
```python
def test2( name="may", age=20 ): 
	print (name,age)
	return( )
	
test2(200)
```

(1) 200,20  
(2) 20,200  
(3) may,20  
(4) may,200  

### 使用*參數,可接收不限數量的位置引數

```python
>>> def print_args(*args):
		print('Positional argument tuple:', args) 
...

>>> print_args()
Positional argument tuple: ()

>>> print_args(3, 2, 1, 'wait!', 'uh...')
Positional argument tuple: (3, 2, 1, 'wait!', 'uh...')

>>> def print_more(required1, required2, *args): 
		print('Need this one:', required1)
		print('Need this one too:', required2) 
		print('All the rest:', args)
		
>>> print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')	

Need this one: cap
Need this one too: gloves
All the rest: ('scarf', 'monocle', 'mustache wax')


```

### 使用**參數,呼叫使可使用不限數量的引數名稱

```python
>>> def print_kwargs(**kwargs):
		print('Keyword arguments:', kwargs) 
...

>>> print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

Keyword arguments: {'dessert': 'macaroon', 'wine': 'merlot', 'entree': 'mutton'}

```

### 不固定接收數量
1. ( ) 內接收資料若是以 * 表示代表可以引入不定數量的參數:
	- *代表以 tuple 的方式引入
	- **代表以 dict 的方式引入
2. 接收資料若需加入多個設定，這些設定請依照順序排列:
	- 第一個參數設定為接收值
	- 第二個參數設定為初始值
	- 第三個參數設定為不固定值，可以是 tuple 或 dict 方式
	- 
#### 操作範例 1:請動手操作，並留意輸出結果
```python
# fun7-1.py
def fun3(arg1,arg2='default',*arg3 ): 
	print("arg1:",arg1)
	print("arg2: ",arg2)	
	for each_arg in arg3:
		print ("each_arg: ", each_arg) 

fun3(1)
fun3(1, 2) 
fun3(1, 2, 3)
```

#### 操作範例 2:請動手操作，並留意輸出結果
```python
# fun7-1a.py
def fun3(arg2='default',arg1,*arg3): 
	print("arg1:",arg1)
	print("arg2: ",arg2)
	for each_arg in arg3:
		print("each_arg: ", each_arg)


fun3(1)
fun3(1, 2) 
fun3(1, 2, 3, 5) 
```

#### 操作範例 3:請動手操作，並留意輸出結果
```
#python7-1b.py

def fun3(arg2='default',*arg3): 
	print("arg2: ",arg2)
	for each_arg in arg3:
		print("each_arg: ", each_arg)

fun3( ) 
print("---A---") 
fun3(1)
 
print("---B---") 
fun3(1, 2) 

print("---C---") 
fun3(1, 2, 3,5)
```

#### 操作範例 4:請動手操作，並留意輸出結果
```python
#fun7-1c.py
def fun3(*arg3):
	for each_arg in arg3:
		print ("each_arg: ", each_arg) 
	print(arg3)

fun3( ) 

print("---A---") 
fun3(1) 

print("---B---") 
fun3(1, 2) 

print("---C---") 
fun3(1, 2, 3,5)
```

#### 操作範例 5-1:請動手操作，並留意輸出結果
```python
# fun7-2.py

def fun4(arg1,arg2='default',**arg4 ):
	print("arg1:",arg1)
	print("arg2: ",arg2)
	for each_arg2 in arg4.keys():
		print("arg4: %s=>%s" % ( each_arg2, str(arg4[each_arg2])))

fun4(1)
fun4(1, 2)
fun4(1, 2, a="b") 
```

####  Question:請問執行後的結果哪一個是對的?(選擇題)
```python
def fun3(arg1,arg2=300,*arg3 ): 
	sum = 0
	sum+=arg1 
	sum+=arg2
	for each_arg in arg3:
		sum+=each_arg 
		print(sum)
	
fun3(1, 2, 3,4,5)
```
(1) 3   
(2) 15   
(3) 6   
(4) 9  

#### HomeWork:回文偵測
- 輸入多個字串為一個 list 清單。
- list 清單的每一個資料進行分析， 判斷是否為回文。所謂的回文是 指從頭到尾與從尾到頭都是一樣 的內容，例如 1221。
- 取出字串若為 x，分析比較的對象 為 "".join(reversed(x))。

```python
請輸入字串, 當您輸入0就代表結束:
請輸入:1221
請輸入:abba
請輸入:3456
請輸入:0
顯示清單內容:
['1221', 'abba', '3456']

符合回文的字串為:
['1221', 'abba']
```

### Docstrings

```python
>>> def echo(anything):
		'echo returns its input argument'
		return anything

```

```python
		
>>> def print_if_true(thing, check): 
		'''Prints the first argument if a second argument is true. The operation is:
		1. Check whether the *second* argument is true.
		2. If it is, print the *first* argument. 
		'''
		if check: 
			print(thing)
			
>>> help(echo)
Help on function echo in module __main__:

echo(anything)
	echo returns its input argument
	
>>> print(echo.__doc__)
echo returns its input argument

```

