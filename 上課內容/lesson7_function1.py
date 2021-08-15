#!/bin/python3.8

def temperature(value_c):
    return 1.8 * value_c + 32


if __name__ == "__main__":
    runAgain = True
    print(f'攝氏10度轉華氏溫度={temperature(10)}')
    print('-------------------------')
    while(runAgain):
        c = int(input('請輸入攝氏溫度:'))
        result = temperature(c)
        print(f"華氏溫度={result}")
        inputWord=input("程式還要繼續嗎?(輸入N...結束)")
        if inputWord.upper() == 'N':
            runAgain = False
        else:
            runAgain = True
    print("程式結束")