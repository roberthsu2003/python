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
		print(count)
		count += 1 
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
		stuff = input("String to capitalize [type q to quit]: ")
			if stuff == "q":
				break
		print(stuff.capitalize())

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
Integer, please [q to quit]: q 
>>>

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

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

>>> rows = range(1,4) 
>>> cols = range(1,3) 
>>> for row in rows:
		 for col in cols:
			print(row, col)

1 1 
1 2 
2 1 
2 2 
3 1 
3 2

=====================================================

>>> rows = range(1,4)
>>> cols = range(1,3)
>>> cells = [(row, col) for row in rows for col in cols] 
>>> for cell in cells:
		print(cell)

(1, 1)
(1, 2)
(2, 1)
(2, 2)
(3, 1)
(3, 2)

>>> for row, col in cells:
		print(row, col)
		

```

### Dictionary Comprehensions

```python
{ key_expression : value_expression for expression in iterable }

>>> word = 'letters'
>>> letter_counts = {letter: word.count(letter) for letter in word}
>>> letter_counts
{'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

=====================================================
>>> word = 'letters'
>>> letter_counts = {letter: word.count(letter) for letter in set(word)} 
>>> letter_counts
{'t': 2, 'l': 1, 'e': 2, 'r': 1, 's': 1}
```
### Set Comprehensions
```python
>>> a_set = {number for number in range(1,6) if number % 3 == 1} 
>>> a_set
{1, 4}

```
### Generator Comprehensions
```python
>>> number_thing = (number for number in range(1, 6))
>>> type(number_thing)
<class 'generator'>

>>> for number in number_thing: 
		print(number)

1
2 
3 
4 
5

===========================================
>>> number_list = list(number_thing) 
>>> number_list
[1,2,3,4,5]

>>> try_again = list(number_thing) 
>>> try_again
[]


```
## Functions
```python
>>> def do_nothing(): 
		pass

>>> do_nothing() 
>>>

========================================

>>> def make_a_sound():
		print('quack')
		
>>> make_a_sound()
quack

========================================

>>> def agree(): 
		return True 

>>> if agree():
		print('Splendid!')
	else:
		print('That was unexpected.')

Splendid!

>>> def echo(anything):
		return anything + ' ' + anything 
...
>>>

>>> echo('Rumplestiltskin')
'Rumplestiltskin Rumplestiltskin'

>>> def commentary(color):
		if color == 'red':
			return "It's a tomato."
		elif color == "green":
			return "It's a green pepper."
		elif color == 'bee purple':
			return "I don't know what it is, but only bees can see it."
		else:
			return "I've never heard of the color " + color + "."

>>> comment = commentary('blue')
>>> print(comment)

I've never heard of the color blue.


```

### Positional Arguments

```python
>>> def menu(wine, entree, dessert):
		return {'wine': wine, 'entree': entree, 'dessert': dessert} 
...
>>> menu('chardonnay', 'chicken', 'cake')
{'dessert': 'cake', 'wine': 'chardonnay', 'entree': 'chicken'}

>> menu('beef', 'bagel', 'bordeaux')
{'dessert': 'bordeaux', 'wine': 'beef', 'entree': 'bagel'}

```

### Keyword Arguments

```python
>>> menu(entree='beef', dessert='bagel', wine='bordeaux')
{'dessert': 'bagel', 'wine': 'bordeaux', 'entree': 'beef'}

>>> menu('frontenac', dessert='flan', entree='fish')
{'entree': 'fish', 'dessert': 'flan', 'wine': 'frontenac'}

```
### Specify Default Parameter Values

```python
>>> def menu(wine, entree, dessert='pudding'):
return {'wine': wine, 'entree': entree, 'dessert': dessert}

>>> menu('chardonnay', 'chicken')
{'dessert': 'pudding', 'wine': 'chardonnay', 'entree': 'chicken'}

>>> menu('dunkelfelder', 'duck', 'doughnut')
{'dessert': 'doughnut', 'wine': 'dunkelfelder', 'entree': 'duck'}

========================================

>>> def buggy(arg, result=[]):
		result.append(arg)
		print(result) 
		...
>>> buggy('a')
['a']
>>> buggy('b') # expect ['b'] ['a', 'b']

========================================

>>> def works(arg):
		result = []
		result.append(arg)
		return result
...
>>> works('a')
['a']
>>> works('b')
['b']

=========================================

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

### Gather Positional Arguments with *

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

### Gather Keyword Arguments with **
```python
>>> def print_kwargs(**kwargs):
		print('Keyword arguments:', kwargs) 
...

>>> print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

Keyword arguments: {'dessert': 'macaroon', 'wine': 'merlot', 'entree': 'mutton'}

```

### Docstrings

```python
>>> def echo(anything):
		'echo returns its input argument'
		return anything

================================================
		
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
### Functions Are First-Class Citizens
```python
>>> def answer(): 
		print(42)

>>> answer()
42

==========================================

>>> def run_something(func): 
	func()

>>> run_something(answer) 
42
```


```python
def add_args(arg1, arg2): 
	print(arg1 + arg2)
	

>>> type(add_args)
<class 'function'>


def run_something_with_args(func, arg1, arg2):
	func(arg1, arg2)
	

>>> run_something_with_args(add_args, 5, 9) 
14

```

```python
def sum_args(*args): 
	return sum(args)
	

def run_with_positional_args(func, *args):
	return func(*args)


>>> run_with_positional_args(sum_args, 1, 2, 3, 4)
10	
```

### Inner Functions

```python
def outer(a, b):
	def inner(c, d): 
		returnc+d
	return inner(a, b)


>>> outer(4, 7)
11


def knights(saying):
	def inner(quote):	
		return "We are the knights who say: '%s'" % quote
	return inner(saying)
	
	
>>> knights('Ni!')
    "We are the knights who say: 'Ni!'"
```

### Closures
```python
def knights2(saying):
	def inner2():
		return "We are the knights who say: '%s'" % saying
	return inner2

>>> a = knights2('Duck')
>>> b = knights2('Hasenpfeffer')

>>> type(a) <class 'function'> 
>>> type(b) <class 'function'>

>>> a
<function knights2.<locals>.inner2 at 0x10193e158> 
>>> b
<function knights2.<locals>.inner2 at 0x10193e1e0>

>>> a()
"We are the knights who say: 'Duck'"
>>> b()
"We are the knights who say: 'Hasenpfeffer'"
```

### Anonymous Functions: the lambda() Function
```python
def edit_story(words, func):
	for word in words:
		print(func(word))


>>> stairs = ['thud', 'meow', 'thud', 'hiss']


def enliven(word): # give that prose more punch 
	return word.capitalize() + '!'
	
>>> edit_story(stairs, enliven) 
Thud!
Meow!
Thud!
Hiss!


>>> edit_story(stairs, lambda word: word.capitalize() + '!') 
Thud!
Meow!
Thud!
Hiss!
```

### Generators

```python
>>> sum(range(1, 101))
5050


def my_range(first=0, last=10, step=1):
	number = first
	while number < last:
		yield number
		number += step

>>> my_range
<function my_range at 0x10193e268>

>>> ranger = my_range(1, 5)
>>> ranger
<generator object my_range at 0x101a0a168>

for x in ranger: 
	print(x)

1
2 
3 
4
```

### Decorators
```python
def document_it(func):
	def new_function(*args, **kwargs):
		print('Running function:', func.__name__) 
		print('Positional arguments:', args) 
		print('Keyword arguments:', kwargs) 
		result = func(*args, **kwargs) 
		print('Result:', result)
		return result
	return new_function



def add_ints(a, b): 
returna+b

>>> add_ints(3, 5)
8

>>> cooler_add_ints = document_it(add_ints) # manual decorator assignment
>>> cooler_add_ints(3, 5) 
Running function: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
8


@document_it
def add_ints(a, b):
	returna+b

>>> add_ints(3, 5)
Start function add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
8



def square_it(func):
	def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
		return result * result
	return new_function


@document_it
@square_it
def add_ints(a, b):
	return a+b

>>> add_ints(3, 5)
Running function: new_function
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 64
64


@square_it
@document_it
def add_ints(a, b):
return a+b 

>>> add_ints(3, 5) 
Running function: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
64

```

### Namespaces and Scope

```python
>>> animal = 'fruitbat'
def print_global():
	print('inside print_global:', animal)
	
	
>>> print('at the top level:', animal)
at the top level: fruitbat
>>> print_global()
inside print_global: fruitbat



def change_and_print_global():
	print('inside change_and_print_global:', animal)
	animal = 'wombat'
	print('after the change:', animal)


>>> change_and_print_global()
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	File "<stdin>", line 2, in change_and_report_it
UnboundLocalError: local variable 'animal' referenced before assignment



def change_local():
	animal = 'wombat'
	print('inside change_local:', animal, id(animal))


>>> change_local()
inside change_local: wombat 4330406160 
>>> animal
'fruitbat'

>>> id(animal)
4330390832


>>> animal = 'fruitbat'


def change_and_print_global():
	global animal
	animal = 'wombat'
	print('inside change_and_print_global',animal)
	
>>> animal
'fruitbat'
>>> change_and_print_global()
inside change_and_print_global: wombat 
>>> animal
'wombat'


>>> animal = 'fruitbat'
	def change_and_print_global():
	animal = 'wombat'
	print('locals:',locals())
	
>>> animal
'fruitbat'
>>> change_local()
locals: {'animal': 'wombat'}

>>> print('globals',globals()) # reformatted a little for presentation
globals: {'animal': 'fruitbat',
'__doc__': None,
'change_local': <function change_it at 0x1006c0170>,
'__package__': None,
'__name__': '__main__',
'__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__builtins__': <module 'builtins'>}
>>> animal
'fruitbat'

```

### Uses of _ and __ in Names

```python

def amazing():
	'''This is the amazing function.
	Want to see it again?'''
	print('This function is named:', amazing.__name__)
	print('And its docstring is:', amazing.__doc__)
	
>>> amazing()
This function is named: amazing
And its docstring is: This is the amazing function.
Want to see it again?
```

### Handle Errors with try and except

```python
>>> short_list = [1, 2, 3]
>>> position = 5
>>> short_list[position] 
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: list index out of range



short_list = [1, 2, 3] 
position = 5
try:
	short_list[position] 
except:
	print('Need a position between 0 and', len(short_list)-1, ' but got',position)
	
	
Need a position between 0 and 2 but got 5



short_list = [1, 2, 3] 
	while True:
		value = input('Position [q to quit]? ')
		if value == 'q':
			break 
		try:
			position = int(value)
			print(short_list[position]) 
		except IndexError as err:
			print('Bad index:', position) 
		except Exception as other:
			print('Something else broke:', other)

Position [q to quit]? 1
2
Position [q to quit]? 0
1
Position [q to quit]? 2
3
Position [q to quit]? 3
Bad index: 3
Position [q to quit]? 2
3
Position [q to quit]? two
Something else broke: invalid literal for int() with base 10: 'two'
Position [q to quit]? q
```

### Make Your Own Exceptions

```python
class UppercaseException(Exception): 
	pass

>>> words = ['eeenie', 'meenie', 'miny', 'MO'] 
for word in words:
	if word.isupper():
		raise UppercaseException(word)
	
Traceback (most recent call last):
File "<stdin>", line 3, in <module>
__main__.UppercaseException: MO



try:
	raise OopsException('panic')
except OopsException as exc:
	print(exc)


```

