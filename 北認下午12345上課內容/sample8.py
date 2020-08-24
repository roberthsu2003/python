import re
s = "Playing 4 hours a day"
obj = re.sub(r"^.*$","Working",s)
print(obj)

s1 = '768 Working 2343 789 five 234 656 hours 324 4646 a 345 day'
obj1 = re.sub(r'\d', "", s1)

print(obj1)

obj2 = re.sub(r'\s', "", obj1)
print(obj2)