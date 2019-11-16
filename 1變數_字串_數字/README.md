# python
## Python內建資料型別  
• booleans (True or False)  
• integers (42 and 100000000)  
• floats (3.14159）  
• string  

```python
#下面2行，將7給變數a, 並且輸出變數a的內容
a=7
print(a)

#將a的參考給b,並且輸出變數b的內容
b=a
print(b)

#使用type function輸出目前的資料型別
type(a) 
<class 'int'>

type(b)
<class 'int'>

type(58)
<class 'int'>

type(99.9)
<class 'float'>

type('abc')
<class 'str'>

```

## 合法命名  

```
• a  
• a1  
• a_b_c___95  
• _abc  
• _1a  
```
## 不合法命名  

```
• 1 
• 1a  
• 1_  
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

## 優先運算子

```python
>>>2+3*4 
   14
   
>>>(2+3)*4
   20
   
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

```kotlin
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
 


>>> '''Boom!'''
    'Boom'
>>> """Eek!"""
    'Eek!'
    
>>> poem = '''There was a Young Lady of Norway, ... Who casually sat in a doorway;
... When the door squeezed her flat,
... She exclaimed, "What of that?"
... This courageous Young Lady of Norway.'''



>>> poem2 = '''I do not like thee, Doctor Fell.
... The reason why, I cannot tell.
... But this I know, and know full well:
... I do not like thee, Doctor Fell.
... '''
>>> print(poem2)
I do not like thee, Doctor Fell.
	The reason why, I cannot tell.
	But this I know, and know full well: 
	I do not like thee, Doctor Fell.
>>>


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




>>> bottles = 99
>>> base = ''
>>> base += 'current inventory: '
>>> base += str(bottles)
>>> base
    'current inventory: 99'



#使用str()轉換為字串型別
>>> str(98.6) 
    '98.6'
>>> str(1.0e4) 
    '10000.0'
>>> str(True)
    'True'




#脫溢字元 \
>>> palindrome = 'A man,\nA plan,\nA canal:\nPanama.' 
>>> print(palindrome)
A man,
A plan,
A canal: Panama.



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



#使用+運算子
>>> 'Release the kraken! ' + 'At once!'
    'Release the kraken! At once!'




>>> a = 'Duck.' 
    b=a
>>> c = 'Grey Duck!' 
>>>a+b+c 
   'Duck.Duck.Grey Duck!'



>>> print(a, b, c) 
    Duck. Duck. Grey Duck!
    
    



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
File "<stdin>", line 1, in <module> IndexError: string index out of range




>>> name = 'Henny'
>>> name[0] = 'P'
Traceback (most recent call last): File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment


>>> name = 'Henny'
>>> name.replace('H', 'P') 
   'Penny'
>>> 'P' + name[1:] 
    'Penny'



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


>>> letters[-1::-1] 
    'zyxwvutsrqponmlkjihgfedcba'


>>> letters[::-1] 
    'zyxwvutsrqponmlkjihgfedcba'



#len()
>>> len(letters)
    26
>>> empty = ""
>>> len(empty)
    0
    
    
#split()
>>> todos = 'get gloves,get mask,give cat vitamins,call ambulance' 
>>> todos.split(',')
['get gloves', 'get mask', 'give cat vitamins', 'call ambulance']


#join()
>>> crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster'] 
>>> crypto_string = ', '.join(crypto_list)
>>> print('Found and signing book deals:', crypto_string) Found and signing book deals: Yeti, Bigfoot, Loch Ness Monster




>>> poem = '''All that doth flow we cannot liquid name Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out But 'tis the wet that makes it die, no doubt.'''


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
>>> 'a duck goes into a bar... '

>>> setup.rjust(30)
' a duck goes into a bar...'

#replace()
>>> setup.replace('duck', 'marmoset') 
   'a marmoset goes into a bar...'
   








```


