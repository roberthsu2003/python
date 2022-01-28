#list的方法index()
cities =  ['台北', '台中', '高雄', '台南', '花蓮']
cities.index('台中')
element = '台南'
if element in cities:
  print(f'{element}的索引編號是{cities.index(element)}')
else:
  print(element)
