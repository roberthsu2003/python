#!usr/bin/python3
'''
請以(複合指定運算子)設計程式,讓用者輸入三個任意數，程式會顯示3數相加的總和(float)
'''
sum = 0
x = float(input('請輸入第一個數:'))
sum += x
x = float(input('請輸入第二個數:'))
sum += x
x = float(input('請輸入第三個數:'))
sum += x
print('三個數的總和為:',sum)