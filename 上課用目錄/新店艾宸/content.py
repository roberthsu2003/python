#小明想要存錢買一輛機車,機車每輛30000元，他將每月存的錢輸入，當存款足夠買機車時，就顯示提示訊息告知。

deposit = 0
num = 0
while(deposit<30000):
  num += 1
  inputNum = int(input(f"請輸入第{num}個月份的存款:"))
  deposit += inputNum
print(f"恭喜!已經存夠了,存了{num}個月,總存款為:{deposit}")
