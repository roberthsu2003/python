from threading import Timer

def countDown(n):
    if n > 0:
        print("倒數計時:",n)
        t = Timer(1,countDown,args=(n-1,))
        t.start()

countDown(10)
