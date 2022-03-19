print(f'game.py的moudle的名稱{__name__}')
def guess_num():
    import random
    min = 1
    max = 100
    count = 0
    target = random.randint(min, max)
    print(target)
    while(True):
       count += 1
       keyin = int(input(f"猜數字範圍{min}~{max}:"))
       if (keyin >= min) and (keyin <= max):
           if keyin == target:
               print(f"賓果!猜對了, 答案是:{target}")
               print(f"您猜了{count}次")
               break;
           elif keyin > target:
               max = keyin
               print("再小一點")
           elif keyin < target:
               min = keyin
               print("再大一點")
           print(f"您已經猜了{count}次")

       else:
           print(f"請輸入提示範圍內的數字{min}~{max}")