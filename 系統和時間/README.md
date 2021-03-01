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
>>> from datetime import time
>>> noon = time(12, 0, 0)
>>> noon

datetime.time(12, 0)

>>> noon.hour
12
>>> noon.minute
0
>>> noon.second
0
>>> noon.microsecond
0
```

#### 使用datetime

```python
>>> from datetime import datetime
>>> some_day = datetime(2021,1,2,3,4,5,6)
>>> some_day

datetime.datetime(2021, 1, 2, 3, 4, 5, 6)

>>> some_day.isoformat()
'2021-01-02T03:04:05.000006'

```

#### 使用datetime.now()取得現在日期和時間

```python
>>> from datetime import datetime
>>> now = datetime.now()
>>> now
datetime.datetime(2021, 3, 1, 15, 27, 25, 43479)

>>> now.month
3
>>> now.day
1
>>> now.hour
15
>>> now.minute
27
>>> now.second
25
>>> now.microsecond
43479
```

#### 使用combine()整合date和time成為datetime

```python
>>> from datetime import datetime, time, date
>>> noon = time(12)
>>> this_day = date.today()
>>> noon_today = datetime.combine(this_day,noon)
>>> noon_today
datetime.datetime(2021, 3, 1, 12, 0)
```

#### 從datetime取出日期和時間
```
>>> from datetime import datetime
>>> now = datetime.now()
>>> now.date()
datetime.date(2021, 3, 1)

>>> now.time()
datetime.time(15, 36, 37, 427772)
```

### time Module
- python同有datatime和time2種module
- time Module內提供的是function
- time Module內的time()function傳出的時間是從1970/1/1到現在的秒數時間


```python
>>> import time
>>> now = time.time()
>>> now
1614598360.741274
```

#### 使用ctime()轉換timestamp成為字串

```python
>>> time.ctime(now)
'Mon Mar  1 19:32:40 2021'
```

#### 使用localtime(),gmtime()建立struct_time物件

```python
>>> time.localtime(now)
time.struct_time(tm_year=2021, tm_mon=3, tm_mday=1, tm_hour=19, tm_min=32, tm_sec=40, tm_wday=0, tm_yday=60, tm_isdst=0)


#建立UTCtime
>>> time.gmtime(now)
time.struct_time(tm_year=2021, tm_mon=3, tm_mday=1, tm_hour=11, tm_min=32, tm_sec=40, tm_wday=0, tm_yday=60, tm_isdst=0)
```

> ### 注意:儲存時間請使用UTC time,儲存字串請使用UTF-8

### 讀寫日期和時間
#### 可將日期轉為字串

- isoformat()
- time.ctime()
- strftime() ->在datetime,date,time物件中被當作method,在time module初當作function

#### strftime()轉為字串的字串格式

| 字串格式 | Date/time單位 | 範圍 |
|:--|:--|:--|
| %Y | year | 1900-... |
| %m | month | 01-12 |
| %B | month name | January,.. |
| %b | month 縮寫 | Jan,.. |
| %d | day of month | 01-31 |
| %A | weekday name | Sunday,... |
| a | weekday 縮寫 | Sun,... |
| %H | hour(24 hr) | 00-23 |
| %I | hour(12 hr) | 01-12 |
| %p | AM/PM | AM,PM |
| %M | minute | 00-59 |
| %S | second | 00-59 |

#### 使用strftime()將struct_time物件轉成字串

```python
>>> import time
>>> fmt = "現在日期是 %A, %B %d, %Y,時間是 %I:%M:%S%p"
>>> t = time.localtime()
time.struct_time(tm_year=2021, tm_mon=3, tm_mday=1, tm_hour=20, tm_min=6, tm_sec=38, tm_wday=0, tm_yday=60, tm_isdst=0)

>>> time.strftime(fmt,t)
'現在日期是 Monday, March 01, 2021,時間是 08:06:38PM'
```

#### 使用date物件和strftime()method

- #### date物件只轉換date部份

```python
>>> from datetime import date
>>> some_day = date(2018, 7, 4)
>>> fmt = "日期是 %B, %d, %Y,時間是 %I:%M:%S%p"
>>> some_day.strftime(fmt)
'日期是 July, 04, 2018,時間是 12:00:00AM'
```

- #### time物件只轉換time部份

```python
>>> from datetime import time
>>> some_time = time(10, 35)
>>> fmt = "日期是 %B, %d, %Y,時間是 %I:%M:%S%p"
>>> some_time.strftime(fmt)
'日期是 January, 01, 1900,時間是 10:35:00AM'
```

### 使用strptime()將字串轉為date或time物件

```pytnon
#注意字串格式
>>> import time
>>> fmt = "%Y-%m-%d"
>>> time.strptime("2012-01-29", fmt)
time.struct_time(tm_year=2012, tm_mon=1, tm_mday=29, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=29, tm_isdst=-1)
```

### 使用local module

```python
>>> import locale
>>> from datetime import date
>>> halloween = date(2018, 10, 20)
>>> for lang_country in  ['en_us','fr_fr','de_de','es_es','is_is','zh_tw']:
       locale.setlocale(locale.LC_TIME, lang_country)
       print(halloween.strftime('%A, %B, %d'))
       
Saturday, October, 20
Samedi, octobre, 20
Samstag, Oktober, 20
sábado, octubre, 20
laugardagur, október, 20
週六, 10月, 20
```



