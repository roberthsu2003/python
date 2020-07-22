#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:24:53 2020

@author: roberthsu2003
"""

money = int(input('請輸入購買金額:'))
if money >= 100000:
    payMoney = money * 0.8
elif money >= 50000:
    payMoney = money * 0.85
elif money >= 30000:
    payMoney = money * 0.9
elif money >= 10000:
    payMoney = money * 0.95
else:
    payMoney = money * 1.0

print("實付金額是:%.2f元" % payMoney)