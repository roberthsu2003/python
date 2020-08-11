data = []
with open('read.txt','r') as file:
    for line in file:
        print(line)

        tmp = line.strip('\n').split(' ')
        tmp = [tmp[0], eval(tmp[1]), eval(tmp[2])]
        data.append(tmp)

name = [data[x][0] for x in range(len(data))]
height = [data[x][1] for x in range(len(data))]
weight = [data[x][2] for x in range(len(data))]

print("Average height: %.2f" % (sum(height)/ len(height)))
print("Average weight: %.2f" % (sum(weight)/ len(weight)))

max_h = max(height)
max_w = max(weight)
print("The tallest is %s with %.2fcm" % (name[height.index(max_h)], max_h))

print("The heaviest is %s with %.2fkg" % (name[weight.index(max_w)], max_w))