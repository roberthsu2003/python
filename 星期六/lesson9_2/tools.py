from random import choice
print("tools module")
print(f"module的名稱是{__name__}")

OK = True

def get_week():
    return choice(['星期1', '星期2', '星期3', '星期4', '星期5', '星期6', '星期日'])

class Student():
    def __init__(self,name,chinese,english,math):
        self.name = name
        self.chinese = chinese
        self.english = english
        self.math = math
