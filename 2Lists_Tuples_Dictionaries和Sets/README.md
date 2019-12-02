# Lists, Tuples, Dictionaries, and Sets
## String ,Lists and Tuples
- 全部都是串列元素型態,有索引編號,可以使用for in迴圈取出每一個元素
- 字串的元素,全部都是相同的字元
- tuple和list可以有不同的資料元素
- 字串和tuple都是不可變變數
- list是可變變數

## List
- 有順序的排序
- 可以有不同類型的元素
- 可新增,修改,插入元素

### 使用簡易表示法 [] or 初始化 list()建立list

```python
>>> empty_list = [ ]
>>> weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] 
>>> big_birds = ['emu', 'ostrich', 'cassowary']
>>> first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']


>>> another_empty_list = list() 
>>> another_empty_list
[]
```

### 使用list()轉換其它型態為list
```python
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

```

### 使用[offset],取得元素

```python
>>> marxes = ['Groucho', 'Chico', 'Harpo']
>>> marxes[0]
    'Groucho'
>>> marxes[1]
	'Chico'
>>> marxes[2]
	'Harpo'

#使用負數索引從-1...-n,由後取得元素
>>> marxes[-1] 
'Harpo'
>>> marxes[-2] 
'Chico'
>>> marxes[-3] 
'Groucho'

#索引超過,將會產生IndexError
>>> marxes = ['Groucho', 'Chico', 'Harpo'] 
>>> marxes[5]

Traceback (most recent call last):
File "<stdin>", line 1, in <module> 
IndexError: list index out of range

>>> marxes[-5]

Traceback (most recent call last):
File "<stdin>", line 1, in <module> 
IndexError: list index out of range

```

```python
>>> small_birds = ['hummingbird', 'finch']
>>> extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue'] 
>>> carol_birds = [3, 'French hens', 2, 'turtledoves']
>>> all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
```

### 巢狀List

```python
>>> all_birds
	[['hummingbird', 'finch'], ['dodo', 'passenger pigeon', 'Norwegian Blue'], 'macaw', [3, 'French hens', 2, 'turtledoves']]


>>> all_birds[0]
   ['hummingbird', 'finch']


>>> all_birds[1]
['dodo', 'passenger pigeon', 'Norwegian Blue']


>>> all_birds[1][0] 
'dodo'
```

### 使用[offset]修改內容

```python
>>> marxes = ['Groucho', 'Chico', 'Harpo']
>>> marxes[2] = 'Wanda'
>>> marxes
['Groucho', 'Chico', 'Wanda']

```

### 使用切割語法[起始值:結束值:增值],取出數個元素

```python
>>> marxes = ['Groucho', 'Chico,' 'Harpo']
>>> marxes[0:2]
['Groucho', 'Chico']


>>> marxes[::2]
['Groucho', 'Harpo']


>>> marxes[::-2] 
['Harpo', 'Groucho']


>>> marxes[::-1]
['Harpo', 'Chico', 'Groucho']

```

### 使用append(), 增加元素增加至list的尾部

```python
>>> marxes.append('Zeppo')
>>> marxes
['Groucho', 'Chico', 'Harpo', 'Zeppo']

```

### 使用 += 或 extend() 組合多個list

```python
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

```

### 使用insert()插入元素

```python
>>> marxes.insert(3, 'Gummo') 
>>> marxes
['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']


>>> marxes.insert(10, 'Karl')
>>> marxes
['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo', 'Karl']

```

### 使用del刪除元素
- del是敘述式

```python
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
```

### 使用remove(),藉由元素值來移除元素

```python

>>> marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo'] 
>>> marxes.remove('Gummo')
>>> marxes
['Groucho', 'Chico', 'Harpo', 'Zeppo']

```

### 使用pop(),來取得元素並刪除該元素

```python
>>> marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo'] 
>>> marxes.pop()
'Zeppo'
>>> marxes
['Groucho', 'Chico', 'Harpo'] >>> marxes.pop(1)
'Chico'
>>> marxes
['Groucho', 'Harpo']

```

