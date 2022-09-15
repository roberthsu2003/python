class Person():
    def __init__(self,n,age=18):
        self.name = n
        self.age = age
        
    
    def description(self):
        print(f"我的名字是{self.name}")
        print(f"我的age是{self.age}")

class Student(Person):
    def __init__(self,n,age=18,chinese=60,english=60):
        super().__init__(n,age)
        self.job="student"
        self.chinese = chinese
        self.english = english

    def description(self):
        super().description()
        print(f"我的職業是{self.job}")
        print(f"我的國文是{self.chinese}")
        print(f"我的英文是{self.english}")

    @property
    def sum(self):
        return self.chinese + self.english