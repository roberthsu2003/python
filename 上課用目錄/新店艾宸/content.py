picnicItems = {"sandwiches":4, 'apple':12, 'cups':4, 'cookies':34}
print("PICNIC ITEMS".center(17,'-'))
for k,v in picnicItems.items():
  print(k.ljust(12,'.') + str(v).rjust(5))
