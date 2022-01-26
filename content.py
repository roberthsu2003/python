sum = 0
num = 00
while(True):
  num += 1
  inputNum = int(input("請輸入第" + str(num) + "個數值:"))
  if(inputNum < 0):
    break
  elif(inputNum % 2 == 1):
    continue
  else:
    sum += inputNum
print(f"所有輸入的正偶數的加總是:{sum}")
