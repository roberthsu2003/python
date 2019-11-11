# python
### Python內建資料型別  
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

### 合法命名  

```
• a  
• a1  
• a_b_c___95  
• _abc  
• _1a  
```
### 不合法命名  

```
• 1 
• 1a  
• 1_  
```
### python數學運算子

運算子 | 描述  | 範例
-----| ------- | ----
| + | 加法 | 5+8=13
| - | 減法 | 90-10=80  
| ** | 乘法 | 4*7=28
| / | 浮點數除法 | 7 / 2=3.5
| // | 整數除法 | 7 // 2 = 3
| % | 餘數  | 7 % 3 = 1
| ** | 次方 |  3 ** 4 = 81

### python的整數

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
```

### 2,8,16進位
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



