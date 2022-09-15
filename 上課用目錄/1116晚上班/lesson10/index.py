from data import Student,Person
        

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