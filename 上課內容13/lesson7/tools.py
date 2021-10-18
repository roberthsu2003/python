def get_hello(name):
    print(f'hello!{name}');

def getPerson(userName):
    p1 = Person(name=userName)
    return p1

class Person():
    def __init__(self,name):
        self.name=name