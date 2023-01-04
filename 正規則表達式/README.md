# Python 正規表示式模組 (re) 簡介
- 正規表示式以及 Python re 模組中定義的正規表示式操作。

- re 是 Python 的標準庫，它支援正規表示式的匹配操作。

- Python 中的正規表示式是一組字元或序列，用於使用正式語法將字串與另一個模式匹配。你可以將正規表示式視為嵌入在 python 中的小型程式語言。

- 你可以使用正規表示式來定義一些規則，然後使用這些規則從你希望與模式匹配的給定字串中建立可能的字串。Python 中的正規表示式被解釋為一組指令。

- [regex pal 正規表示式模擬測試網站](https://www.regexpal.com)

- [python 正規則表達式測試網站](https://pythex.org)

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
import re
emailRegex = re.compile(r'''
        [a-zA-Z0-9._%+-]+ #username
        @                 #symbol
        [a-zA-Z0-9.-]+    #domain name
        (\.[a-zA-Z]{2,4}){:3}

''',re.VERBOSE)
```







### match() 函式
- 你可以使用 match() 函式將 RE 模式與給定字串來匹配。match() 函式也包含了標誌，標誌定義正規表示式的行為，它可以有不同的值
 
```python
re.match(pattern, string, flags=0)
regex.match(pattern,flags)

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
#使用match()

import re

strText = "Hello Python Programming"
helloRegex = re.compile(r"hello",re.I)
matchObjec = helloRegex.match(strText)
if matchObjec is None:
    print("文字最前面沒有搜尋到")
else:
    print("文字最前面搜尋到%s" % matchObjec.group())

#在此示例中，使用字首 r 來表示字串是原始字串。在原始字串中，在使用轉義序列時不需要寫雙斜槓，例如，如果你想要一個反斜槓，那麼你只需要一個\，而不用像普通字串那樣的雙反斜槓\\。
```

```python
import re

line = "Cats are smarter than dogs"
catsRegex = re.compile(r'(.*) are (.*?) .*',re.M|re.I)

matchObj = catsRegex.match(line)

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
regex.search(string)
```

```pytnon

import re
str = "Hello Python Programming"
programRegex = re.compile(r"programming",re.I)
searchObject = programRegex.search(str)
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
pRegex=re.compile(r"^programming",re.I)
sobj = pRegex.search(str)
print(sobj) #no match is found

hRegex = re.compile(r"^hello",re.I)
sobj = hRegex.search(str)
print(sobj.group()) #matching: Hello
結果:=====================
None
Hello
```

這裡，^ 的意思是隻在字串的開頭進行搜尋，假如開頭不匹配的話，就返回 None，而不管字串後續中有沒有再匹配到。

---

### 在字串結尾搜尋
- 你也可以在給定字串的末尾搜尋，通過在模式後面加 $ 來限定。

```python
#在字串結尾搜尋
import re
str = "Hello Python Programming"
pRegex=re.compile(r"programming$",re.I)
sobj = pRegex.search(str)
print(sobj.group()) #matching: Programming

hRegex = re.compile(r"^hello$",re.I)
sobj = hRegex.search(str)
print(sobj) #no match found

結果:=================
Programming
None
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
結果:=================
1
2
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
lRegx= re.compile(r"L")
s = lRegx.search("Hello")
print(s)		#Output: None, L is there but in small letter and we didn't use flags

lRegx= re.compile(r"L",re.I)
s = lRegx.search("Hello")
print(s)		#Output: 1

lRegx= re.compile(r"^L",re.I)
s = lRegx.search("Hello")
print(s)  #Output:None

結果:=========================
None
<re.Match object; span=(2, 3), match='l'>
None
```
---

### 搜尋和替換
- re 模組提供了一個 sub 函式來替換給定字串 string 中出現的所有符合 pattern 匹配模式的情況，用來替換的字串是 repl。你可以通過 count 關鍵字引數指定最大的替換次數，假如 count 沒有給定的話，那就沒有最大替換次數限制。
- sub 函式返回了一個新的字串。

```python
regex.sub(repl, string, count = 0)
```



```python
#sub 函式舉例
#下面的例子中，sub 函式將整個字串用新的字串替換掉了

s = "Playing 4 hours a day"
regex = re.compile(r'^.*$')
obj = regex.sub("Working",s)
print(obj)

結果:=============
Working
```
- 這裡，模式 r'^.*$ 中，^和 $ 意思是從開頭到結尾，.*意思是匹配字串中的任意字元，它們結合起來就是匹配從開頭到結尾的任意字元。 "Working"將來替換整個字串 s.

```python
#替換文字regex.sub
import re
s = "Playing 4 hours a day"
regex = re.compile(r'hours')
matchStr = regex.sub("Working",s)
print(matchStr.__class__)
print(matchStr)


結果:========================
<class 'str'>
Playing 4 Working a day
```



```python
#使用 sub 函式來刪除字串中的所有數字
#下面的例子中，使用 sub 函式來刪除給定字串中的數字，你需要用\d 來匹配數字。

import re
import re
s = "768 Working 2343 789 five 234 656 hours 324 4646 a 345 day"
regex =  re.compile(r'\d')
obj = regex.sub("",s)
print(obj)
結果:========================
Working   five   hours   a  day
```

```python
#類似的，你可以來刪除字串中的字母，用 \D 來匹配所有的字母。
結果:=======================
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