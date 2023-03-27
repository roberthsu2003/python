def printPicnic(itemDict, leftWidth, rightWidth):
  print("PICNIC ITEMS".center(leftWidth+rightWidth,'-'))
  for k,v in itemDict.items():
    print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))

picnicItems = {"sandwiches":4, 'apple':12, 'cups':4, 'cookies':34}
printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)
