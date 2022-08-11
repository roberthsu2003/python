#小明想要存錢買一輛機車,機車每輛30000元，他將每月存的錢輸入，當存款足夠買機車時，就顯示提示訊息告知。
#不明確執行幾次

deposit = 0
while deposit < 30000:
  value = eval(input("請輸入本月將存款的金額:"))
  deposit += value
print(f"您的總存款為{deposit},已經足夠買機車了。")
