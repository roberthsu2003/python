class Student:
    def __init__(self,name,chinese=0,english=0,math=0):
        self.name = name
        self.__chinese = chinese
        self.__english = english
        self.__math = math

    @property
    def math(self):
        return self.__math

    @math.setter
    def math(self, value):
        if value > 100:
            self.__math = 100
        elif value < 0:
            self.__math = 0
        else:
            self.__math = value

    @property
    def english(self):
        return self.__english

    @english.setter
    def english(self, value):
        if value > 100:
            self.__english = 100
        elif value < 0:
            self.__english = 0
        else:
            self.__english = value

    @property
    def chinese(self):
        return self.__chinese

    @chinese.setter
    def chinese(self,value):
        if value > 100:
            self.__chinese = 100
        elif value < 0:
            self.__chinese = 0
        else:
            self.__chinese = value

    @property
    def sum(self):
        return self.chinese+self.english+self.math

    @property
    def average(self):
        return self.sum / 3

if __name__ == "__main__":
    stu1 = Student("robert")
    stu2 = Student("robert",math=60)
    stu3 = Student("robert", math=60,chinese=70)
    stu3 = Student("robert", math=60, chinese=70,english=89)