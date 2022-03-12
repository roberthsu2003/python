class BMI():
    def __init__(self,name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / (self.height / 100) ** 2

class Person():
    pass

