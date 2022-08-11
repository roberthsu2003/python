#小王班上有五位學生，請您為小王設計一個輸入成績的程式，並且在輸入成績後顯示班上總成績及平均成績
total = 0
for i in range(1,6):
  value = eval(input(f"請輸入第{i}位學生的成績:"))
  total += value

print(f"五位學生的總分為:{total},平均為{total/5:.2f}")

