#!usr/bin/python3

"""
#taiwanId.py
#r'^[A-Z]\d{9}$'
#驗證身份證字號
請輸入身份證字號:A12345678
A12345678有誤

請輸入身份證字號:A123456789
A123456789正確
"""
import re

taiwanId = input('請輸入身份證字號:')
mobj = re.match(r'^[A-Z]\d{9}$',taiwanId,re.I)
if(mobj):
    print(taiwanId,"正確")
else:
    print(taiwanId, "有誤")


