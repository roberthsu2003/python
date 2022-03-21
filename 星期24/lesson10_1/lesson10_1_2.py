import tools

if __name__ == "__main__":
    if tools.OK:
        print(tools.getWeek())
        stu1 = tools.Student()
        print(stu1.__class__)