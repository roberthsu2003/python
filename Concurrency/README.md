# Concurrency
- 執行緒
- 次程序

## 啟動和結束執行緒

- 建立執行緒必需要執行start()才會啟動
- 執行緒的執行完全由作業係統管理

```python
import time
#建立一個執行緒要執行的function
def countdown(n):
    while n > 0:
        print('倒數計時:',n)
        n -= 1
        time.sleep(5)


#建立和啟動執行緒
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()

輸出結果:=============
倒數計時: 10
倒數計時: 9
倒數計時: 8
倒數計時: 7
倒數計時: 6
倒數計時: 5
倒數計時: 4
倒數計時: 3
倒數計時: 2
倒數計時: 1
```

### is_alive()檢查執行緒是否還在執行

```python
import time
#建立一個執行緒要執行的function
def countdown(n):
    while n > 0:
        print('倒數計時:',n)
        n -= 1
        time.sleep(5)


#建立和啟動執行緒
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()

#由主執行緒執行以下程式碼, 並使用is_alive()檢查是否次執行緒還在執行
while t.is_alive():
    print('still running')
    time.sleep(1)
else:
    print('Completed')
    
    
輸出結果:================
倒數計時: 2
still running
still running
still running
still running
still running
倒數計時: 1
still running
still running
still running
still running
still running
Completed
```

### 使用join()等待執行緒結束

```python
import time
#建立一個執行緒要執行的function
def countdown(n):
    while n > 0:
        print('倒數計時:',n)
        n -= 1
        time.sleep(1)


#建立和啟動執行緒
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()

#由主執行緒執行以下程式碼, 使用join()的方法等待執行緒結束後才執行以下程式碼
t.join()
print("執行緒執行完畢")

輸出結果:================
倒數計時: 10
倒數計時: 9
倒數計時: 8
倒數計時: 7
倒數計時: 6
倒數計時: 5
倒數計時: 4
倒數計時: 3
倒數計時: 2
倒數計時: 1
執行緒執行完畢
```

### 做用引數名稱daemon=True建立長時間執行的執行緒(背景執行)
- 背景執行的執行緒不能使用join()方法
- 背景執行緒要等到主執行緒結束後才會使用中斷執行

```python
t = Thread(target=countdown, args=(10,), daemon=True)
t.start()
```

### 手動中斷執行緒執行的執行

```python
import time
from threading import Thread
class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('倒數計時:', n)
            n -= 1
            time.sleep(1)

c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
time.sleep(5)
c.terminate()
t.join()
print("執行緒被手動中斷")

輸出結果:=================
倒數計時: 10
倒數計時: 9
倒數計時: 8
倒數計時: 7
倒數計時: 6
執行緒被手動中斷
```

## GIL(global interpreter lock)

- processing (進程)
- threading (線程)

```
由於pytnon有GIL的保護，python限制我們同時只能使用一個threading，所以就算我們在主程式中建立一個主程式(main processing)，使用8個threading也只能使用到一個核心的CPU，所以threading不要執行太過於繁重的工作，比較適合做I/O和等待資料庫回應的動作。

如果我們有許多的工作要分給多個 CPU 核心做運算，最簡單的方式就是使用佇列(Queue)的方式，讓多個 CPU 可從佇列中取得尚未處理的工作來處理
```

## 建立繼承Thread的自訂類別

```python
from threading import Thread
import time

class CountdownThread(Thread):
    def __init__(self,n):
        super().__init__()
        self.n = n

    #run是overwrite
    def run(self):
        while self.n > 0:
            print('倒數計時:',self.n)
            self.n -= 1
            time.sleep(1)

c = CountdownThread(5)
c.start()
c.join()

輸出結果:==================
倒數計時: 5
倒數計時: 4
倒數計時: 3
倒數計時: 2
倒數計時: 1
執行緒結束執行
```

## 善用threading.Timer

```python
from threading import Timer

def countDown(n):
    if n > 0:
        print('倒數計時:', n)
        t = Timer(1, countDown,args=(n-1,))
        t.start()
countDown(10)

輸出結果:==============
倒數計時: 10
倒數計時: 9
倒數計時: 8
倒數計時: 7
倒數計時: 6
倒數計時: 5
倒數計時: 4
倒數計時: 3
倒數計時: 2
倒數計時: 1
```