#keys(),values(),items()
signals = {'綠燈': '走', '黃燈': '走快些', '紅燈': '停等'} 
print(signals.keys())

print(signals.values())

print(signals.items())






#for in取出key和value
for key,value in signals.items():
  print(key,value)
