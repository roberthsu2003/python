#2個條件時,可以使用巢狀判斷

furry = False
small = True
if furry:
  if small:
    print("它是貓!")
  else:
    print("它是熊!")
else:
  if small:
    print("它是小蜥蜴")
  else:
    print("它是人類或是沒毛的熊")