### 使用index()方法,透過元素值,取得索引編號

```python
>>> marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo'] 
>>> marxes.index('Chico')
1
```

### 使用in運算子,檢查是否有包含此值

```python

>>> marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo'] 
>>> 'Groucho' in marxes
True
>>> 'Bob' in marxes
False


>>> words = ['a', 'deer', 'a' 'female', 'deer'] 
>>> 'deer' in words
True

```

### 使用count()方法,取得相同元素值的數量

```python
>>> marxes = ['Groucho', 'Chico', 'Harpo'] 
>>> marxes.count('Harpo')
1
>>> marxes.count('Bob')
0
>>> snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger'] 
>>> snl_skit.count('cheeseburger')
3

```

### 使用字串方法,組合list元素值,成為字串

```python
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

```

### 排序list
- 使用sorted() function傳出新排序的list
- 使用list.sort() 方法,重新排序自身的list

```python
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

```

### 使用len() function取得list的元素數量

```python
>>> marxes = ['Groucho', 'Chico', 'Harpo']
>>> len(marxes)
3

```

### 使用=,copy參考,使用copy()方法,拷貝全新的list

```python
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
### 使用()建立tuple
- 不可改變的內容

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
- 有key和value 

### 使用{}建立Dictionary

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

```

### 使用dict()初始化建立dictionary

```python
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

```

### 使用[key]增加和改變value

```python
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
```

### 使用update()組合Dictionary

```python
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

```

### del 刪除元素

```pythone
>>> del pythons['Marx']
>>> pythons
{'Cleese': 'John', 'Howard': 'Moe', 'Gilliam': 'Terry', 'Palin': 'Michael', 'Chapman': 'Graham', 'Idle': 'Eric', 'Jones': 'Terry'}
>>> del pythons['Howard']
>>> pythons
{'Cleese': 'John', 'Gilliam': 'Terry', 'Palin': 'Michael', 'Chapman': 'Graham', 'Idle': 'Eric', 'Jones': 'Terry'}
```

### 使用clear()刪除所有內容

```python
>>> pythons.clear() 
>>> pythons
{}
>>> pythons = {}
>>> pythons
{}

```

### 使用in檢查dictionary有沒有這個key

```python
>>> pythons = {'Chapman': 'Graham', 'Cleese': 'John',
'Jones': 'Terry', 'Palin': 'Michael'}
>>> 'Chapman' in pythons 
True
>>> 'Palin' in pythons 
True
>>> 'Gilliam' in pythons 
False

```

### 使用[key]取得值

```python
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

```

### 使用keys()取得所有的key

```python
>>> signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'} 
>>> signals.keys()
dict_keys(['green', 'red', 'yellow'])

```

### 使用values(), 取得所有的值

```python
>>> list( signals.values() )
['go', 'smile for the camera', 'go faster']

```

### 使用items(),取得配對的tuple

```python
>>> list( signals.items() )
[('green', 'go'), ('red', 'smile for the camera'), ('yellow', 'go faster')]

```

### 使用=建立新參考,使用copy()建立新的拷貝

```python
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
### 使用set()建立set

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

```

### 使用set()轉換其它資料類型為set

```python
>>> set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] ) 
{'Dancer', 'Dasher', 'Prancer', 'Mason-Dixon'}


>>> set( ('Ummagumma', 'Echoes', 'Atom Heart Mother') )
{'Ummagumma', 'Atom Heart Mother', 'Echoes'}


>>> set( {'apple': 'red', 'orange': 'orange', 'cherry': 'red'} )
{'apple', 'cherry', 'orange'}

```

### 使用in檢查值

```python
>>> drinks = {
... 'martini': {'vodka', 'vermouth'},
... 'black russian': {'vodka', 'kahlua'},
... 'white russian': {'cream', 'kahlua', 'vodka'},
... 'manhattan': {'rye', 'vermouth', 'bitters'},
... 'screwdriver': {'orange juice', 'vodka'}
... }


>>> for name, contents in drinks.items():
...    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents): 
			print(name)

screwdriver
black russian
```




