# Modules, Packages, and Programs
## Standalone Programs
```python
#test.py

>>> print("This interactive snippet works.") 
This interactive snippet works.


$ python test1.py
This standalone program works!
```

## Command-Line Arguments

```python
# test2.py 

import sys
print('Program arguments:', sys.argv)


$ python test2.py
Program arguments: ['test2.py']
$ python test2.py tra la la
Program arguments: ['test2.py', 'tra', 'la', 'la']

```

## Modules and the import Statement

```python
#A module is just a file of Python code.
```

### Import a Module
```python
#module is the name of another Python file, without the .py extension

# weatherman.py

import report
description = report.get_description() 
print("Today's weather:", description)

# report.py

def get_description(): # see the docstring below? 
	"""Return random weather, just like the pros""" 

	from random import choice
	possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows'] 
	return choice(possibilities)



$ python weatherman.py 
Today's weather: who knows 
$ python weatherman.py 
Today's weather: sun
$ python weatherman.py 
Today's weather: sleet



def get_description(): 
	import random
	possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows'] 
	return random.choice(possibilities)


```

```python
>>> import random
>>> def get_description():
...possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows'] 
...return random.choice(possibilities)

>>> get_description()
'who knows'
>>> get_description() 
'rain'

```

### Import a Module with Another Name

```python
import report as wr
description = wr.get_description() 
print("Today's weather:", description)

```

### Import Only What You Want from a Module

```python
from report import get_description
description = get_description()
print("Today's weather:", description)




from report import get_description as do_it 
description = do_it()
print("Today's weather:", description)

```

### Module Search Path

```python
>>> import sys
>>> for place in sys.path: 
... print(place)



/Library/Frameworks/Python.framework/Versions/3.3/lib/python33.zip
/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3 
/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/plat-darwin 
/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/lib-dynload 
/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/site-packages
```

## Packages

```python
#Main program: boxes/weather.py.

from sources import daily, weekly
print("Daily forecast:", daily.forecast()) 
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
	print(number, outlook)


#Module 1: boxes/sources/daily.py.
def forecast():
	'fake daily forecast' 
	return 'like yesterday'
	

#Module 2: boxes/sources/weekly.py.

def forecast():
	"""Fake weekly forecast"""
	return ['snow', 'more snow', 'sleet','freezing rain', 'rain', 'fog', 'hail']
	

$ python weather.py
Daily forecast: like yesterday Weekly forecast:
1 snow
2 more snow
3 sleet
4 freezing rain
5 rain
6 fog
7 hail
```

## The Python Standard Library
```python
#Python Module of the Week
#The Python Standard Li‐ brary by Example
```
