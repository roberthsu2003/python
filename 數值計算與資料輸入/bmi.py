#!usr/bin/python3
'''
請依據 BMI 值分析他人的身體狀況。
BMI值	< 18.5	18.5-25	25-30	>30
身體狀態	 太輕	 正常	過重 	肥胖
'''

height = float(input('請輸入身高,單位為公分:'))
weight = float(input('請輸入體重,單位為公斤:'))
bmi = weight / ((height/100) ** 2)

if bmi < 18.5:
    state = '太輕'
elif bmi <= 25:
    state = '正常'
elif bmi <= 30:
    state = '過重'
else:
    state = '肥胖'

print('您的BMI是',bmi)
print('「您的體重',state,'」')
