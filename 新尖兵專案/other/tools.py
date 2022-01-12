toos_list = list(range(11))

def add(a,b):
    return a + b

def get_bicycle():
    return Bicycle()

class Bicycle():
    def sayHello(self):
        print("Hello!")

    @staticmethod
    def add(a,b):
        return a+b