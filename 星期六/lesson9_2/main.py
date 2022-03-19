from tools import Student

if __name__ == "__main__":
    print("小專案lesson9_2")
    if Student.OK:
        print(Student.get_week())

    stu1 = Student("robert",chinese=89,math=95,english=78)
    print(stu1)
    print(f"stu1學生的姓名{stu1.name}")
    print(f"stu1國文分數:{stu1.chinese}")
    print(f"stu1英文分數:{stu1.english}")
    print(f"stu1數學分數:{stu1.math}")
    print(f"stu1的總分是:{stu1.sum()}")
    print("stu1的平均是{:.2f}".format(stu1.average()))



