#!usr/bin/python3.8

'''
#問題 sale_s.py
#小英是百貨公司結帳員,請您為她設計一個程式，先輸入客戶購買的貨品件數，再依此件數宣告陣列來儲存貨品價格，最後計算全部貨品總價

顯示=======
請輸入購買貨品件數:4
請輸入第1件貨品的價格:xxx
請輸入第2件貨品的價格:xxx
請輸入第3件貨品的價格:xxx
請輸入第4件貨品的價格:xxx
全部貨品總價為:xxxxx元

'''

if __name__ == '__main__':
    nums = int(input("請輸入購買貨品件數:"))
    products = list()
    num = 1
    sum = 0
    while(num <= nums):
        score = int(input("請輸入第{:d}件貨品的價格".format(num)))
        products.append(score)
        sum += score
        num += 1

    print("全部貨品總價為:{:d}元".format(sum))