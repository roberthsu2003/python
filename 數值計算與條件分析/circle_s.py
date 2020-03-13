#!usr/bin/python3
'''
讓使用者輸入梯形的上底、下底及高，程式會計算梯形的面積(上底加下底乘以高除以2)
'''

PI = 3.14159
radius = float(input('請輸入圓柱體的半徑(公分):'))
height = float(input('請輸入圓柱體的高(公分):'))
area = radius ** 2 * PI * height
print('圓柱體的體積:',area,'立方公分')