#!usr/bin/python3.8
'''
#Name        : sequential1.py
#百貨公司舉辦週年抽獎活動，將顧客的抽獎編號及姓名分別儲存於陣列中，使用者輸入編號，程式會搜尋出該編號的姓名並顯示。若查詢不到也會顯示無此編號的訊息

#============================================================

請輸入中獎者的編號943
中獎者的姓名為:stu3

#============================================================
'''

if __name__ == '__main__':
    nums = (256, 731, 943, 389, 142, 645, 829, 945, 371, 418)
    names = ("stu1", "stu2", "stu3", "stu4", "stu5", "stu6", "stu7", "stu8", "stu9", "stu10")
    data = {}
    for item in zip(nums, names):
        data[item[0]] = item[1]

    #comprehension:
    #data = {item[0]:item[1] for item in zip(nums, names)}
    #print(data)

    inputNum = int(input('請輸入中獎者的編號:'))
    if inputNum in data:
        name = data[inputNum]
        print('中獎者的姓名為:', name)
    else:
        print('無此中獎號碼!')