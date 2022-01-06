#!usr/bin/python3.9
import random as rd

def getAwesome():
    awesomeNum = set()
    while len(awesomeNum) < 7:
        awesomeNum.add(rd.randint(1,49))
    awesomeList = sorted(awesomeNum)
    specialNum = awesomeList.pop(rd.randint(0,6))
    return (awesomeList,specialNum)


if __name__ == "__main__":
    # 大樂透
    # 1~49,6號碼+特別號
    whichSet = int(input("大樂透電腦選號(組數):"))
    print("大樂透電腦選號:")
    for i in range(whichSet):
        six, one = getAwesome()
        print(f"第{i + 1}組")
        for num in six:
            print(num, end=' ')
        print(f"特別號:{one}")
        print()