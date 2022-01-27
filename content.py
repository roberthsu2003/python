#list
#for in
#索引編號取出值
#可以改內容的串列
list_num = [10,20,30,40,50,60]
for num in list_num:
  print(num)
print(list_num[0])
print(list_num[:3])
print(list_num[-3:])
list_num[0] = 100
list_num[1] = 200
print(list_num)
