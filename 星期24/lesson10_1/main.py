import tools

def main():
    print(f"PI的內容是{tools.PI}")
    print(f"3+4={tools.add(3,4)}")
    stu1 = tools.getStudent()
    print(stu1.name)
    print(stu1.sum())

if __name__ == "__main__":
    main()