import random

#自訂的function
def play_game():
    min = 1
    max = 100
    target = random.randint(min,max)
    print(target)
    count = 0
    print("==========猜數字遊戲==========\n\n")
    while True:    
        keyin = int(input(f"猜數字的範圍{min}~{max}:"))
        count += 1
        if keyin >= min and keyin <= max:
            if(keyin == target):
                print(f"賓果!猜對了, 答案是:{keyin}")
                print(f"您總共猜了{count}次")
                break
            elif(keyin > target):            
                print("再小一點")
                max = keyin-1
                
            elif(keyin < target):
                print("再大一點")
                min = keyin + 1
                
            print(f"您已經猜了{count}次")
        else:
            print("超出範圍")

while True:
    play_game()#呼叫function    
    play_again = input("您還要繼續嗎?(y or n):")
    if play_again == 'n':        
        break
    else:
        continue

print("遊戲結束")