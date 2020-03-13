#!usr/bin/python3.8

'''
#Name        : function3.py
#輸入攝氏溫度，求華氏溫度
#function 的原型宣告
#加上do...while()

#=============================

攝氏10度轉華氏溫度=50
#==========================
請輸入攝氏溫度:20
華氏溫度=68
程式還要繼續嗎?(輸入N....結束):h
請輸入攝氏溫度:40
華氏溫度=104
程式還要繼續嗎?(輸入N....結束):a
請輸入攝氏溫度:10
華氏溫度=50
程式還要繼續嗎?(輸入N....結束):N
程式結束

#===============================

'''

def temperature(value):
    return 1.8 * value + 32



if __name__ == '__main__':
    runAgain = True;
    print('攝氏10度轉華氏溫度=',temperature(10))
    print('------------------')
    while(runAgain):
        value = int(input('請輸入攝氏溫度:'))
        result = temperature(value)
        print('華氏溫度=', result)
        inputValue = input('程式還要繼續嗎?(輸入N...結束):')
        if inputValue == 'N':
            runAgain = False
        else:
            runAgain = True


