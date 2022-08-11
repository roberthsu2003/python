#請設計一個程式，讓使用者輸入數值，只有加總正偶數值，不加總正奇數值，如果輸入負數，結束程式。
total = 0
while True:
  value = eval(input("請輸入數值:"))
  if value < 0:
    break
  elif value % 2 == 1:
    continue
  else:
    total += value

print(f"total={total}")

