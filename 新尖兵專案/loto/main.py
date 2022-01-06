#!usr/bin/python3.9
import random as rd
import sqlite3

def getAwesome():
    awesomeNum = set()
    while len(awesomeNum) < 7:
        awesomeNum.add(rd.randint(1,49))
    awesomeList = sorted(awesomeNum)
    specialNum = awesomeList.pop(rd.randint(0,6))
    return (awesomeList,specialNum)

def insertOneRowToSqlite(date,sixList,oneItem):
    conn = sqlite3.connect('loto.db')
    cursor = conn.cursor()
    sqlString = "INSERT INTO awesome (日期,num1,num2,num3,num4,num5,num6,特別號) VALUES ('20170301',2, 25, 26, 36, 38, 47,24)"
    print(date)
    print(sixList)
    print(oneItem)


if __name__ == "__main__":
    # 大樂透
    # 1~49,6號碼+特別號
    '''
    whichSet = int(input("大樂透電腦選號(組數):"))
    print("大樂透電腦選號:")
    for i in range(whichSet):
        six, one = getAwesome()
        print(f"第{i + 1}組")
        for num in six:
            print(num, end=' ')
        print(f"特別號:{one}")
        print()
    '''
    six, one = getAwesome()
    insertOneRowToSqlite("20170301",six,one)


