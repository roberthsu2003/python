import time

def countdown(n):
    print("次執行緒執行中")
    while n > 0:
        print('倒數計時:',n)
        n -= 1
        time.sleep(5)

from threading import Thread
t = Thread(target=countdown,args=(5,))
t.start()
print("主執行緒結束")