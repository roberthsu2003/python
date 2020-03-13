#!usr/bin/python3

"""
字串文字接龍
"""
print('失敗就會退出遊戲!')
inputString = input('請輸入一個字串:')
sampleString = 'wordlink'
for single in sampleString:
    print('上一個字串是:',inputString)
    outputWords = "請輸入-",single,"-開始的字串"
    keyin = input(outputWords)
    if keyin[0] != single:
        print('遊戲失敗')
        print('您輸入的字串是:',inputString)
        break
    inputString += '-' + keyin
else:
    print('恭喜!成功完成遊戲')
    print('您輸入的字串是:',inputString)
