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

    cursor.execute("INSERT INTO awesome(日期,num1,num2,num3,num4,num5,num6,特別號) VALUES (?,?,?,?,?,?,?,?)",(date,sixList[0],sixList[1],sixList[2],sixList[3],sixList[4],sixList[5],oneItem))

    conn.commit()
    conn.close()
    print("insert 成功")


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
    insertOneRowToSqlite("20170401",six,one)


