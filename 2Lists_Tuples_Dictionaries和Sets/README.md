# Lists, Tuples, Dictionaries, and Sets

## Create with [] or list()

```python
>>> empty_list = [ ]
>>> weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] 
>>> big_birds = ['emu', 'ostrich', 'cassowary']
>>> first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']


>>> another_empty_list = list() 
>>> another_empty_list
[]


#使用list()轉換其它型態為list
>>> list('cat')
    ['c', 'a', 't']

>>> a_tuple = ('ready', 'fire', 'aim') 
>>> list(a_tuple)
['ready', 'fire', 'aim']


>>> birthday = '1/6/1952' 
>>> birthday.split('/') 
['1', '6', '1952']

>>> splitme = 'a/b//c/d///e'
>>> splitme.split('/')
['a', 'b', '', 'c', 'd', '', '', 'e']


>>> splitme = 'a/b//c/d///e' 
>>> splitme.split('//')
['a/b', 'c/d', '/e']


>>> marxes = ['Groucho', 'Chico', 'Harpo']
>>> marxes[0]
    'Groucho'
>>> marxes[1]
	'Chico'
>>> marxes[2]
	'Harpo'
	
>>> marxes[-1] 
'Harpo'
>>> marxes[-2] 
'Chico'
>>> marxes[-3] 
'Groucho'

>>> marxes = ['Groucho', 'Chico', 'Harpo'] 
>>> marxes[5]
Traceback (most recent call last):
File "<stdin>", line 1, in <module> IndexError: list index out of range
>>> marxes[-5]
Traceback (most recent call last):
File "<stdin>", line 1, in <module> IndexError: list index out of range



```





