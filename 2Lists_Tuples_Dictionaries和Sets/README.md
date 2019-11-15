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

```python
>>> small_birds = ['hummingbird', 'finch']
>>> extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue'] 
>>> carol_birds = [3, 'French hens', 2, 'turtledoves']
>>> all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]


>>> all_birds
	[['hummingbird', 'finch'], ['dodo', 'passenger pigeon', 'Norwegian Blue'], 'macaw', [3, 'French hens', 2, 'turtledoves']]


>>> all_birds[0]
   ['hummingbird', 'finch']


>>> all_birds[1]
['dodo', 'passenger pigeon', 'Norwegian Blue']


>>> all_birds[1][0] 
'dodo'


>>> marxes = ['Groucho', 'Chico', 'Harpo']
>>> marxes[2] = 'Wanda'
>>> marxes
['Groucho', 'Chico', 'Wanda']


>>> marxes = ['Groucho', 'Chico,' 'Harpo']
>>> marxes[0:2]
['Groucho', 'Chico']


>>> marxes[::2]
['Groucho', 'Harpo']


>>> marxes[::-2] 
['Harpo', 'Groucho']


>>> marxes[::-1]
['Harpo', 'Chico', 'Groucho']


>>> marxes.append('Zeppo')
>>> marxes
['Groucho', 'Chico', 'Harpo', 'Zeppo']


>>> marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo'] 
>>> others = ['Gummo', 'Karl']
>>> marxes.extend(others)
>>> marxes
['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']


>>> marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
>>> others = ['Gummo', 'Karl']
>>> marxes += others
>>> marxes
['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']


>>> marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo'] 
>>> others = ['Gummo', 'Karl']
>>> marxes.append(others)
>>> marxes
['Groucho', 'Chico', 'Harpo', 'Zeppo', ['Gummo', 'Karl']]


>>> marxes.insert(3, 'Gummo') 
>>> marxes
['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']


>>> marxes.insert(10, 'Karl')
>>> marxes
['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo', 'Karl']


>>> del marxes[-1]
>>> marxes
['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']


>>> marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo'] 
>>> marxes[2]
'Harpo'
>>> del marxes[2]
>>> marxes
['Groucho', 'Chico', 'Gummo', 'Zeppo']
>>> marxes[2]
'Gummo'


>>> marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo'] 
>>> marxes.remove('Gummo')
>>> marxes
['Groucho', 'Chico', 'Harpo', 'Zeppo']


>>> marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo'] 
>>> marxes.pop()
'Zeppo'
>>> marxes
['Groucho', 'Chico', 'Harpo'] >>> marxes.pop(1)
'Chico'
>>> marxes
['Groucho', 'Harpo']


>>> marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo'] 
>>> marxes.index('Chico')
1


>>> marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo'] 
>>> 'Groucho' in marxes
True
>>> 'Bob' in marxes
False


>>> words = ['a', 'deer', 'a' 'female', 'deer'] 
>>> 'deer' in words
True


>>> marxes = ['Groucho', 'Chico', 'Harpo'] 
>>> marxes.count('Harpo')
1
>>> marxes.count('Bob')
0
>>> snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger'] 
>>> snl_skit.count('cheeseburger')
3


>>> marxes = ['Groucho', 'Chico', 'Harpo'] 
>>> ', '.join(marxes)
'Groucho, Chico, Harpo'


>>> friends = ['Harry', 'Hermione', 'Ron'] 
>>> separator = ' * '
>>> joined = separator.join(friends)
>>> joined
'Harry * Hermione * Ron'
>>> separated = joined.split(separator) 
>>> separated
['Harry', 'Hermione', 'Ron']
>>> separated == friends
True


>>> marxes = ['Groucho', 'Chico', 'Harpo'] 
>>> sorted_marxes = sorted(marxes)
>>> sorted_marxes
['Chico', 'Groucho', 'Harpo']


>>> marxes
['Groucho', 'Chico', 'Harpo']
>>> marxes.sort()
>>> marxes
['Chico', 'Groucho', 'Harpo']


>>> numbers = [2, 1, 4.0, 3] 
>>> numbers.sort()
>>> numbers
[1, 2, 3, 4.0]


>>> numbers = [2, 1, 4.0, 3] 
>>> numbers.sort(reverse=True) 
>>> numbers
[4.0, 3, 2, 1]


>>> marxes = ['Groucho', 'Chico', 'Harpo']
>>> len(marxes)
3


>>>a=[1,2,3] 
>>> a
[1, 2, 3] 
>>>b=a


>>> b
[1, 2, 3]
>>> a[0] = 'surprise'
>>> a
['surprise', 2, 3]
>>> b
['surprise', 2, 3]


>>> b
['surprise', 2, 3]
>>> b[0] = 'I hate surprises'
>>> b
['I hate surprises', 2, 3]
>>> a
['I hate surprises', 2, 3]


>>>a=[1,2,3] 
>>> b = a.copy() 
>>> c = list(a) 
>>>d=a[:]


>>> a[0] = 'integer lists are boring'
>>> a
['integer lists are boring', 2, 3]
>>> b
[1, 2, 3]
>>> c
[1, 2, 3]
>>> d
[1, 2, 3]

```

