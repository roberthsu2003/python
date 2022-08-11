#使用while迴圈建立明確知道執行的次數
total = 0
nums = 1
while nums <=5:
  value = eval(input(f"請輸入第{nums}位學生的成績:"))
  total += value
  nums += 1
print(f"五位學生的總分為:{total},平均為{total/5:.2f}")
