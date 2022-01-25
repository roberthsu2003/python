score = int(input("請輸入分數"))
if score >= 90:
  grade = '優'
elif score >= 80:
  grade = '甲'
elif score >= 70:
  grade = '乙'
elif score >= 60:
  grade = '丙'
else:
  grade = '丁'

print("成績等級為",grade) 
