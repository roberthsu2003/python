import random

def allNames() -> list:
    names_list = []
    with open("names.txt",encoding="utf-8") as file:    
        for line in file:
            names_list.append(line[:3])
    return names_list

print("=====取名字系統========\n\n")

while(True):
    names_list = allNames()
    first_name = input("請輸入您的姓:")
    count = int(input("請輸入您要的筆數:"))
    random_names = random.choices(names_list,k=count)
    for name in random_names:
        print(first_name + name[-2:])
    
    again = input("您還要繼續嗎?(y,n)")
    if again.lower() == "n":
        break

print("系統結束")
    
