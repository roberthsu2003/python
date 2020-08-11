'''
1. 題目說明:
請開啟PYD708.py檔案，依下列題意進行作答，進行兩詞典合併，使輸出值符合題意要求。作答完成請另存新檔為PYA708.py再進行評分。

2. 設計說明：
請撰寫一程式，自行輸入兩個詞典（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），將此兩詞典合併，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值。

3. 輸入輸出：
輸入說明
輸入兩個詞典，直至end結束輸入

輸出說明
合併兩詞典，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
Create dict1:
Key: a
Value: apple
Key: b
Value: banana
Key: d
Value: durian
Key: end
Create dict2:
Key: c
Value: cat
Key: e
Value: elephant
Key: end
a: apple
b: banana
c: cat
d: durian
e: elephant
'''
def compute():
    dic = {}
    while True:
        key = input("Key:")
        if key == "end":
            return dic
        value = input("Value: ")
        dic[key] = value
        

print("Create dict1")
dict1 = compute()

print("Create dict2")
dict2 = compute()

merge_dict = dict1.copy()
merge_dict.update(dict2)

sortedDict = sorted(merge_dict)

for i in sortedDict:
    print("%s: %s" % (i, merge_dict[i]))
