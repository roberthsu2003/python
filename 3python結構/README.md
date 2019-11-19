# python 程式結構
## 註解
```python
>>> # 60 sec/min * 60 min/hr * 24 hr/day 
>>> seconds_per_day = 86400

>>> seconds_per_day = 86400 # 60 sec/min * 60 min/hr * 24 hr/day


#python不支援多行註解
>>> # I can say anything here, even if Python doesn't like it,
... # because I'm protected by the awesome
... # octothorpe. ...
>>>

>>> print("No comment: quotes make the # harmless.")
 No comment: quotes make the # harmless.

```

## Continue Lines with \

```python
>>> alphabet = ''
>>> alphabet += 'abcdefg'
>>> alphabet += 'hijklmnop'
>>> alphabet += 'qrstuv'
>>> alphabet += 'wxyz'

#連結字串
>>> alphabet = 'abcdefg' + \
... 'hijklmnop' + \
... 'qrstuv' + \
... 'wxyz'


>>>1+2+
File "<stdin>", line 1
1+2+ ^
SyntaxError: invalid syntax 
>>>1+2+\
... 3
6
```
## 判斷流程控制 if, elif, and else
```python
>>> disaster = True 
>>> if disaster:
		print("Woe!") 
	else:
		print("Whee!")
Woe!

###

furry = True 
small = True 
if furry:
	if small:
		print("It's a cat.")
	else:
		print("It's a bear!")
else:
	if small:
		print("It's a skink!")
	else:
		print("It's a human. Or a hairless bear.")

It's a cat.

###
color = "puce"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)


I've never heard of the color puce

###
>>>x=7
>>>x==5 
False 
>>>x==7
True 
>>>5<x
True
>>>x<10 
>>>True

>>>5<xandx<10 
True

>>>(5<x) and (x<10)
True

>>>5<x or x<10 
True 
>>>5<x and x>10
False 
>>>5 < x and not x > 10 
True


>>>5 < x < 10 
True

```




