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


- **decorator的範例1,計算一個function執行所花費的時間**

```python
import time
def timer_decorator(func):
  def wrapper():
    start_time = time.time()
    func()
    end_time = time.time()
    print(f"func.__name__花費{end_time-start_time:.4f}秒執行")

  
  return wrapper
  
@timer_decorator
def slow_function():
  time.sleep(2)
  print("function執行完成")

slow_function()

#========output=========
function執行完成
func.__name__花費2.0021秒執行
```

- **decorator的範例2,接受引數的decorator**

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

- **decorator的範例3,檢查輸入的引數值是int或float並小於0**

```python
def validate_positive_numbers(func):
  def wrapper(*args,**kwargs):
    for arg in args:
      if isinstance(arg,(int, float)) and arg < 0:
        raise ValueError("引數值必需是int或float並且大於0")
    return func(*args, **kwargs)
  return wrapper

@validate_positive_numbers
def calculate_square_root(number):
  return number ** 0.5
  
try:
  calculate_square_root(-10)
except Exception as e:
  print(e)
  
#======output========
引數值必需是int或float並且大於0
```

- **decorator的範例4,將function輸出的值全部轉成大寫**

```python
def uppercase_decorator(func):
  def wrapper():
    original_result = func()
    return original_result.upper()  
  return wrapper

@uppercase_decorator
def greet():
  return "hello, world!"

print(greet())

#========output========
HELLO, WORLD!
```

## Class Decorator

```python
class SimpleDecorator:
  def __init__(self,func):
    self.func = func

  def __call__(self):
    print("function執行前")
    self.func()
    print("function執行後")
    
@SimpleDecorator
def say_hello():
  print("Hello!")

say_hello()

#=========output==========
# Output:
function執行前
Hello!
function執行後
```

## Decorator with parameter
- 建立一個decorator factory

```python
def decorator_with_params(prefix):
  def actual_decorator(func):
    def wrapper(*args, **kwargs):
      print(f"{prefix}:function 呼叫前")
      result = func(*args, **kwargs)
      print(f'{prefix}:function呼叫後')
      return result
    return wrapper
  return actual_decorator

@decorator_with_params("DEBUG")
def greet(name):
  print(f"Hello, {name}")

greet("Alice")

#======output=======
DEBUG:function 呼叫前
Hello, Alice
DEBUG:function呼叫後
```

## functools.wraps的功能
使用在decorator function內的重要功能

- function的名稱(__name__)變為wrapper function的名稱
- function的名稱docstring(__doc__)變為wrapper function的docstring

要排除上面的方法就要使用functools.wraps的功能

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper docstring."""
        print("Wrapper executed!")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """Original docstring."""
    print("Hello!")

print(greet.__name__)  # Output: greet
print(greet.__doc__)   # Output: Original docstring
```





