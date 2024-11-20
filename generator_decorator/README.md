# Generator和Decorator

## Generators
- generator是一個串列資料，可以存放大量資料，但不會建立和儲存全部資料於記憶體內。
- range()產生的就是一個generators
- generators只可以使用一次

```python
def my_generator():
    for i in range(10):
        yield i

g = my_generator()

print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2

```

### Generators is iteration

```python
def my_generator():
    for i in range(10):
        yield i


for i in my_generator():
    print(i)
```

- **使用Comprehensions 建立Generators**

```python
squares = (i * i for i in range(10))

for square in squares:
    print(square)

even_squares = (i * i for i in range(10) if i % 2 == 0)

for square in even_squares:
    print(square)

sum_of_squares = sum(i * i for i in range(10))
print(sum_of_squares)
```

- **range()也可以建立Generators**

```python
>>> sum(range(1, 101))
5050


def my_range(first=0, last=10, step=1):
	number = first
	while number < last:
		yield number #透過yield建立generator的元素
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

## Decorators
**修飾已經有的function功能，但不需要更改到裏面原本的內容程式碼**

### 由淺而深了解Decorator

### 1. python的Function是First-Class物件

代表function可以指定給變數,function可以當作參數,function可以當作另一個function的return值

### 2. Function是物件,代表有型別
- **使用Callable常作型別提示(type hint)**
- **自已定義一個function型別**

```python
from typing import Callable

# Define a function type: A function that takes two integers and returns a string
MyFunctionType = Callable[[int, int], str]

# Example of a function matching this type
def my_function(a: int, b: int) -> str:
    return f"The sum is {a + b}"

# Function with the specified type as a parameter
def apply_function(func: MyFunctionType, x: int, y: int) -> str:
    return func(x, y)

# Usage
result = apply_function(my_function, 3, 5)
print(result)  # Output: The sum is 8

```

- **如果function有很多的參數**

```python
from typing import Callable
AnyFunction = Callable[..., str]
```


- **function指定給變數**

```python
def greet():
    return "Hello"

say_hello = greet
print(say_hello())  # Output: Hello
```

- **inner function(function內可以有function)**

```python
def greet():
    return "Hello"

say_hello = greet
print(say_hello())  # Output: Hello
```

- **function當作包裝器(Decorator的本質)**
	- 要成為包裝器,必需接收一個function當作參數,並且傳出(return)一個新的function
	- Decorator的本質就是擴充使用者提供的function功能

```python
#手動寫法
def say_hello():
    print("Hello!")
    
def decorator_function(original_function):
    def wrapper_function():
        print("擴增的功能!")
        original_function()
    return wrapper_function

decorated_function = decorator_function(say_hello)
decorated_function()
# =====Output:============
# 擴增的功能!
# Hello!
```

```python
#使用@語法,簡化寫法

    
def decorator_function(original_function):
    def wrapper_function():
        print("擴增的功能!")
        original_function()
    return wrapper_function

@decorator_function
def say_hello():
	print("Hello")

say_hello()
# =====Output:============
# 擴增的功能!
# Hello!
```

- **decorator的範例1**

```python
def log_decorator(func):
  def wrapper(*args, **kwargs):
    print(f'Calling {func.__name__} with {args} and {kwargs}')
    return func(*args,**kwargs)
  return wrapper

@log_decorator
def add(a,b):
  return a + b

print(add(3, 4))
```






一個decorator是一個function, 這個function有一個參數，可以利用參數傳入其它function,然後傳出其它修改過的function

下方的程式碼包含

- *args 和 **kwargs
- Inner functions
- Functions 當作引數


```python
def document_it(func):
    def new_function(*args, **kwargs):
        print('要執行的function:',func.__name__)
        print('引數位置:',args)
        print('keyword引數名稱',kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

#手動傳遞function當作參數
def add_ints(a, b): 
	return a+b

>>> add_ints(3, 5)
8

>>> cooler_add_ints = document_it(add_ints) # manual decorator assignment
>>> cooler_add_ints(3, 5) 
要執行的function: add_ints
引數位置: (3, 5)
keyword引數名稱 {}
Result: 8
8

#另一種傳遞function當作參數的寫法,使用@
@document_it
def add_ints(a, b):
	returna+b

>>> add_ints(3, 5)
要執行的function: add_ints
引數位置: (3, 5)
keyword引數名稱 {}
Result: 8
8


#也可以傳遞一個function給多個decorator
def square_it(func):
	def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
		return result * result
	return new_function

#同時使用2個decorator
@document_it
@square_it
def add_ints(a, b):
	return a+b

>>> add_ints(3, 5)
要執行的function: new_function
引數位置: (3, 5)
keyword引數名稱 {}
Result: 64
64


#改變decorator的順序
@square_it
@document_it
def add_ints(a, b):
return a+b 

>>> add_ints(3, 5) 
要執行的function: add_ints
引數位置: (3, 5)
keyword引數名稱 {}
Result: 8
64

```