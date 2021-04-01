class Student:
    def __init__(self,name,chinese=0,english=0,math=0):
        self.name = name
        self.chinese = chinese
        self.english = english
        self.math = math

if __name__ == "__main__":
    stu1 = Student("robert")
    stu2 = Student("robert",math=60)
    stu3 = Student("robert", math=60,chinese=70)
    stu3 = Student("robert", math=60, chinese=70,english=89)