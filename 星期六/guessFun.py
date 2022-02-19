import random
min = 1
max = 10
count = 0
target = random.randint(min, max)
print(target)
print("＝＝＝＝＝＝＝＝＝猜數字遊戲===============:\n\n")
while(True):
   count += 1
   keyin = int(input(f"猜數字範圍{min}~{max}:"))
   if (keyin >= min) and (keyin <= max):
       if keyin == target:
           print(f"賓果!猜對了, 答案是:{target}")
           print(f"您猜了{count}次")
           break;
       else:
           print(f"您已經猜了{count}次")
   else:
       print(f"請輸入提示範圍內的數字{min}~{max}")
print("Game Over")