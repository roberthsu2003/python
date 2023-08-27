import random
def __get_all_names() -> list[str]:
    with open('names.txt',mode='r',encoding='utf-8') as file:
        names:list[str] = []
        for line in file:
            #names.append(line)
            line = line.rstrip('\n')
            names.append(line)
        return names
    
def __get_random_names(nums:int) -> list[str]:
    names = __get_all_names()
    random_list = random.choices(names,k=nums)
    return random_list

def get_students(student_num:int) -> list[list]:    
    students:list[list] = [] #建立第一維list
    names = __get_random_names(nums=student_num)
    for i in range(student_num):
        one_student = [random.randint(50, 100) for _ in range(5)] #建立第2維list
        name = names[i]
        one_student = [name] + one_student
        students.append(one_student)
    return students