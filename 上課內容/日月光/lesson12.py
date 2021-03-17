import random
students = list()
for _ in range(50):
    scores = {}
    subjects = ["國文","英文","數學","社會","自然"]
    for subject in subjects:
        scores[subject] = random.randint(50,100)
    students.append(scores)

print(students)