dict1 = {
    'a':200,
    'b':300,
    'c':400
}

print(dict1['a'])
print(dict1['b'])
dict1['c'] = 500 #修改
print(dict1['c'])

dict1['d'] = 600 #新增
print(dict1)

del dict1['d'] #刪除
print(dict1)
