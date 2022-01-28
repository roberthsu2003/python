#set
empty_set = set()
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)

#元素不會重覆
odd_numbers = {1, 1, 1, 3, 3, 3, 5, 5, 5, 7, 7, 7, 9, 9, 9}
print(odd_numbers)

#新增元素add()

odd_numbers.add(11)
print(odd_numbers)

for item in list(odd_numbers):
  print(item)
