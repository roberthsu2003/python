#!usr/bin/python3
'''
計算固定中的支出，媽媽每天會將家裡的花費記錄下來，並且計算本週的花費總和

顯示:
請輸入星期1 的支出567
請輸入星期2 的支出456
請輸入星期3 的支出567
請輸入星期4 的支出890
請輸入星期5 的支出345
請輸入星期6 的支出534
請輸入星期日 的支出678
本星期的支出為:4037元
'''
sum=0;
i=1;
while (True):
    if (i<7):
        output='請輸入星期'+str(i)+'的花費:'
        n=int(input(output))
    elif(i==7):
        n=int(input("請輸入星期日的花費:"))
    sum += n
    i += 1
print(f'本星期的支出為{sum}元')

