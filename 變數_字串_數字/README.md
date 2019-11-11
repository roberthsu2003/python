# python
### Python內建資料型別  
• booleans (True or False)  
• integers (42 and 100000000)  
• floats (3.14159）  
• string  

```python
//下面2行，將7給變數a, 並且輸出變數a的內容
a=7
print(a)

//將a的參考給b,並且輸出變數b的內容
b=a
print(b)

//使用type function輸出目前的資料型別
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

//數字前不可以加0
>>> 05
      File "<stdin>", line 1
05
^
SyntaxError: invalid token //python的語法錯誤

```


