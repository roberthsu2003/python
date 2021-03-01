# 系統和時間
## 檔案
### 使用open()和print()建立檔案

- 細節的檔案處理請參考[檔案存取](../檔案存取/README.ipynb)

```python
#建立一個oops.txt

fout = open('oops.txt', 'wt')
print('喔!建立了一個檔案',file=fout)
fout.close()
```

### 使用exist()檢查檔案是否存在

```
>>> import os
>>> os.path.exists('oops.txt')
True

>>> os.path.exists('./oops.txt')
True

>>> os.path.exists('waffles')
False

>>> os.path.exists('.')
True

>>> os.path.exists('..')
True
```

### 使用isfile()檢查是否是檔案

```python
>>> name = 'oops.txt'
>>> os.path.isfile(name)
True

# 檢查是否是目錄
>>> os.path.isdir(name)
False

>>> os.path.isdir('.')
True

# 檢查是否為絕對路徑
>>> os.path.isabs(name)
False

>>> os.path.isabs('/big/fake/name')
True

>>> os.path.isabs('big/fake/name/without/a/leading/slash')
False
```

### copy()複制檔案

```python
>>> import shutil
>>> shutil.copy('oops.txt', 'ohno.txt')
ohno.txt

#.move(),移動檔案
```

### 使用rename()更變檔案名稱

```python
>>> import os
>>> os.rename('ohno.txt', 'ohwell.txt')
```

### 使用link() 或 symlink()建立link(類似捷徑)

```python
>>> os.link('oops.txt','yikes.txt')
>>> os.path.isfile('yikes.txt')
True

>>> os.path.islink('yikes.txt')
False

>>> os.symlink('oops.txt', 'jeepers.txt')
>>> os.path.islink('jeepers.txt')
True
```

### 取得檔案絕對路徑

```python
>>> os.path.abspath('oops.txt')
'/Users/roberthsu2003/Documents/GitHub/python/上課內容/oops.txt'
```

### 取得替身的真實路徑

```python
>>> os.path.realpath('jeppers.txt')
'/Users/roberthsu2003/Documents/GitHub/python/上課內容/jeppers.txt'
```

### 刪除檔案remove()

```python
>>> os.remove('oops.txt')
>>> os.path.exists('oops.txt')
False
```

## 目錄
### mkdir()建立目錄

```python
>>> os.mkdir('poems')
>>> os.path.exists('poems')
True
```

### rmdir()刪除目錄

```python
>>> os.rmdir('poems')
>>> os.path.exists('poems')
False
```

### 使用listdir()顯示目錄內容

```python
>>> os.mkdir('poems')
>>> os.listdir('poems')
[]
```

```python
>>> os.mkdir('poems/mcintyre')
>>> os.listdir('poems')
['mcintyre']
```

使用相對路徑建立一個檔案

```python
>>> fout = open('poems/mcintyre/the_good_man','wt')
>>> fout.write('''Cheerful and happy was his mood,
He to the poor was kind and good,
And he oft' times did find them food,
Also supplies of coal and wood,
He never spake a word was rude,
And cheer'd those did o'er sorrows brood,
He passed away not understood,
Because no poet in his lays
Had penned a sonnet in his praise,
'Tis sad, but such is world's ways.
''')
>>> fout.close()

>>> os.listdir('poems/mcintyre')
['the_good_man']
```

### chdir()更改目錄

```python
>>> os.chdir('poems')
>>> os.listdir('.')
['mcintyre']
```

### 程序(Processes)

```
#取得目前處理程序id
>>> import os
>>> os.getpid()
1235

#取得目前工作目錄
>>> os.getcwd()
'/Users/roberthsu2003/Documents/GitHub/python/上課內容/poems'
```

### 建立多個程序


```python
#這範例必需使用.py檔案執行，不可使用.ipynb

import multiprocessing
import os


def do_this(what):
    whoami(what)


def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))


if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this, args=("I'm function %s" % n,))
        p.start()
```

### 使用terminate()中斷子程序

```python
#這範例必需使用.py檔案執行，不可使用.ipynb
import multiprocessing
import os
import time


def whoami(name):
    print("Process %s says: %s" % (name,os.getpid()))

def loopy(name):
    whoami(name)
    start = 1
    stop = 1000000
    for num in range(start, stop):
        print("\tNumber %s of %s. BREAK!" % (num, stop))
        time.sleep(1)


if __name__ == "__main__":
    whoami("I'm the main program")
    p = multiprocessing.Process(target=loopy, args=("loopy",))
    p.start()
    time.sleep(5)
    p.terminate()
```

## 日期和時間

不同日期的表示方法

- July 29 1984
- 29 Jul 1984
- 29/7/1984
- 7/29/1984

### 檢查是否是潤年

```python
>>> import calendar
>>> calendar.isleap(1900)
False

>>> calendar.isleap(1996)
True

>>> calendar.isleap(1999)
False

>>> calendar.isleap(2000)
True

>>> calendar.isleap(2002)
False

>>> calendar.isleap(2004)
True
```

### datetime Module

#### 四個主要的物件
- date -> 年,月,日
- time -> 時,分,秒,分數
- datetime -> 年,月,日,時,分,秒,分數
- timedelta -> 一段日期和一段時間

```python
>>> from datetime import date
>>> halloween = date(2018, 10, 9)
>>> halloween
datetime.date(2018, 10, 9)

>>> halloween.isoformat()
'2018-10-09'

>>> halloween.day
9

>>> halloween.month
10

>>> halloween.year
2018
```

#### 使用today()取得現在日期

```python
>>> from datetime import date
>>> now = date.today()
>>> now

datetime.date(2021, 3, 1)
```

#### 使用timedelta取得一日期

```python
>>> from datetime import date
>>> from datetime import timedelta
>>> now = date.today()
>>> one_day = timedelta(days=1)
>>> tomorrow = now + one_day
>>> tomorrow

datetime.date(2021, 3, 2)

>>> now + 17*one_day
datetime.date(2021, 3, 18)

>>> yesterday = now - one_day
>>> yesterday
datetime.date(2021, 2, 28)
```

#### 使用time

```python

```

