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



## Python 正規表示式模組 (re) 簡介
- 正規表示式以及 Python re 模組中定義的正規表示式操作。

- re 是 Python 的標準庫，它支援正規表示式的匹配操作。

- Python 中的正規表示式是一組字元或序列，用於使用正式語法將字串與另一個模式匹配。你可以將正規表示式視為嵌入在 python 中的小型程式語言。

- 你可以使用正規表示式來定義一些規則，然後使用這些規則從你希望與模式匹配的給定字串中建立可能的字串。Python 中的正規表示式被解釋為一組指令。

- [regex pal 正規表示式模擬測試網站](https://www.regexpal.com)

---

###  為何需要正規則表達式
#### 檢查台灣手機號碼輸入格式(xxxx-xxx-xxx)


```python
# 檢查台灣手機號碼輸入格式(xxxx-xxx-xxx)
# 沒有使用正規則表達式

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    if not text[0:4].isdecimal():
        return False
    if text[4] != "-":
        return False
    if not text[5:8].isdecimal():
        return False
    if text[8] != "-":
        return False
    if not text[9:12].isdecimal():
        return False
    return True
    
phone_num = input("請輸入手機號碼xxxx-xxx-xxx:")
if isPhoneNumber(phone_num):
    print(f"您的手機號碼是:{phone_num:s}")
else:
    print("手機號碼格式不正確")
```

```python
#使用正規則表達式
import re
def isPhoneNumber(text):
    phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
    match = re.match(phoneNumRegex,text)
    if re.match(phoneNumRegex,text) is None:
        return False
    else:
        print(match.group())
        return True

phone_num = input("請輸入手機號碼xxxx-xxx-xxx:")
if isPhoneNumber(phone_num):
    print(f"您的手機號碼是:{phone_num:s}")
else:
    print("手機號碼格式不正確")
```

[python 正規則表達式測試網站](https://pythex.org)

```python
#正規則表達式使用()符號
import re
def isPhoneNumber(text):
    phoneNumRegex = re.compile(r'(\d\d\d\d)-(\d\d\d)-(\d\d\d)')
    match = re.match(phoneNumRegex,text)
    if re.match(phoneNumRegex,text) is None:
        return False
    else:
        print(match.group(0))
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))
        return True

phone_num = input("請輸入手機號碼xxxx-xxx-xxx:")
if isPhoneNumber(phone_num):
    print(f"您的手機號碼是:{phone_num:s}")
else:
    print("手機號碼格式不正確")
    
結果:=======================
0926-444-333
0926
444
333
您的手機號碼是:0926-444-333
```

在正規則表達式中，有特殊意義的符號

```python
. ^  $ * + ? { } [] \ | ( )
```

如果在正規則表達式中,要搜尋這些特殊字元,必需在前面加上脫逸字元(\)

```python
\. \^ \$ \* \+ \?  \{  \}  \[  \]  \\  \|  \(  \)
```

```python
import re
def isPhoneNumber(text):
    phoneNumRegex = re.compile(r'(\(\d\d\d\d\))-(\d\d\d)-(\d\d\d)')
    match = re.match(phoneNumRegex,text)
    if re.match(phoneNumRegex,text) is None:
        return False
    else:
        print(match.group(0))
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))
        return True

phone_num = input("請輸入手機號碼xxxx-xxx-xxx:")
if isPhoneNumber(phone_num):
    print(f"您的手機號碼是:{phone_num:s}")
else:
    print("手機號碼格式不正確")

結果:=================================
(0926)-666-000
(0926)
666
000
您的手機號碼是:(0926)-666-000
```

### 使用pipe(|),選擇多選1

```python
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.match('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.match('Tina Fey and Batman')
print(mo2.group())

結果:========================
Batman
Tina Fey
```

### 同時使用 () 和 |符號

```python
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

結果:========================
Batmobile
mobile
```

### optional matching with ?
-zero或1次

```python
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')

print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

結果:================================
Batman
Batwoman
```

### asterist(*),zero or more

```python
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

結果:==============================
Batman
Batwoman
Batwowowowoman
```

### + one or more

```python
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
print(mo3  ==  None)

結果:=======================
Batwoman
Batwowowowoman
True
```

### 指定次數: {}
- (ha){3} -> 3次
- (ha){3,5} -> 3-5次
- (ha){,5} -> 0-5次
- (ha){3,} -> 3次以上

```python
(ha){3}
(ha)(ha)(ha)
```

```python
(ha){3,5}
((ha)(ha)(ha))|((ha)(ha)(ha)(ha))|((ha)(ha)(ha)(ha)(ha))
```

```python
haRegex = re.compile(r'(ha){3}')
mo1 = haRegex.search('hahaha')
print(mo1.group())

mo2 = haRegex.search('ha')
print(mo2  == None)

結果:======================
hahaha
True
```

### Greedy(最多次數) and Non-greedy(最少次數) Matching

```python
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

結果:===========================
HaHaHaHaHa
HaHaHa
```

### findall() method
- search()搜尋到最前一個match
- findall()搜尋所有match

```python
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work:212-555-0000')
print(mo.group())
li = phoneNumRegex.findall('Cell: 415-555-9999 Work:212-555-0000')
print(li)

結果:======================
415-555-9999
['415-555-9999', '212-555-0000']
```

###  findall 和 group()結合

```python
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
li = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(li)

結果:============================
[('415', '555', '9999'), ('212', '555', '0000')]
```

### 字元集
- \d -> (0|1|2|3|4|5|6|7|8|9)
- \d -> 0-9
- \D -> 不是0-9
- \w -> 任何字元,數字,和底線
- \W -> 不是(任何字元,數字,和底線)
- \s -> 任何空白,tab或者newline
- \S -> 不是(任何空白,tab或者newline)
- [0-5] -> 0-5任一個
- [0-9] -> 0-9任一個
- [a-z] -> a-z任一個
- [a-zA-Z] -> a-z,A-Z任一個

```python
xmaxRegex = re.compile(r'\d+\s\w+')
li = xmaxRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings,4 birds, 3 hens, 2 doves, 1 partridge')
print(li)

結果:================================
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
```

### 建立自已的字元集

```python
vowelRegex = re.compile(r'[aeiouAEIOU]')
li = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(li)

結果:===========================
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
```

- [.*?] -> 在中括號內的特殊符號，可以不用使用脫逸字元
- [ ^ ]  -> 在中括號內的最前面的^,代表的是negative character class

```python
consonantRegex = re.compile(r'[^aeiouAEIOU]')
li = consonantRegex.findall('RoboCop  eats baby food. BABY FOOD.')
print(li)

結果:==========================
['R', 'b', 'C', 'p', ' ', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
```

### ^ 和 $ 符號
- ^ -> 起始
- $ -> 結束

```python
beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello, world!')
print(mo.group())
print(beginsWithHello.search('He said hello.') == None)

結果:===============================
Hello
True
```


```python
endsWithNumber = re.compile(r'\d$')
mo = endsWithNumber.search('Your number is 42')
print(mo.group())

print(endsWithNumber.search('Your number is forty two.') == None)

結果:=======================
2
True
```

```python
wholeStringIsNum = re.compile(r'^\d+$')
mo = wholeStringIsNum.search('1234567890')
print(mo.group())

print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12  67890') == None)

結果:==========================
1234567890
True
True
```

### (.) Wildcard 字元

- (.)符號 -> 除了new line以外的所有字元

```python
atRegex = re.compile(r'.at')
li = atRegex.findall('The cat in the hat sat on the flat mat.')
print(li)

結果:==============================
['cat', 'hat', 'sat', 'lat', 'mat']
```

#### .* Matching Everything(greedy)

```python
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Robert Last Name: Hsu')
print(mo.group())
print(mo.group(1))
print(mo.group(2))

結果:=======================
First Name: Robert Last Name: Hsu
Robert
Hsu
```

#### .*? Matching Everything(non-greedy)

```python
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex =  re.compile(r'<.*>')
mo1 =  greedyRegex.search('<To serve man> for dinner.>')
print(mo1.group())

結果:========================
<To serve man>
<To serve man> for dinner.>
```

####  (.*)也包含new line(re.DOTALL)

```python
noNewLineRegex = re.compile('.*')
mo = noNewLineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.')
print(mo.group())

newlineRegex = re.compile('.*', re.DOTALL)
mo1 = newlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.')
mo1.group()

結果:===============================
Serve the public trust.
'Serve the public trust.\nProtect the innocent. \nUphold the law.'
```

#### 不分大小寫(re.IGNORECASE)

```python
robocop = re.compile(r'robocop', re.I)
mo = robocop.search('RoboCop is part man, part machine, all cop.')
print(mo.group())

mo1 = robocop.search('ROBOCOP protects the innocent.')
print(mo1.group())

mo2 = robocop.search('Al, why does your programming book talk about robocop so much?')
print(mo2.group())

結果:=================================
RoboCop
ROBOCOP
robocop
```

### sub() 替換字串

```python
namesRegex = re.compile(r'Agent \w+')
str1 = namesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')
print(str1)

結果:==================
CENSORED gave the secret documents to CENSORED.
```

```python
agentnamesRegex = re.compile(r'Agent (\w)\w+')
str1 = agentnamesRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(str1)

結果:========================
A**** told C**** that E**** knew B**** was a double agent.
```

### 複雜的正規則表達式寫法,使用re.VERBOSE,可以使用空白和註解

```python
#美國,加拿大,電話號碼
phoneRegex = re.compile(r'''
        (\d{3}|\(d{3}\))  #區域碼
        (\s|-|\.)?        #separator
        \d{3}             #first 3 digits
        (\s|-|\.)         #separator
        \d{4}             #last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?   #extension
''',re.VERBOSE)
```

```python
#email
emailRegex = re.compile()
```







### match() 函式
- 你可以使用 match() 函式將 RE 模式與給定字串來匹配。match() 函式也包含了標誌，標誌定義正規表示式的行為，它可以有不同的值
 
```python
re.match(pattern, string, flags=0)

#它有三個引數:
pattern 是要匹配的正規表示式模式
string 是與正規表示式匹配的給定字串
flags 用於更改正規表示式的行為，這是個可選項

如果匹配成功就返回 Match 物件，否則返回 NONE。
返回的匹配物件 Match 還有兩個主要方法，即 group(num=0)。
可以使用這些方法來分別返回匹配的特定子序列和所有子序列。

re.match只匹配字串的開始，如果字符開始不符合正则表達式，则匹配失败
```



```python
#使用 match 函式

import re

strText = "Hello Python Programming"
matchObjec = re.match(r"hello", strText, re.I)
if matchObjec is None:
    print("文字最前面沒有搜尋到")
else:
    print("文字最前面搜尋到%s" % matchObjec.group())

#在此示例中，使用字首 r 來表示字串是原始字串。在原始字串中，在使用轉義序列時不需要寫雙斜槓，例如，如果你想要一個反斜槓，那麼你只需要一個\，而不用像普通字串那樣的雙反斜槓\\。
```

```python
import re
 
line = "Cats are smarter than dogs"
 
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")

輸出結果:========================
matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter
```

---

### search() 函式

search 函式搜尋整個字串

你可以使用 search() 函式搜尋給定字串中的正規表示式匹配模式。search 有三個輸入引數，匹配模式，給定字串以及可選的匹配行為選項 flags

```python
re.search(pattern, string, flags)
```

```pytnon

import re
str = "Hello Python Programming"
searchObject = re.search(r"programming", str, re.I)
if not searchObject:
    print("文字內沒有搜尋到任何相同內容")
else:
    print("文字內搜尋到%s" % searchObject.group())
    print("文字內搜尋到的位置是",searchObject.span())
    print(str[13:24])
    
輸出結果:================
文字內搜尋到Programming
文字內搜尋到的位置是 (13, 24)
Programming
    
```

在此程式碼中，我們來搜尋給定字串中是否存在 programming，search 函式搜尋整個字串。
- 搜尋 search 和匹配 match 之間的區別在於 match 函式只檢查字串的開頭，而 search 在整個字串中搜尋。

---

### 在字串開頭搜尋
- 果你想在字串的開頭搜尋，那麼可以使用^。來看下例

```python
#在字串開頭搜尋

import re
str = "Hello Python Programming"
sobj = re.search(r"^programming", str, re.I)
print(sobj) #no match is found

sobj = re.search(r"^hello", str, re.I)
print(sobj.group()) #matching: Hello
```

這裡，^ 的意思是隻在字串的開頭進行搜尋，假如開頭不匹配的話，就返回 None，而不管字串後續中有沒有再匹配到。

---

### 在字串結尾搜尋
- 你也可以在給定字串的末尾搜尋，通過在模式後面加 $ 來限定。

```python
#在字串結尾搜尋
import re
str = "Hello Python Programming"
sobj = re.search(r"programming$", str, re.I)
print(sobj.group()) #matching: Programming

sobj = re.search(r"hello$", str, re.I)
print(sobj) #no match found
```

---

### 編譯正規表示式
- Python 中的正規表示式在編譯時將轉換為模式，這些模式實際上是包含不同功能的模式物件，以執行不同的任務，包括搜尋，匹配和替換等。

- 編譯模式後，你可以稍後在程式中使用該模式。 



### 使用預編譯的模式
- 在下面的例子中，被編譯的模式 r"\d" 意思是在字串中的第一個數字。當該模式後續跟 search 一起使用的時候，它搜尋輸入字串中的一個數字；同樣的，你也可以用這個模式跟 match 搭配來找到給定字串中的匹配。

```python
#使用預編譯的模式

import re
compPat = re.compile(r"\d")
sobj = compPat.search("Lalalala 123")
print(sobj.group())

mobj = compPat.match("234Lalalala 123456789")
print(mobj.group())
```
--- 

### 標誌位 flags
- 你可以使用標誌位 flags 來改變正規表示式的行為。在正則函式中，標誌位是可選項。你可以通過兩種不同的方式來使用標誌，即使用關鍵字 flags 併為其分配標誌值或直接寫入標誌位的值。你可以設定多個標誌位，這可以通過使用按位或運算|符來完成。
下表列出了正規表示式的一些常用標誌

| 標誌位 | 說明 |
|:--|:--|
| re.I | 在匹配時忽略字串和模式的大小寫 |
| re.M | $ 匹配行末尾，而不是字串末尾，同理^匹配行開頭而不是字串開頭 |
| re.S | . 匹配任何字元，也包括新的一行|
| re.U | 使用 Unicode 字符集 |
| re.X | 忽略各種空格以及以 # 開頭的註釋，這使得長匹配模式可以分行來寫，提高了可讀性 |

```python
import re
s = re.search("L", "Hello")
print(s)		#Output: None, L is there but in small letter and we didn't use flags

s = re.search("L", "Hello", re.I)
print(s)		#Output: 1

s = re.search("^L", "Hello", re.I)
print(s)  #Output:None
```
---

### 搜尋和替換
- re 模組提供了一個 sub 函式來替換給定字串 string 中出現的所有符合 pattern 匹配模式的情況，用來替換的字串是 repl。你可以通過 count 關鍵字引數指定最大的替換次數，假如 count 沒有給定的話，那就沒有最大替換次數限制。
- sub 函式返回了一個新的字串。

```python
re.sub(pattern, repl, string, count = 0)
```



```python
#sub 函式舉例
#下面的例子中，sub 函式將整個字串用新的字串替換掉了

import re
s = "Playing 4 hours a day"
obj = re.sub(r'^.*$',"Working",s)
print(obj)
```
- 這裡，模式 r'^.*$ 中，^和 $ 意思是從開頭到結尾，.*意思是匹配字串中的任意字元，它們結合起來就是匹配從開頭到結尾的任意字元。 "Working"將來替換整個字串 s.

```python
#替換文字re.sub
import re
s = "Playing 4 hours a day"
#matchStr = re.sub(r'^.*$',"Working",s)
matchStr = re.sub(r'hours',"Working",s)
print(matchStr.__class__)
print(matchStr)


========================
<class 'str'>
Playing 4 Working a day
```



```python
#使用 sub 函式來刪除字串中的所有數字
#下面的例子中，使用 sub 函式來刪除給定字串中的數字，你需要用\d 來匹配數字。

import re
s = "768 Working 2343 789 five 234 656 hours 324 4646 a 345 day"
obj = re.sub(r'\d',"",s)
print(obj)
```
```python
Working   five   hours   a  day
```
```python
#類似的，你可以來刪除字串中的字母，用 \D 來匹配所有的字母。
```

```
76823437892346563244646345
```
---

### findall() 函式
- The findall 函式傳回與模式匹配的所有字串組成的列表。search 和 findall 函式之間的區別在於 findall 查詢所有匹配項，而 search 只查詢第一個匹配項。findall 函式查詢出非重疊的匹配並將其組成列表來返回。

```python
findall(pattern, string, flags)
```

--- 

 
```python
#查詢所有的非重疊的匹配


import re
str1 = "Working 6 hours a day. Studying 4 hours a day."
mobj = re.findall(r'[0-9]', str1)
print(mobj)

輸出結果:===============
['6', '4']
```
---

### finditer() 函式
- finditer 函式可用於在字串中查詢正規表示式模式並將匹配的字串以及字串的位置返回。

```python
finditer(pattern, string, flags)
```


- 遍歷所有的匹配
	- findall 和 finditer 之間唯一的區別是 finditer 返回索引以及匹配的字串。在下面的程式碼中，finditer 用於查詢匹配字串的位置，而後通過 for 迴圈來在遍歷所有的匹配（匹配字串）。


```pytnon
#遍歷所有的匹配

import re
str1 = "Working 6 hours a day. Studying 4 hours a day."
pat = r'[0-9]'
for mobj in re.finditer(pat, str1):
    print(mobj.__class__)
    s = mobj.start()
    e = mobj.end()
    g = mobj.group()
    print('{} found at location [{},{}]'.format(g, s, e))

輸出結果:===================
<class 're.Match'>
6 found at location [8,9]
<class 're.Match'>
4 found at location [32,33]
```
---

### split() 函式
- split 函式用於拆分字串

```python
split(patter, string, maxsplit=0, flags=0)
```

- 這裡 maxsplit 是最多的拆分次數，假如能夠拆分的次數大於 maxsplit 那麼剩餘的字串將作為列表中的最後一個元素。maxsplit 的預設值是 0，意思是可以無限拆分。

---
### 拆分一個字串
- 我們可以通過 split 來拆分字串，下面的例子中，字串根據給定的模式以及最大拆分的數量來拆分。

```python
import re
str1 = "Birds   fly  high in    the   sky for ever"
splitList = re.split(r'\s+',str1)
print(splitList)
print("-".join(splitList))

輸出結果:==================
['Birds', 'fly', 'high', 'in', 'the', 'sky', 'for', 'ever']
Birds-fly-high-in-the-sky-for-ever
```

- 本例中，模式 \s 用來匹配所有的空白字元，它等效於各種空白字元的集合，包括空格，製表符，回車等，具體如 [ \t\n\r\f\v]。所以你可以通過它將各個拆分開來。這裡的最大拆分次數是 5，所以結果列表中有 6 個元素，最後一個元素是最後一次拆分後剩下的所有的字串。

```python
import re
s = "768 Working 2343 789 five 234 656 hours 324 4646 a 345 day"
matchStr = re.sub(r'\d',"",s)
print(matchStr)
splitList = re.split(r'\s+',matchStr)
for word in splitList:
    print(word)
    


    
輸出結果======================================
 Working   five   hours   a  day

Working
five
hours
a
day
```



---

### Basic patterns of re 的基本模式
- 正規表示式可以指定與給定字串進行比較的模式。
- 以下是正規表示式的基本模式

| 模式 |	描述 |
|:-- | :-- |
| ^ |	在字串開頭匹配 |
|$	| 在字串的結尾處匹配|
|.|	匹配任意一個字元（不包括換行符）|
|[...]|	匹配括號內的單個字元|
| *	| 給定字串中出現 0 次或更多次 |
| +	| 給定字串中出現 1 次或多次前面的 |
| ?	| 給定字串中出現 0 次或 1 次 |
| {n} |	匹配給定字串中出現次數為 n |
| {n,} | 匹配給定字串中出現次數為 n 次或多次 |
|{n,m}	| 匹配給定字串中的出現次數為至少 n 個，最多 m 個 |
| \w	 | 此模式用於匹配單詞 |
| \W |	此模式用於匹配非單詞 |
| \s	 | 它將匹配空格。\ s 等於[\ t \ n \ r \ n] |
| \S |	它將匹配非空格 |
| \d	 | \ d 等於 [0-9]。它匹配字串中的數字 |
| \D |	匹配非數字 |
| \A	 | 匹配字串的開頭 |
| \Z |	匹配字串的結尾。如果有任何換行符，它將在換行符之前匹配 |
| \z |	匹配字串的結尾 |
| \G	 | \G 用於匹配最後一次匹配結束的點 |
| \b	 | 匹配在開頭或者結尾的空字元 |
| \B |	匹配不在開頭或者結尾的空字元 |


---

```python
#taiwanId.py
#r'^[A-Z]\d{9}$'
#驗證身份證字號


顯示:
請輸入身份證字號:A12345678
A12345678有誤

請輸入身份證字號:A123456789
A123456789正確
#===========================

import re
taiwanId = input("請輸入身份證字號:")
matchObject = re.match(r'^[A-Z]\d{9}$',taiwanId,re.I)
if matchObject:
    print(matchObject.group(), "正確")
else:
    print(taiwanId, "不正確")

```

---

```python
#email.py
# r'\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+'


顯示:
請輸入多筆email:內政部公開New eID換發系統建置及維護案，規定業bogusemail123@sillymail.com者須在明年6月10日前完成相關系統開發，包括New eID管理系統、戶役政資訊系統軟硬robert@gmail.com擴充、維護、人員訓練等。LINE GrayLab資安研究roberthsu2003@gmail.com室負責人公布他們在企業內部與產品發布的資安防護作法，同時也透露他們最新的諸多進展

bogusemail123@sillymail.com, ,roberthsu2003@gmail.com,,,robert@gmail.com

取出的email有:
bogusemail123@sillymail.com
robert@gmail.com
roberthsu2003@gmail.com


import re
emails = input('請輸入多筆email:')
getEmails = re.findall(r'\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+',emails)
print('取出的email有:')
for email in getEmails:
    print(email)
```