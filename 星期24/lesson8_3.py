#文件是一個命名空間
def fun1():
    #function也是一個命名空間
    print("我是fun1")
    print(f"我的名字是{fun1.__name__}")

def fun2():
    # function也是一個命名空間
    print("我是fun2")
    print(f"我的名字是{fun2.__name__}")


def main():
    print("我是主程式")
    fun1()
    fun2()

if __name__ == "__main__":
    main()