#!usr/bin/python3.8
'''
#Name        : return1.py
#自鍵盤輸入一個數字n,顯示1...n。
#=============================

請輸入數字 n:10
1 2 3 4 5 6 7 8 9 10

#===============================
'''

def showNum(n):
    i = 1;
    while(True):
        if(i > n):
            return()

        print(i,end=' ')
        i += 1

if __name__ == '__main__':
    inputNum = int(input('請輸入數字 n:'))
    showNum(inputNum);
    print()