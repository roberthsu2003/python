import random
min = 1
max = 20
count = 0
target = random.randint(min,max)
print("==========猜數字遊戲================:\n\n")

while(True):
  count += 1
  keyin =int(input("猜數字範圍{0}~{1}:".format(min,max)))
  if(keyin == target):
    print(f"賓果!猜對了, 答案是:{keyin}")
    print(f"您猜了{count}次")
    break
  elif(keyin > target):
    print("再小一點")
  elif(keyin < target):
    print("再大一點")
print("Game Over")
