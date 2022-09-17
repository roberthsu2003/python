class Person():
    def __init__(self,n,a):
        self.name = n
        self.age = a
        print("初始化實體")
    
    def description(self):
        print(f"我的名字叫{self.name}")
        print(f"我的年紀:{self.age}")

class Student(Person):
    def __init__(self,name,age,chinese=60,english=60):
        super().__init__(name,age)
        self.chinese = chinese
        self.english = english

    def description(self):
        super().description()
        print(f"chinese:{self.chinese}")
        print(f"english:{self.english}")
        

    @property
    def sum(self):
        return self.chinese + self.english 

class BMI(Person):
    def __init__(self,name,age,height,weight):
        super().__init__(name,age)
        self.__height = height
        self.__weight = weight

    @property
    def height(self):
        return self.__height

    @property
    def weight(self):
        return self.__weight

    @property
    def bmi(self):
        return self.weight / (self.height/100) ** 2

def main():
    alice = BMI("Alice",age=23,height=169,weight=50)
    print(f"姓名{alice.name}")
    print(f"年紀:{alice.age}")
    print(f"bmi:{alice.bmi}")

if __name__ == "__main__":
    main()