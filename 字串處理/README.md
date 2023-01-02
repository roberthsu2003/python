# 字串的處理
### 字串表示式:
```python
>>> words = 'That is Alice's cat.'
>>> words = "That is Alice's cat."
```

### 脫逸字元

```
\' -> 單引號
\" -> 雙引號
\n -> "換行"
\t ->  "tab"
\\ -> "反斜線"

>>> print("Hello there!\nHow are you?\nI\'m doing fine.")

結果:=================
Hello there!
How are you?
I'm doing fine.
```

### 原始字串

```python
>>> print(r'That is Carol\'s cat.')
結果:=================
That is Carol\'s cat
```

### 單行文字

```python
>>> sentens = "Dear Alice,\
Eve's cat has been arrested for catnapping, cat burglary, and\
 extortion.\
Sincerely,\
Bob"

>>> print(sentens)

結果:===============
Dear Alice,Eve's cat has been arrested for catnapping, cat burglary, and extortion.Sincerely,Bob
```


### 多行文字

```python

>>> sentens = '''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob'''

>>> print(sentens)

結果:======================================
Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob
```

### 多行文字當作註解

```python
>>> """This is a test Python program.
Written by Al robert robert@gmail.com
This program was designed for Python 3, not Python 2.
"""

結果:=========================

```

### 計算字元數:len()

```python
#len()
>>> letters = 'abcdefghijklmnopqrstuvwxyz'
>>> print(len(letters))

>>> empty = ""
>>> print(len(empty))

結果:==================================
26
0
```

---
### 字引索引
###  索引編號與取值
- 字元依照順序排序:
	- 第一個字索引編號為 0，第二個字索引編號為 1。
	- 最後一個字索引編號為 -1，倒數第二個字索引編號為 -2。

---
###  索引編號與取值
- [n]
	- [ ]內可加入一個整數 n。
	- 代表由字串中取出固定索引欄位 n 的字元。
	- 由左向右存取，編號由 0 開始遞增。
	- 由右向左存取，編號由 -1 開始遞減。


```python
>>> letters = 'abcdefghijklmnopqrstuvwxyz'
>>> letters[0]
	'a'
>>> letters[1]
	'b'
>>> letters[-1]
    'z'
>>> letters[-2] 
    'y'
>>> letters[25]
    'z'
>>> letters[5]
    'f'
    
>>> letters[100]
Traceback (most recent call last):
File "<stdin>", line 1, in <module> 
IndexError: string index out of range


>>> name = 'Henny'
>>> name[0] = 'P'
Traceback (most recent call last): File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```
---

###  字串的切割slice
- [n : m]
	- 在一個範圍內找資料
	- n 與 m 均是一個整數
	- n 代表起始位置，第一個為 0。
	- m 是結束位置，不包含這個位置。




```python
#索引編號與取值:請留意輸出結果
#string3.py

>>> myString1="Hello World"
>>> print(myString1[0]) 
>>> print(myString1[2]) 
>>> print(myString1[-1]) 
>>> print(myString1[-2]) 
>>> print(myString1[2:]) 
>>> print(myString1[:3]) 
>>> print(myString1[1:4])

結果:================
H
l
d
l
llo World
Hel
ell 
```


| H | e | l | l | o |  | W | o | r | l | d |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7| 8 | 9 | 10 |
| -11 | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

---
```python
#[ start : end : step ]

>>> letters = 'abcdefghijklmnopqrstuvwxyz'
>>> letters[:]
    'abcdefghijklmnopqrstuvwxyz'

>>> letters[20:]
    'uvwxyz'

>>> letters[10:]
    'klmnopqrstuvwxyz'

>>> letters[12:15]
    'mno'

>>> letters[-3:] 
    'xyz'
    
>>> letters[18:-3] 
    'stuvw'
    
>>> letters[-6:-2] 
    'uvwx'
    
>>> letters[::7]
    'ahov'


>>> letters[4:20:3]
    'ehknqt'


>>> letters[19::4]
    'tx'


>>> letters[:21:5]
    'afkpu'

>>> letters[::-1] 
    'zyxwvutsrqponmlkjihgfedcba'
```
---

###  字串取代
- 語法:字串.replace(old, new[, max])
- replace方法 可以將指定的字串進行更換:
	- 字串.replace(舊字串, 新字串)
- replace方法 可以指定您要第幾個位置*後*不進行更換:
	- 字串.replace(舊字串, 新字串,替換不可以超過幾次)
	- 位置編號由 0 開始