## Tuples

```python
>>> empty_tuple = () 
>>> empty_tuple
()


>>> one_marx = 'Groucho', 
>>> one_marx ('Groucho',)


>>> marx_tuple = 'Groucho', 'Chico', 'Harpo' 
>>> marx_tuple
('Groucho', 'Chico', 'Harpo')


>>> marx_tuple = ('Groucho', 'Chico', 'Harpo') 
>>> marx_tuple
('Groucho', 'Chico', 'Harpo')


>>> marx_tuple = ('Groucho', 'Chico', 'Harpo') 
>>> a, b, c = marx_tuple
>>> a
'Groucho'
>>> b
'Chico'
>>> c
'Harpo'


>>> password = 'swordfish'
>>> icecream = 'tuttifrutti'
>>> password, icecream = icecream, password
>>> password
'tuttifrutti'
>>> icecream
'swordfish'


>>> marx_list = ['Groucho', 'Chico', 'Harpo'] 
>>> tuple(marx_list)
('Groucho', 'Chico', 'Harpo')
```

## Dictionaries

```python
>>> empty_dict = {} 
>>> empty_dict
{}


>>> bierce = {
... "day": "A period of twenty-four hours, mostly misspent",
... "positive": "Mistaken at the top of one's voice",
... "misfortune": "The kind of fortune that never misses",
... } 
>>>


>>> bierce
{'misfortune': 'The kind of fortune that never misses', 'positive': "Mistaken at the top of one's voice", 'day': 'A period of twenty-four hours, mostly misspent'}


>>> lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
>>> dict(lol)
{'c': 'd', 'a': 'b', 'e': 'f'}


>>> lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
>>> dict(lot)
{'c': 'd', 'a': 'b', 'e': 'f'}


>>> tol = ( ['a', 'b'], ['c', 'd'], ['e', 'f'] )
>>> dict(tol)
{'c': 'd', 'a': 'b', 'e': 'f'}


>>> los = [ 'ab', 'cd', 'ef' ]
>>> dict(los)
{'c': 'd', 'a': 'b', 'e': 'f'}


>>> tos = ( 'ab', 'cd', 'ef' )
>>> dict(tos)
{'c': 'd', 'a': 'b', 'e': 'f'}


>>> pythons = {
... 'Chapman': 'Graham',
... 'Cleese': 'John',
... 'Idle': 'Eric',
... 'Jones': 'Terry',
... 'Palin': 'Michael',
... }
>>> pythons
{'Cleese': 'John', 'Jones': 'Terry', 'Palin': 'Michael', 'Chapman': 'Graham', 'Idle': 'Eric'}


>>> pythons['Gilliam'] = 'Gerry'
>>> pythons
{'Cleese': 'John', 'Gilliam': 'Gerry', 'Palin': 'Michael',
'Chapman': 'Graham', 'Idle': 'Eric', 'Jones': 'Terry'}


>>> pythons['Gilliam'] = 'Terry'
>>> pythons
{'Cleese': 'John', 'Gilliam': 'Terry', 'Palin': 'Michael',
'Chapman': 'Graham', 'Idle': 'Eric', 'Jones': 'Terry'}


>>> some_pythons = {
... 'Graham': 'Chapman',
... 'John': 'Cleese',
... 'Eric': 'Idle',
... 'Terry': 'Gilliam',
... 'Michael': 'Palin',
... 'Terry': 'Jones',
... }
>>> some_pythons
{'Terry': 'Jones', 'Eric': 'Idle', 'Graham': 'Chapman', 'John': 'Cleese', 'Michael': 'Palin'}


>>> pythons = {
... 'Chapman': 'Graham',
... 'Cleese': 'John',
... 'Gilliam': 'Terry',
... 'Idle': 'Eric',
... 'Jones': 'Terry',
... 'Palin': 'Michael'
... }
>>> pythons
{'Cleese': 'John', 'Gilliam': 'Terry', 'Palin': 'Michael', 'Chapman': 'Graham', 'Idle': 'Eric', 'Jones': 'Terry'}


>>> others = { 'Marx': 'Groucho', 'Howard': 'Moe' }
>>> pythons.update(others)
>>> pythons
{'Cleese': 'John', 'Howard': 'Moe', 'Gilliam': 'Terry', 'Palin': 'Michael', 'Marx': 'Groucho', 'Chapman': 'Graham', 'Idle': 'Eric', 'Jones': 'Terry'}


>>> first = {'a': 1, 'b': 2} 
>>> second = {'b': 'platypus'} 
>>> first.update(second)
>>> first
{'b': 'platypus', 'a': 1}


>>> del pythons['Marx']
>>> pythons
{'Cleese': 'John', 'Howard': 'Moe', 'Gilliam': 'Terry', 'Palin': 'Michael', 'Chapman': 'Graham', 'Idle': 'Eric', 'Jones': 'Terry'}
>>> del pythons['Howard']
>>> pythons
{'Cleese': 'John', 'Gilliam': 'Terry', 'Palin': 'Michael', 'Chapman': 'Graham', 'Idle': 'Eric', 'Jones': 'Terry'}


>>> pythons.clear() 
>>> pythons
{}
>>> pythons = {}
>>> pythons
{}


>>> pythons = {'Chapman': 'Graham', 'Cleese': 'John',
'Jones': 'Terry', 'Palin': 'Michael'}
>>> 'Chapman' in pythons 
True
>>> 'Palin' in pythons 
True
>>> 'Gilliam' in pythons 
False


>>> pythons['Cleese']
'John'


>>> pythons['Marx']
    Traceback (most recent call last):
File "<stdin>", line 1, in <module> KeyError: 'Marx'


>>> 'Marx' in pythons 
False


>>> pythons.get('Cleese') 
'John'


>>> pythons.get('Marx', 'Not a Python')
'Not a Python'


>>> signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'} 
>>> signals.keys()
dict_keys(['green', 'red', 'yellow'])


>>> list( signals.values() )
['go', 'smile for the camera', 'go faster']


>>> list( signals.items() )
[('green', 'go'), ('red', 'smile for the camera'), ('yellow', 'go faster')]


>>> signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'} 
>>> save_signals = signals
>>> signals['blue'] = 'confuse everyone'
>>> save_signals
    {'blue': 'confuse everyone', 'green': 'go',
    'red': 'smile for the camera', 'yellow': 'go faster'}


>>> signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'} >>> original_signals = signals.copy()
>>> signals['blue'] = 'confuse everyone'
>>> signals
{'blue': 'confuse everyone', 'green': 'go',
'red': 'smile for the camera', 'yellow': 'go faster'}
>>> original_signals
{'green': 'go', 'red': 'smile for the camera', 'yellow': 'go faster'}



```

## Sets

```python
>>> empty_set = set()
>>> empty_set
set()
>>> even_numbers = {0, 2, 4, 6, 8} 
>>> even_numbers
{0,8,2,4,6}
>>> odd_numbers = {1, 3, 5, 7, 9} 
>>> odd_numbers
{9,3,1,5,7}


>>> set( 'letters' )
{'l', 'e', 't', 'r', 's'}


>>> set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] ) 
{'Dancer', 'Dasher', 'Prancer', 'Mason-Dixon'}


>>> set( ('Ummagumma', 'Echoes', 'Atom Heart Mother') )
{'Ummagumma', 'Atom Heart Mother', 'Echoes'}


>>> set( {'apple': 'red', 'orange': 'orange', 'cherry': 'red'} )
{'apple', 'cherry', 'orange'}


>>> drinks = {
... 'martini': {'vodka', 'vermouth'},
... 'black russian': {'vodka', 'kahlua'},
... 'white russian': {'cream', 'kahlua', 'vodka'},
... 'manhattan': {'rye', 'vermouth', 'bitters'},
... 'screwdriver': {'orange juice', 'vodka'}
... }



```




