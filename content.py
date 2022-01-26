deposit = 0
num = 0
while(deposit < 30000):
  num += 1
  inputValue = int(input(f"請輸入第{num}月份的存款:"))
  deposit += inputValue

print("恭喜!已經存夠了，存了{:d}月,共存了{:.2f}元".format(num,deposit))
