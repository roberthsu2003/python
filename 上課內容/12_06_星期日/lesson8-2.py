#! usr/bin/python3.x
'''
這個py是教學用的
'''

def outputGloble():
    global a;
    a = 20
    print("func內的a的id",id(a))
    print("func外的b的id是",id(b))

if __name__ == "__main__":
    a = 5
    b = 10
    outputGloble()
    print("func外的a的id", id(a))
    print("func外的b的id是",id(b))