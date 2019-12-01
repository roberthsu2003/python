# Objects and Classes
## Define a Class with class
- variables, called attributes
- functions, called methods

```python
class Person():
	pass

>>> someone = Person()

class Person():
	def __init__(self): 
		pass


class Person():
	def __init__(self, name):
		self.name = name

>>> hunter = Person('Elmer Fudd')
>>> print('The mighty hunter: ', hunter.name)
The mighty hunter: Elmer Fudd
```

## Inheritance
```python
class Car():
	pass

class Yugo(Car):
	pass

>>> give_me_a_car = Car() 
>>> give_me_a_yugo = Yugo()
```

```python
class Car():
	def exclaim(self):
		print("I'm a Car!")
		
class Yugo(Car):
	pass

>>> give_me_a_car = Car() 
>>> give_me_a_yugo = Yugo() 
>>> give_me_a_car.exclaim()
I'm a Car!
>>> give_me_a_yugo.exclaim()
I'm a Car!

```

## Override a Method

```python
class Car():
	def exclaim(self):
		print("I'm a Car!")

class Yugo(Car):
	def exclaim(self):
		print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

>>> give_me_a_car = Car() 
>>> give_me_a_yugo = Yugo()

>>> give_me_a_car.exclaim()
I'm a Car!
>>> give_me_a_yugo.exclaim()
I'm a Yugo! Much like a Car, but more Yugo-ish.



class Person():
	def __init__(self, name):
	self.name = name

class MDPerson(Person):
	def __init__(self, name):
	self.name = "Doctor " + name

class JDPerson(Person):
	def __init__(self, name):
	self.name = name + ", Esquire"
	
>>> person = Person('Fudd') 
>>> doctor = MDPerson('Fudd') 
>>> lawyer = JDPerson('Fudd') 
>>> print(person.name)
Fudd
>>> print(doctor.name) 
Doctor Fudd
>>> print(lawyer.name) 
Fudd, Esquire

```

## Add a Method

```python
class Car():
	def exclaim(self):
	print("I'm a Car!")
	

class Yugo(Car):
	def exclaim(self):
		print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
	
	def need_a_push(self):
		print("A little help here?")


>>> give_me_a_car = Car()
>>> give_me_a_yugo = Yugo()

>>> give_me_a_yugo.need_a_push()
A little help here?

>>> give_me_a_car.need_a_push() 
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'Car' object has no attribute 'need_a_push'
```

## Get Help from Your Parent with super

```python
class Person():
	def __init__(self, name):
		self.name = name


class EmailPerson(Person):
	def __init__(self, name, email): 
		super().__init__(name) 
		self.email = email


>>> bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
>>> bob.name
'Bob Frapples' 
>>> bob.email 
'bob@frapples.com'

class EmailPerson(Person):
	def __init__(self, name, email):
		self.name = name
		self.email = email

```

## In self Defense

```python

>>> car = Car() 
>>> car.exclaim() 
I'm a Car!

>>> Car.exclaim(car)
I'm a Car!

```

## Get and Set Attribute Values with Properties

```python
class Duck():
	def __init__(self, input_name): 
		self.hidden_name = input_name

	def get_name(self): 
		print('inside the getter') 
		return self.hidden_name
		
	def set_name(self, input_name): 
		print('inside the setter') 
		self.hidden_name = input_name

	name = property(get_name, set_name)
	
>>> fowl = Duck('Howard') 
>>> fowl.name
inside the getter 'Howard'

>>> fowl.get_name() 
inside the getter 'Howard'

>>> fowl.name = 'Daffy' 
inside the setter
>>> fowl.name
inside the getter 'Daffy'

>>> fowl.set_name('Daffy') 
inside the setter
>>> fowl.name
inside the getter
'Daffy'






class Duck():
def __init__(self, input_name):
	self.hidden_name = input_name
	@property
	def name(self):
		print('inside the getter') 
		return self.hidden_name
	
	@name.setter
	def name(self, input_name): 
		print('inside the setter') 
		self.hidden_name = input_name


>>> fowl = Duck('Howard') 
>>> fowl.name
inside the getter 'Howard'
>>> fowl.name = 'Donald' 
inside the setter
>>> fowl.name
inside the getter 'Donald'


class Circle():
	def __init__(self, radius): 
		self.radius = radius

	@property
		def diameter(self): 
			return 2 * self.radius
			
>>> c = Circle(5) 
>>> c.radius
5

>>> c.diameter
10

>>> c.radius = 7 
>>> c.diameter 
14

>>> c.diameter = 20
Traceback (most recent call last):
File "<stdin>", line 1, in <module> 
AttributeError: can't set attribute
```

## Name Mangling for Privacy

```python
class Duck():
def __init__(self, input_name): 
	self.__name = input_name
	@property
	def name(self):
		print('inside the getter') 
		return self.__name
	
	@name.setter
	def name(self, input_name): 
		print('inside the setter') 
		self.__name = input_name	

>>> fowl = Duck('Howard') 
>>> fowl.name
inside the getter 'Howard'
>>> fowl.name = 'Donald' 
inside the setter
>>> fowl.name
inside the getter 'Donald'

>>> fowl.__name
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'Duck' object has no attribute '__name'
```

