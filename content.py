• 如果x不是負數，則傳回值為 x ** (1 / y)。
• 如果x是負數而且為偶數，則傳回值為"虛數"。
• 如果x是負數而且為奇數，則傳回值為 -(-x) ** (1 / y)。

x = int(input('請輸入x:'))
if x >= 0:
  root = x ** (1 / y)
else:
  if x % 2 == 0:
    root = "虛數"
  else:
    root = -(-x) ** (1 / y)

print(root)
