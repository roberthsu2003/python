#文件是一個命名空間
def fun1():
    #function也是一個命名空間
    print("我是fun1")
    print(f"我的名字是{fun1.__name__}")
    chinese = 90
    print(f"func1_chinese:{chinese}")

def fun2():
    # function也是一個命名空間
    print("我是fun2")
    print(f"我的名字是{fun2.__name__}")
    chinese = 80
    print(f"fun2_chinese:{chinese}")


def main():
    print("我是主程式")
    fun1()
    fun2()
    print(f"chinese:{chinese}")



if __name__ == "__main__":
    chinese = 100
    print(f"__main__ chinese:{chinese}")
    main()