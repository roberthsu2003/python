#!usr/bin/python3
'''
#range1.py
#小王班上有五位學生，請您為小王設計一個輸入成績的程式，並且在輸入成績後顯示班上總成績及平均成績。

顯示:
請輸入第1位學生的成績:89
請輸入第2位學生的成績:89
請輸入第3位學生的成績:89
請輸入第4位學生的成績:89
請輸入第5位學生的成績:89

全班總成績為: ***分，平均為89分

'''

sum = 0
students = 5
for i in range(students):
    studentScore = int(input('請輸入第'+ str(i+1) +'位學生的成績:'))
    sum += studentScore

print("全班總成績為:" + str(sum) + "分,平均分數為" + str(sum/students) + "分")
