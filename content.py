num = 0
sum = 0
while(True):
  num += 1
  score = int(input('請輸入第' + str(num) + '位學生的成績:'))
  if(score < 0):
    break
  sum += score

print("全班總成績為:%d,平均分數為:%.2f" % (sum, sum/(num-1)))
