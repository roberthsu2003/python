#!usr/bin/python3

'''
請使用者輸入一個任意數，程式會顯示此數的平方值及立方值
'''

num = float(input('請輸入任意數:'))
result = num ** 2
print('此數的平方是:',result)
result = num ** 3
print('此數的立方是:',result)