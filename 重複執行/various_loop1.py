#!usr/bin/python3
'''
#various_loop1.py

以for迴圈計算1到100的和
顯示=================
1+2+3+~+100的總合是5050
'''
sum = 0
for i in range(100):
    i += 1
    if(i != 100):
        print(i,"+", end='')
        sum += i
        continue
    print(i," = ", end='')
    sum += i

print(sum)
