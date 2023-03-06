#請輸入小寫英文字[按q會離開]:taipei
#Taipei
#請輸入小寫英文字[按q會離開]:q
#程式結束

stuff = input("請輸入小寫英文字[按q會離開]:")
while(stuff != "q"):
  print(stuff.capitalize())
  stuff = input("請輸入小寫英文字[按q會離開]:")

print("程式結束")
