#! /usr/bin/python3

'''
#Name: callByReference.py
#callByReference
'''

def turbo(speed):
    print(id(speed))
    print('加速前速度:',speed[0])
    speed[0] += 10

if __name__ == '__main__':
    speed = list()
    print(id(speed))
    startSpeed = int(input('請輸入初始速度:'))
    speed.append(startSpeed)
    turbo(speed)
    print('加速後的速度:',speed[0])

