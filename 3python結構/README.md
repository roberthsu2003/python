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


>>> 1+2+
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

===============================

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

=============================

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

================================


>>> x=7
>>> x==5 
False 
>>> x==7
True 
>>> 5<x
True
>>> x<10 
True

>>> 5<x and x<10 
True

>>> (5<x) and (x<10)
True

>>> 5<x or x<10 
True 

>>> 5<x and x>10
False 

>>> 5 < x and not x > 10 
True

>>>5 < x < 10 
True

>>> some_list = []
>>> if some_list:
			print("There are something in here")
		else:
			print("Hey! It's empty")

Hey, it's empty!

```

### Repeat with while

```python
>>> count = 1
>>> while count <= 5:
... print(count)
... count += 1 
...
1
2
3
4
5
>>>
```

### Cancel with break

```python
>>> while True:
... stuff = input("String to capitalize [type q to quit]: ")
... if stuff == "q":
... break
... print(stuff.capitalize())
...
String to capitalize [type q to quit]: test
Test
String to capitalize [type q to quit]: hey, it works Hey, it works
String to capitalize [type q to quit]: q
>>>
```

### Skip Ahead with continue
```python
>>> while True:
	value = input("Integer, please [q to quit]: ") 
	if value == 'q': # quit
	break
	number = int(value)
	if number % 2 == 0: # an even number
	continue
	print(number, "squared is", number*number)
Integer, please [q to quit]: 1 1 squared is 1
Integer, please [q to quit]: 2 Integer, please [q to quit]: 3 3 squared is 9
Integer, please [q to quit]: 4 Integer, please [q to quit]: 5 5 squared is 25
Integer, please [q to quit]: q >>>

```

### Check break Use with else

```python
>>> numbers = [1, 3, 5]
>>> position = 0
>>> while position < len(numbers):
			number = numbers[position] 
			if number%2==0:
				print('Found even number', number)
				break
			position += 1
		else: # break not called
			print('No even number')
			
No even number found
```

### Iterate with for
```python
>>> rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter'] 
>>> current = 0
>>> while current < len(rabbits):
			print(rabbits[current])
			current += 1 
...
Flopsy
Mopsy
Cottontail
Peter

#it's better
>>> for rabbit in rabbits: 
			print(rabbit)
			
Flopsy
Mopsy
Cottontail
Peter

```


### 
```python
>>> word = 'cat'
>>> for letter in word:
			print(letter) 
			
c
a
t


====================================

>>> accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
>>> for card in accusation: # or, for card in accusation.keys():
			print(card)

room
weapon
person

=====================================
>>> for value in accusation.values(): 
			print(value)

ballroom
lead pipe 
Col. Mustard

======================================
>>> for item in accusation.items(): 
			print(item)

('room', 'ballroom')
('weapon', 'lead pipe') 
('person', 'Col. Mustard')

=======================================
>>> for card, contents in accusation.items():
			print('Card', card, 'has the contents', contents) 

			
Card weapon has the contents lead pipe
Card person has the contents Col. Mustard
Card room has the contents ballroom
```

### Check break Use with else

```python
>>> cheeses = []
>>> for cheese in cheeses:
			print('This shop has some lovely', cheese)
			break
		else: # no break means no cheese
			print('This is not much of a cheese shop, is it?') 
			
This is not much of a cheese shop, is it?
```
### Iterate Multiple Sequences with zip()

```python
>>> days = ['Monday', 'Tuesday', 'Wednesday']
>>> fruits = ['banana', 'orange', 'peach']
>>> drinks = ['coffee', 'tea', 'beer']
>>> desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
>>> for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts): 
			print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)
			
Monday : drink coffee - eat banana - enjoy tiramisu 
Tuesday : drink tea - eat orange - enjoy ice cream 
Wednesday : drink beer - eat peach - enjoy pie

=============================================

>>> english = 'Monday', 'Tuesday', 'Wednesday'
>>> french = 'Lundi', 'Mardi', 'Mercredi'
>>> list( zip(english, french) )
[('Monday', 'Lundi'), ('Tuesday', 'Mardi'), ('Wednesday', 'Mercredi')]

>>> dict( zip(english, french) )
{'Monday': 'Lundi', 'Tuesday': 'Mardi', 'Wednesday': 'Mercredi'}


```
### Generate Number Sequences with range()

```python
>>> for x in range(0,3): 
			print(x)

0
1
2
>>> list( range(0, 3) )
[0, 1, 2]

=================================================

>>> for x in range(2, -1, -1):
			print(x)

2
1
0
>>> list( range(2, -1, -1) ) 
[2, 1, 0]

====================================================

>>> list( range(0, 11, 2) )
[0,2,4,6,8,10]
```
### Comprehensions
```python
>>> number_list = []
>>> number_list.append(1)
 >>> number_list.append(2) 
 >>> number_list.append(3) 
 >>> number_list.append(4) 
 >>> number_list.append(5) 
 >>> number_list 
 [1,2,3,4,5]
 
===========================================
>>> number_list = []
>>> for number in range(1, 6):
			number_list.append(number) 
>>> number_list
[1,2,3,4,5]

============================================

>>> number_list = list(range(1, 6)) 
>>> number_list
[1,2,3,4,5]

============================================
[ expression for item in iterable ]

>>> number_list = [number for number in range(1,6)] 
>>> number_list
[1,2,3,4,5]

============================================

>>> number_list = [number-1 for number in range(1,6)] 
>>> number_list
[0,1,2,3,4]

===============================================
[ expression for item in iterable if condition ]

>>> a_list = [number for number in range(1,6) if number % 2 == 1] 
>>> a_list
[1, 3, 5]

==================================================
>>> a_list = []
>>> for number in range(1,6):
			if number%2 == 1: 
				a_list.append(number)
>>> a_list
[1, 3, 5]


```






