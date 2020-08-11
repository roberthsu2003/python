f = open("read.txt", 'r')
data = f.read()
f.close()

num = data.split(' ')
total = 0
for i in range(0, len(num)):
    total += eval(num[i])
    
print(total)