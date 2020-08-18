# 字串的處理

```python
#len()
letters = 'abcdefghijklmnopqrstuvwxyz'
print(len(letters))

empty = ""
print(len(empty))

結果:==================================
26
0
```

---
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

###  索引編號與取值
- [n : m]
	- 在一個範圍內找資料
	- n 與 m 均是一個整數
	- n 代表起始位置，第一個為 0。
	- m 是結束位置，不包含這個位置。




```python
#索引編號與取值:請留意輸出結果
#string3.py

myString1="Hello World"
print(myString1[0]) 
print(myString1[2]) 
print(myString1[-1]) 
print(myString1[-2]) 
print(myString1[2:]) 
print(myString1[:3]) 
print(myString1[1:4])

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


str1 = "This is Python, That is Java; This is SQLite, That is MySQL"
print("原本的字串:", str1)
print()
print("is 替換為 - :" + str1.replace("is", "-"))
print()

str1 = "This is Python, That is Java; This is SQLite, That is MySQL"
print("原本的字串:", str)
print()
print("加上參數值2:" + str1.replace("is", "-", 2))
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

str1 = "this is Python Tutorial, there"
search1 = "Python" 
print(str1.find(search1)) #使用slice範例

search2= "not" 
print(str1.find(search2)) #使用判斷範例

search3="t" 
print(str1.find(search3)) 
print(str1.find(search3,4)) 
print(str1.find(search3,11,20))
```

---

####  字串連接與切割
- 字串.join( ) : 於字串或著字元之間加入指定的文字
	- 連接符號字串.join(串列)
- 字串.split( ) : 將字串進行切割
	- 字串.split(分割符號)
	- 字串.split(分割符號,分割次數)

```python
#string6.py

str1 = "-"
str2 = ("a", "b", "c") 
print(str1.join(str2))

str2 = ("abc", “xyz", “123") 
print(str1.join(str2))
 
str3=":".join("Python") 
print(str3)

str4 = "python-java-c++-ruby" 
print(str4.split('-')) 
print(str4.split('-',1))
```



```python
#split()
>>> todos = 'get gloves,get mask,give cat vitamins,call ambulance' 
>>> todos.split(',')
['get gloves', 'get mask', 'give cat vitamins', 'call ambulance']

```



```python
#join()
>>> crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster'] 
>>> crypto_string = ', '.join(crypto_list)
>>> print('Found and signing book deals:', crypto_string)

Found and signing book deals: Yeti, Bigfoot, Loch Ness Monster

```

---

```python
#字串常用的一些操控

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

### Homewrok:字串文字接龍
```python
#wordLink.pyworwor

失敗就會退出遊戲
請輸入一個字串:Python
上一個字串是Python
請輸入-n-開始的字串:new
上一個字串是Python-new
請輸入-w-開始的字串:well
上一個字串是Python-new-well
請輸入-l-開始的字串: long time
上一個次串是Python-new-well-long time
請輸入-e-開始的字串
```
[解題](./wordLink.py)


---

## Python 正規表示式模組 (re) 簡介
- 正規表示式以及 Python re 模組中定義的正規表示式操作。

- re 是 Python 的標準庫，它支援正規表示式的匹配操作。

- Python 中的正規表示式是一組字元或序列，用於使用正式語法將字串與另一個模式匹配。你可以將正規表示式視為嵌入在 python 中的小型程式語言。

- 你可以使用正規表示式來定義一些規則，然後使用這些規則從你希望與模式匹配的給定字串中建立可能的字串。Python 中的正規表示式被解釋為一組指令。

---

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
```


```python
#使用 match 函式

import re
strTest = "Hello Python Programming"
mobj = re.match(r"hello", strTest, re.I)
print(mobj.group())


#在此示例中，使用字首 r 來表示字串是原始字串。在原始字串中，在使用轉義序列時不需要寫雙斜槓，例如，如果你想要一個反斜槓，那麼你只需要一個\，而不用像普通字串那樣的雙反斜槓\\。
```

---

### search() 函式
你可以使用 search() 函式搜尋給定字串中的正規表示式匹配模式。search 有三個輸入引數，匹配模式，給定字串以及可選的匹配行為選項 flags

```python
re.search(pattern, string, flags)
```

```pytnon
import re
str = "Hello Python Programming"
sobj = re.search(r"programming", str, re.I)
print(sobj.group())
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
print(s)
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
```
```python
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
str1 = "Birds fly high in the sky for ever"
mobj = re.split('\s+', str1, 5)
print(mobj)
```

```python
['Birds', 'fly', 'high', 'in', 'the', 'sky for ever']
```

- 本例中，模式 \s 用來匹配所有的空白字元，它等效於各種空白字元的集合，包括空格，製表符，回車等，具體如 [ \t\n\r\f\v]。所以你可以通過它將各個拆分開來。這裡的最大拆分次數是 5，所以結果列表中有 6 個元素，最後一個元素是最後一次拆分後剩下的所有的字串。

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
taiwanId = input('請輸入身份證字號:')
mobj = re.match(r'^[A-Z]\d{9}$',taiwanId,re.I)
if(mobj):
    print(taiwanId,"正確")
else:
    print(taiwanId, "有誤")

```

---
```python
#email.py
# r'\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+'


顯示:
請輸入多筆email:bogusemail123@sillymail.com, robert@gmail.com ,,,roberthsu2003@gmail.com
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