import random

min = 1
max = 100
target = random.randint(min, max)

print("============猜數字遊戲==============")

while(True):
  keyin = int(input(f"猜數字範圍{min}~{max}:"))
  if(keyin >= min and keyin <= max):
    print("在範圍內")
  else:
    print("請輸入提示範圍內的數字")
    continue
  
  break

print("程式結束")
