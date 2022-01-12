import tools
def another1():
    pass

if __name__ == "__main__":
    print(another1.__name__)
    print(tools.__name__)
    print(tools.toos_list)
    print(tools.add(10, 20))
    print(tools.Bicycle.add(5,10))
    bike = tools.get_bicycle()
    print(bike.__class__)
    bike.sayHello()