```python
>>> name = 'Henny'
>>> name.replace('H', 'P') 
   'Penny'
>>> 'P' + name[1:] 
    'Penny'
```


```python
#字串取代:請留意輸出結果
#string4.py


>>>  str1 = "This is Python, That is Java; This is SQLite, That is MySQL"
>>> print("原本的字串:", str1)
>>> print()
>>> print("is 替換為 - :" + str1.replace("is", "-"))
>>> print()
=========================================
原本的字串: This is Python, That is Java; This is SQLite, That is MySQL

is 替換為 - :Th- - Python, That - Java; Th- - SQLite, That - MySQL



>>> str1 = "This is Python, That is Java; This is SQLite, That is MySQL"
>>> print("原本的字串:", str1)
>>> print()
>> print("加上參數值2:" + str1.replace("is", "-", 2))
=====================================
原本的字串: This is Python, That is Java; This is SQLite, That is MySQL

加上參數值2:Th- - Python, That is Java; This is SQLite, That is MySQL
```
---

###  字串內容搜尋

- 語法:字串.find(要搜尋的字串, beg=0, end=len(string))
- 字串可以搜尋特定內容的位置。
- 搜尋的字串位置編號由 0 開始。
- 字串.find(搜尋字串,起始位置,結束位置)
- 搜尋時不包含結束位置。
- 若搜尋不到則回傳 -1。
- 若沒有起始位置，也沒有結束位置，預設由 0 開始。
- 若沒有結束位置，預設到最後一個字。


```python
#字串內容搜尋:請留意輸出結果
#string5.py

>>> str1 = "this is Python Tutorial, there"
>>> search1 = "Python" 
>>> print(str1.find(search1)) #使用slice範例
=============================
8


>>> search2= "not" 
>>> print(str1.find(search2)) #使用判斷範例
================================
-1


>>>search3="t" 
>>> print(str1.find(search3)) 
=============================
0


>>> print(str1.find(search3,4)) 
================================
10

>>>print(str1.find(search3,11,20))
===============================
17
```

---

####  字串連接與分割
- 字串.join( ) : 於字串或著字元之間加入指定的文字
	- 連接符號字串.join(串列)
- 字串.split( ) : 將字串進行切割
	- 字串.split(分割符號)
	- 字串.split(分割符號,分割次數)

```python
#string6.py

>>> str1 = "-"
>>> str2 = ("a", "b", "c") 
>>> print(str1.join(str2))
=======================
a-b-c

>>> str2 = ("abc", “xyz", “123") 
>>> print(str1.join(str2))
========================
abc-xyz-123

 
>>> str3=":".join("Python") 
>>> print(str3)
======================
P:y:t:h:o:n

str4 = "python-java-c++-ruby" 
print(str4.split('-')) 
結果:=====================
[python, java, c++, ruby]
```



```python
#split()
>>> todos = 'get gloves,get mask,give cat vitamins,call ambulance' 
>>> todos.split(',')
結果:=====================
['get gloves', 'get mask', 'give cat vitamins', 'call ambulance']

```



```python
#join()
>>> crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster'] 
>>> crypto_string = ', '.join(crypto_list)
>>> print('Found and signing book deals:', crypto_string)

結果:=====================
Found and signing book deals: Yeti, Bigfoot, Loch Ness Monster

```

---

```python
#字串常用的一些操控
#字串的method

>>> poem = '''All that doth flow we cannot liquid name Or else would fire and water be the same;
But that is liquid which is moist and wet Fire that property can never get. Then 'tis not cold that doth the fire put out But 'tis the wet that makes it die, no doubt.'''


>>> poem[:13]
    'All that doth'
    
>>> len(poem)
    250

>>> poem.startswith('All')
True


>>> poem.endswith('That\'s all, folks!')
False


>>> word = 'the' 
>>> poem.find(word) 
    73


>>> poem.rfind(word)
    214
    

>>> poem.count(word)
    3

```

---

```python
#字串常用的一些操控
#字串的method

>>> setup = 'a duck goes into a bar...'

>>> setup.strip('.')
'a duck goes into a bar'

>>> setup.capitalize()
'A duck goes into a bar...'

>>> setup.title()
'A Duck Goes Into A Bar...'

>>> setup.upper()
'A DUCK GOES INTO A BAR...'

>>> setup.lower()
'a duck goes into a bar...'

>>> setup.swapcase()
'a DUCK GOES INTO A BAR...'

>>> setup.center(30)
    '  a duck goes into   '

>>> setup.ljust(30) 
   'a duck goes into a bar... '

>>> setup.rjust(30)
    ' a duck goes into a bar...'

#replace()
>>> setup.replace('duck', 'marmoset') 
   'a marmoset goes into a bar...'

```

