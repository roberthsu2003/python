f_name = input()
n = int(input())
word_dict = dict()

with open(f_name, 'r') as file:
    for line in file:
        word = line.strip('\n').split(' ')

        for x in word:
            if x in word_dict:
                word_dict[x] += 1
            else:
                word_dict[x] = 1
word_list = word_dict.items()
wordQTY = [x for (x, y) in word_list if y==n]

sortedword = sorted(wordQTY)

for x in sortedword:
    print(x)