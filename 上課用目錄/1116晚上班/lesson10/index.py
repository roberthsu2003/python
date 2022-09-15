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

def main():
    s1 = Student(n="jone",chinese=85)
    s2 = Student(n="peter",age=21,english=92)

    s1.description()
    print("總分",s1.sum)
    print("=============")
    s2.description()
    print("總分",s2.sum)


if __name__ == "__main__":
    main()