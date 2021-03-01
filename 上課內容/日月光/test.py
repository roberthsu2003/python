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