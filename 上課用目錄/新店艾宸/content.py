import random

def generate_scores() -> list:
  scores = []
  for i in range(5):
    scores.append(random.randint(50, 100))
  return scores

students = []
for i in range(50):
  students.append(generate_scores())

students
