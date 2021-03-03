# 物件和類別
## 使用class定義類別
- 變數, 稱為屬性(instance attribute)
- 函式, 稱為方法(instance method)

### 建立一個最簡單的類別

```python
class Person():
	pass

>>> someone = Person()
```

### 建立一個有自訂初始化功能的類別

- 引數self代表是呼叫這個實體的參考

```
class Person():
	def __init__(self): 
		pass

```

### 建立一個有屬性name

```
class Person():
	def __init__(self, name):
		self.name = name

>>> hunter = Person('Elmer Fudd')
>>> print('The mighty hunter: ', hunter.name)
The mighty hunter: Elmer Fudd
```

### hunter = Person('Elmer Fudd')
#### 這行程式同時代表6個意思
1. 尋找Person類別
2. 在記憶體內建立實體
3. 呼叫Person類別內的__init__(self,name), 將引數字串'Elmer Fudd'傳遞給參數name
4. 儲存'Elmer Fudd'儲存至實體的name屬性內
5. 傳出這個實體的參考
6. 將參考儲存至hunter變數

### 注意事項
- __init__方法不是一定要實作的
- name屬性在Person定義的類別內的存取，必需使用self.name,但當建立真實的實體後必需使用參考名稱.name,本範例為hunter.name

## 繼承

- 透過建立全新的類別，以便擴充現有的類別功能。
- 因為有繼承的關係，所有有父類別和子類別區分，以下範例，Car是父類別，Yugo為子類別

```python
class Car():
	pass

class Yugo(Car):
	pass

>>> give_me_a_car = Car() 
>>> give_me_a_yugo = Yugo()
```

- 當父類別有增加一個方法時，子類別也將會繼承這個方法
- 呼叫方法exclaim()時，程式自動會將實體的參考傳給參數self

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

## 覆寫方法

- 子類別透過覆寫更改父類別方法的功能

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

```

- 實作__init__()就是覆寫父類別的__init__()
```python
class Person():
    def __init__(self,name):
        self.name = name

class MDPerson(Person):
    pass

class JDPerson(Person):
    pass

person = Person('Fudd')
doctor = MDPerson('robert')
lawyer = JDPerson('Alice')
```

```python
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
>>> doctor = MDPerson('Robert') 
>>> lawyer = JDPerson('Alice') 
>>> print(person.name)
Fudd
>>> print(doctor.name) 
Doctor Robert
>>> print(lawyer.name) 
Alice, Esquire

```

## 子類別增加一個方法

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

## 使用super()呼叫父類別

```python
class Person():
	def __init__(self, name):
		self.name = name


class EmailPerson(Person):
	#當建立自訂的__init__,就不會繼承父類別的__init__
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

## self

```python

>>> car = Car() 
>>> car.exclaim() 
I'm a Car!

#也可以使用這種語法,但不建議使用-類別名稱.實體方法(實體參考)
>>> Car.exclaim(car)
I'm a Car!

```

## 實體property屬性

- 實作屬性attribute的Getter和Setter方法成為一個新屬性(Property)
- 目的是讓實體不可以直接存取屬性attribute

### 方法1:
- 建立attribute的getter
- 建立attributer的setter
- 使用name = property(get,set), 建立name property

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

```

### 方法2做用decorators

- @preperty,定義getter 方法
- @name.setter,定義setter 方法

```
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

```

> 注意:上方的範例，實際上還是可以直接存取hidden_name(attribute)

### 僅建立getter property

```python
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

## 建立private 屬性(attribute)

- 使用符號 __屬性名稱

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

## 類別方法和類別屬性

- 類別方法是為類別建立獨自的類別功能
- @classmethod修飾詞建立類別方法
- 使用類別方法和類別屬性時，必需使用-類別名稱.類別屬性或類別名稱.類別方法
- 建立類別方法必需要有一個參數(cls),cls代表類別

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
```

### 靜態類別方法
- 使用@staticmethod
- 靜態類別方法可以不用參數

```
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