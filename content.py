numbers = [10, 20, 30, 40]
print(numbers)
numbers.append(50)
print(numbers)
numbers.extend([60, 70])
print(numbers)
numbers += [80, 90]
print(numbers)
numbers.insert(1,15)
print(numbers)





numbers = [10, 15, 20, 30, 40, 50, 60, 70, 80, 90]

#刪除
del numbers[1]
print(numbers)

#pop
numbers.pop()
print(numbers)
numbers.pop(0)
print(numbers)
