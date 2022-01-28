#大樂透電腦選號
import random
lot = set()
while(len(lot)<7):
  lot.add(random.randint(1,49))

for i in list(lot)[:6]:
  print(i,end=' ')
print(f"特別號:{list(lot)[-1]}")
