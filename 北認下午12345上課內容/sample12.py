import random

lotters = set()
while(len(lotters) < 8):
    lotters.add(random.randint(1,49))

lottersList = list(lotters)
special_Num = lottersList.pop()
print("大樂透電腦選號:")
lottersList.sort(reverse=False)
print(lottersList)
print("特別號:")
print(special_Num)
