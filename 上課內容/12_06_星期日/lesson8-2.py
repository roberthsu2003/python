#! usr/bin/python3.x
'''
這個py是教學用的
'''

def outputGloble():
    a = 20
    print("func內的a",a)
    print("func外的b",b)

if __name__ == "__main__":
    a = 5
    b = 10
    outputGloble()
    print("func外的a", a)