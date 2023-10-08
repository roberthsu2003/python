import random
import pyinputplus as pyip
import csv

def generate_stu()->list[int]:
    scores = []
    for _ in range(5):
        scores.append(random.randint(50,100))
    return scores

def getNames(num:int) -> list[str]:
    with open("names.txt",encoding="utf-8") as file:
        names = []
        for name in file:
            names.append(name.rstrip())
    return random.choices(names,k=num)

def save_csv_file(filename:str, data:list) -> bool:
    try:
        with open(filename,mode='w',encoding="utf-8",newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["姓名","國文","英文","數學","地理","歷史"])
            csv_writer.writerows(data)
    except:
        return False
    else:
        return True
    
num = pyip.inputInt('請輸入學生的人數:',min=5,max=50)
print(num)
names = getNames(num=num) #建立學生姓名的list
students = []
for i in range(num):
    scores =  generate_stu() #建立學生的5個分數
    scores.insert(0,names[i]) #將學生姓名加入至list內
    students.append(scores)

fname = input("請輸入csv儲檔的檔案名稱:")
if save_csv_file(filename=f"{fname}.csv",data=students):
    print("存檔成功")
else:
    print("存檔失敗")

