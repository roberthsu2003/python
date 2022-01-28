datas = {1: '張三', 2: '李四', 3: '王五'}
num = int(input('請輸入座號: '))
if not num in datas:
  print('該座號不存在！')
else:
  print("學生姓名為： " + datas[num])
