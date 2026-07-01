#!usr/bin/python3
'''
讓使用者輸入圓柱體的半徑及高，程式會計算圓柱體的體積(圓週率乘以半徑平方再乘以高)
'''

PI = 3.14159
radius = float(input('請輸入圓柱體的半徑(公分):'))
height = float(input('請輸入圓柱體的高(公分):'))
area = radius ** 2 * PI * height
print('圓柱體的體積:',area,'立方公分')