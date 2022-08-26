#tools的module
#function
#class
#常數

PI=3.14159

def add(a,b):
    return a + b;

class Student():
    def __init__(self):
        self.name="robert"
        self.chinese = 97
        self.english = 75
        self.math = 92

    def sum(self):
        return self.chinese + self.english + self.math

def getStudent():
    return Student()