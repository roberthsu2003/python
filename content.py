import random
students = []
for i in range(50):
  scores = []
  for j in range(5):
    scores.append(random.randint(50,100))
  students.append(scores)

for student in students:
  print(student,end=',')
  total = 0
  for num in student:
    total += num
  
  print(total,end=',')
  print(total/5.0,end='\n')
