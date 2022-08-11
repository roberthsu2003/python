##小美是一位教師，請你以while迴圈方式為小美設計一個輸入成績的程式，如果輸入負數表示成績輸入結束，在輸入成績結束後顯示班上總成績及平均成績。
score = 0
nums = 0
total = 0
while score >= 0:  
  score=eval(input(f"請輸入第{nums+1}學生的分數:"))
  if score >= 0:
    nums += 1
    total += score

print(f"學生的數量是{nums},總分是{total},平均是{total/nums:.2f}")
