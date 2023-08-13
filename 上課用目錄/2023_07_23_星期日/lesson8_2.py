#!/usr/local/bin/python3.10
'''
整個py文件的說明
'''

def check_prime(start: int, end: int)-> None:
    '''
    function的說明,check_prime是例印一個數值間的質數
    '''
    for i in range(start, end+1):
        is_prime = True
        if i == 1:
            continue
        for j in range(2,i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=' ')
    return None
    print("程式結束") #不會執行

help(check_prime)