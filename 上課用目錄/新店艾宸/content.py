import random
def generate_scores() -> dict:
  scores = {}
  scores['chinese'] = random.randint(50,100)
  scores['english'] = random.randint(50,100)
  scores['math'] = random.randint(50,100)
  scores['history'] = random.randint(50,100)
  scores['discover'] = random.randint(50,100)
  return scores

generate_scores()




students = []
for _ in range(50):
  students.append(generate_scores())

for student in students:
  print(f"國文:{student['chinese']}")
  print(f"英文:{student['english']}")
  print(f"數學:{student['math']}")
  print(f"歷史:{student['history']}")
  print(f"創造:{student['discover']}")
  print("==========================")
