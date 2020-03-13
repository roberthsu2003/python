#! /usr/bin/python3
'''
# Name        : callByValue1.py
#callByValue
'''

def turbo(speed):
    print('加速前速度:',speed)
    speed += 10
    return speed

if __name__ == '__main__':
    speed = int(input('請輸入初始速度:'))
    speed = turbo(speed)
    print('加速後的速度:',speed)

