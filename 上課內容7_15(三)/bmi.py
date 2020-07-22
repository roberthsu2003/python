#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:20:44 2020

@author: roberthsu2003
"""

height = float(input('請輸入身高,單位為公分:'))
weight = float(input('請輸入體重,單位為公斤:'))
bmi = weight / ((height/100) ** 2)
if bmi < 18.5:
    state = '太輕'
elif 18.5 <= bmi < 25:
    state = '正常'
elif 25 <= bmi < 30:
    state = '過重'
else:
    state = '肥胖'

print('你的BMI是%.2f,您的體重%s' % (bmi, state))

