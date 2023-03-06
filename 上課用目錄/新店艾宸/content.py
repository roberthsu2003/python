#請設計一個程式，讓使用者輸入數值，只有加總正偶數值，不加總正奇數值，如果輸入負數，結束程式。

sum = 0
while(True):
  inputNum = eval(input("請輸入數值:"))
  if(inputNum < 0):
    break
  elif(inputNum % 2 == 1):
    continue
  else:
    sum += inputNum

print(f"所有輸入的正偶數的加總是:{sum}")
