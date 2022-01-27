import random
students = []
for i in range(50):
  scores = []
  for j in range(5):
    scores.append(random.randint(50,100))
  students.append(scores)

students
