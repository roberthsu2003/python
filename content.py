total = 0
i = 2
count = 0
while i <= 10:
  count += 1
  total += i
  #print("第",count,"次迴圈的i=", i,"總和為", total)
  #舊的方法
  #print("第%d次迴圈的i=%i總和為%i" % (count, i, total))

  #新的方法
  print("第{:d}次迴圈的i={:d}總和為{:.2f}".format(count, i, total))

  
  i += 2
print('程式結束')

