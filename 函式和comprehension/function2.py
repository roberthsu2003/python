#!usr/bin/python3.8
'''
#Name        : function2.py
#輸入攝氏溫度，求華氏溫度
#=============================

攝氏10度轉華氏溫度=50
#==========================
請輸入攝氏溫度:19
華氏溫度=66.2

#===============================

'''
def temperature(value):
    return 1.8 * value + 32



if __name__ == '__main__':
    print('攝氏10度轉華氏溫度=',temperature(10))
    print('------------------')
    value = int(input('請輸入攝氏溫度:'))
    result = temperature(value)
    print('華氏溫度=',result)
