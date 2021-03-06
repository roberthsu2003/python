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