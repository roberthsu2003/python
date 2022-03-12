from bmi import BMI

if __name__ == "__main__":
    one = BMI(name="robert",height=178,weight=79)
    print(f"{one.name}的bmi是{one.bmi()}")

    two = BMI(name="jenny", height=170, weight=65)
    print(f"{two.name}的bmi是{two.bmi()}")

    three = BMI(name="alice", height=160, weight=54)
    print(f"{three.name}的bmi是{three.bmi()}")