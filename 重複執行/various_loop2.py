#!usr/bin/python3

'''
*問題 various_loop2.py
以while迴圈計算1到100的和

顯示============
1+2+3+~+100的總合是5050
'''

sum = 0
i = 1
while(i <= 100):

    if(i != 100):
        print(i,"+",end='')
    else:
        print(i,"=",end='')

    sum += i
    i += 1
print("的總合是",sum)