from threading import Thread
import time

class CountdownThread(Thread):
    def __init__(self,n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            print('倒數計時:',self.n)
            self.n -= 1;
            time.sleep(1)

c=CountdownThread(5)
c.start()
c.join()
print("次執行緒結束")