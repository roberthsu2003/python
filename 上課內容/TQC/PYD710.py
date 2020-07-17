'''
1. 題目說明:
請開啟PYD710.py檔案，依下列題意進行作答，為一詞典輸入資料並進行搜尋，使輸出值符合題意要求。作答完成請另存新檔為PYA710.py再進行評分。

2. 設計說明：
請撰寫一程式，為一詞典輸入資料（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），再輸入一鍵值並檢視此鍵值是否存在於該詞典中。

3. 輸入輸出：
輸入說明
先輸入一個詞典，直至end結束輸入，再輸入一個鍵值進行搜尋是否存在

輸出說明
鍵值是否存在詞典中

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
Key: 123-4567-89
Value: Jennifer
Key: 987-6543-21
Value: Tommy
Key: 246-8246-82
Value: Kay
Key: end
Search key: 246-8246-82
True
'''

my_dict = {}

while True:
    key = input("Key: ")
    if key == "end":
        break

    value = input("Value: ")
    my_dict[key] = value

search_key = input("Search key: ")
print(search_key in my_dict)