---

### 使用isX()method
- isalpha() 只可以是英文字母,不可以有空白
- isalnum() 只可以是英文字母或數字，不可以有空白
- isdecimal() 只可以是數字，不可以有空白
- isspace() 是否有空白
- istitle() 每個字的第一個字元必需是大寫

```python
>>> 'hello'.isalpha() 
True

>>> 'hello123'.isalpha() 
False

>>> 'hello123'.isalnum() 
True

>>> 'hello'.isalnum() 
True

>>> '123'.isdecimal() 
True

>>> ' '.isspace() 
True

>>> 'This Is Title Case'.istitle()
True

>>> 'This Is Title Case 123'.istitle()
True

>>> 'This Is not Title Case'.istitle()
False

>>> 'This Is NOT Title Case Either'.istitle()
False
```

#### 輸入檢查

```python
while True:
    print('請輸入age:')
    age = input()
    if age.isdecimal():
        break
    print('請輸入一個數字:')

while True:
    print('請輸入密碼(只可以是數字或英文字母):')
    password = input()
    if password.isalnum():
        break
    print('密碼只可以是數字或英文字母')

print(name)
print(password)
```

### 文字對齊rjust(), ljust(), and center()

```python
>>> 'Hello'.rjust(10)
'     Hello'

>>> 'Hello'.rjust(20)
'                Hello'

>>> 'Hello, World'.rjust(20)
'         Hello, World'
 
>>> 'Hello'.ljust(10) 
'Hello     '

>>> 'Hello'.rjust(20, '*')
'***************Hello'

>>> 'Hello'.ljust(20, '-')
'Hello---------------'

>>> 'Hello'.center(20, '=')
'=======Hello========'
```

#### 對齊應用:

```python
>>> def printPicnic(itemsDict, leftWidth, rightWidth):
>>>    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
>>>    for k, v in itemsDict.items():
>>>        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

>>> picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
>>> printPicnic(picnicItems, 12, 5)
>>>  printPicnic(picnicItems, 20, 6)

結果:===========================
---PICNIC ITEMS--
sandwiches..    4
apples......   12
cups........    4
cookies..... 8000
-------PICNIC ITEMS-------
sandwiches..........     4
apples..............    12
cups................     4
cookies.............  8000
```

#### homeword
- 將上面對齊應用輸出為文字檔.(必需會檔案的存取)

#### homeword
-將上方多行文字，轉變為下方符號串列
-將上方多行文字，轉變為下方數字串列

```python
Lists of animals
Lists of aquarium life
Lists of robert by author abbreviation
Lists of cultivars

結果=====================
* Lists of animals
* Lists of aquarium life
* Lists of robert by author abbreviation
* Lists of cultivars


結果=====================
1. Lists of animals
2. Lists of aquarium life
3. Lists of robert by author abbreviation
4. Lists of cultivars

```

#### homeword
- 將上方的list輸出成為下方的樣子

```python
>>> tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
					   ['dogs', 'cats', 'moose', 'goose']]
					   
結果:===========================
  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
```



### in 和 not in 操作字串

```python
>>> 'Hello' in 'Hello, World' True
>>> 'Hello' in 'Hello'
True
>>> 'HELLO' in 'Hello, World' False
>>> '' in 'spam'
True
>>> 'cats' not in 'cats and dogs' False
```

### 字串使用(+)運算子

```python
>>> name = 'Robert'
>>> age = 40
>>> 'Hello, my name is ' + name + '. I am ' + str(age) + ' years old.' 
==============================
'Hello, my name is Robert. I am 40 years old.'
```
---

### 字串使用(%)運算子

```python
>>> name = 'Robert'
>>> age = 40
>>> 'Hello, my name is  %s. I am  %d years old.' % (name,age)
結果:==============================
'Hello, my name is  Robert. I am  40 years old.'
```

### 使用字串插補

```python
>>> name = 'Robert'
>>> age = 40
>>> f'Hello, my name is  {name:s}. I am  {age:d} years old.'
結果:==============================
'Hello, my name is  Robert. I am  40 years old.'
```

