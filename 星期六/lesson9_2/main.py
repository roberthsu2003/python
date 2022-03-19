import tools
from tools import Student

if __name__ == "__main__":
    print("小專案lesson9_2")
    if tools.OK:
        print(tools.get_week())

    stu1 = Student("robert",chinese=89,math=95,english=78)
    print(stu1)
    print(f"stu1學生的姓名{stu1.name}")
    print(f"stu1國文分數:{stu1.chinese}")
    print(f"stu1英文分數:{stu1.english}")
    print(f"stu1數學分數:{stu1.math}")