## Method Types
```python
class A():
	count = 0
	def __init__(self):
		A.count += 1
	def exclaim(self):
		print("I'm an A!")
		
	@classmethod
	def kids(cls):
		print("A has", cls.count, "little objects.")

>>> easy_a = A()
>>> breezy_a = A()
>>> wheezy_a = A()
>>> A.kids()
A has 3 little objects.


class CoyoteWeapon():
	@staticmethod
	def commercial():
		print('This CoyoteWeapon has been brought to you by Acme')

>>> CoyoteWeapon.commercial()
This CoyoteWeapon has been brought to you by Acme

```

## Duck Typing

```python
class Quote():
	def __init__(self, person, words): 
		self.person = person 
		self.words = words
	def who(self):
		return self.person says(self):
	
	def says(self):
		return self.words + '.'


class QuestionQuote(Quote):
	def says(self):
		return self.words + '?'
		

class ExclamationQuote(Quote):
	def says(self):
		return self.words + '!' 


>>> hunter = Quote('Elmer Fudd', "I'm hunting wabbits") 
>>> print(hunter.who(), 'says:', hunter.says())
Elmer Fudd says: I'm hunting wabbits.

>>> hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc") 
>>> print(hunted1.who(), 'says:', hunted1.says())
Bugs Bunny says: What's up, doc?

>>> hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season") 
>>> print(hunted2.who(), 'says:', hunted2.says())
Daffy Duck says: It's rabbit season!




class BabblingBrook():
	def who(self):
		return 'Brook'
	
	def says(self):
		return 'Babble'
 
>>> brook = BabblingBrook()

def who_says(obj):
	print(obj.who(), 'says', obj.says())

>>> who_says(hunter)
Bugs Bunny says What's up, doc? 

>>> who_says(hunted1)
Elmer Fudd says I'm hunting wabbits.

>>> who_says(hunted2)
Daffy Duck says It's rabbit season! 
>>> who_says(brook)
Brook says Babble
```

## Special Methods
```python
class Word():
	def __init__(self, text):
		self.text = text
	
	def equals(self, word2):
		return self.text.lower() == word2.text.lower()
	
>>> first = Word('ha')
>>> second = Word('HA')
>>> third = Word('eh')

>>> first.equals(second)
True

>>> first.equals(third)
False


class Word():
	def __init__(self, text):
		self.text = text
	
	def __eq__(self, word2):
		return self.text.lower() == word2.text.lower()


>>> first = Word('ha')
>>> second = Word('HA')
>>> third = Word('eh')
>>> first == second
True
>>> first == third
False
```

```python
Table 6-1. Magic methods for comparison  
__eq__(self, other) self==other  
__ne__(self, other) self!=other  
__lt__(self, other) self<other  
__gt__(self, other) self>other  
__le__(self, other) self<=other  
__ge__(self, other) self>=other  


Table 6-2. Magic methods for math  
__add__(self, other)  
__sub__(self, other)   
__mul__(self, other)   
__floordiv__(self, other)   
__truediv__(self, other)  
__mod__(self, other)  
__pow__(self, other)  

Table 6-3. Other, miscellaneous magic methods  
__str__(self) str(self)  
__repr__(self) repr(self)  
__len__(self) len(self)  
```

```python
>>> first = Word('ha')
>>> first
<__main__.Word object at 0x1006ba3d0> 
>>> print(first)
<__main__.Word object at 0x1006ba3d0>


class Word():
	def __init__(self, text):
		self.text = text
		
	def __eq__(self, word2):
		return self.text.lower() == word2.text.lower()
		
	def  __str__(self):
		return self.text __repr__(self):
	
	def __repr__(self):
		return 'Word("' self.text '")'

>>> first = Word('ha')
>>> first # uses __repr__ Word("ha")
>>> print(first) # uses __str__ ha
```

## Composition

```python
class Bill():
	def __init__(self, description):
		self.description = description
		
class Tail():
	def __init__(self, length):
		self.length = length

class Duck():
	def __init__(self, bill, tail): 
		self.bill = bill
		self.tail = tail 
	
	def about(self):
		print('This duck has a', bill.description, 'bill and a', tail.length, 'tail')

>>> tail = Tail('long')
>>> bill = Bill('wide orange')
>>> duck = Duck(bill, tail)
>>> duck.about()
This duck has a wide orange bill and a long tail

```

## When to Use Classes and Objects versus Modules

```python

```

## Named Tuples

```python
>>> from collections import namedtuple 
>>> Duck = namedtuple('Duck', 'bill tail') 
>>> duck = Duck('wide orange', 'long') 
>>> duck
Duck(bill='wide orange', tail='long')
>>> duck.bill
'wide orange'
>>> duck.tail
'long'



parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
duck2
Duck(bill='wide orange', tail='long')


>>> duck2 = Duck(bill = 'wide orange', tail = 'long')

>>> duck3 = duck2._replace(tail='magnificent', bill='crushing') 
>>> duck3
Duck(bill='crushing', tail='magnificent')

>>> duck_dict = {'bill': 'wide orange', 'tail': 'long'} 
>>> duck_dict
{'tail': 'long', 'bill': 'wide orange'}

>>> duck_dict['color'] = 'green'
>>> duck_dict
{'color': 'green', 'tail': 'long', 'bill': 'wide orange'}

>>> duck.color = 'green' 
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'color'

```