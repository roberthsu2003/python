## 迴圈Loop
###  重複執行概念
- 重覆執行可以讓程式中某一區段流程反覆執行
- 重複執行可用 while 及 for 兩種方式設計

### while 迴圈的架構如下:
```python
設定控制迴圈變數的初始值
while 條件分析:
	條件成立下執行迴圈要執行的工作
	調整控制迴圈變數的內容
```

### while 迴圈
- 當 while 迴圈的條件分析成立時，才會進入到迴圈。
- 若 while 迴圈的條件分析不成立，則跳出迴圈。
- 若 while 迴圈內條件分析一開始不成立，則迴圈一次都不執行。

#### while 迴圈:請動手操作，並留意輸出結果
```python
#while1.py


a=6
while a > 0:
	print(a)
	a -= 1 
print("離開後a為",a)

```

#### Question: 請問執行後最後的輸出哪一個是對的?(選擇題)  

```python
a = 15 
while a > 0:
	print(a) 
	a -= 2
```
(1) 0  
(2) 1  
(3) -2  


### 使用while迴圈,重複執行程式區塊
- 有時我們需要做一件事超過一次，這時就需要迴圈程式
- python最簡單的迴圈就是while迴圈,範例如下:

```python
#簡單列印1~5
#這樣的使用等同於c語言的的 for(int count=1;count<=5;count+=1)
#使用時機明確的知道要執行多少次迴圈

>>> count = 1
>>> while count <= 5:
		print(count)
		count += 1 
...
1
2
3
4
5
>>>
```

#### Homework:計算2 - 10所有偶數的總和
```python
#loop1.py
#計算2 - 10所有偶數的總和

第 1.0 次迴圈的i = 2 總和為 2
第 2.0 次迴圈的i = 4 總和為 6
第 3.0 次迴圈的i = 6 總和為 12
第 4.0 次迴圈的i = 8 總和為 20
第 5.0 次迴圈的i = 10 總和為 30
```
[解題](loop1.py)

### Homework:計算固定中的支出，媽媽每天會將家裡的花費記錄下來，並且計算本週的花費總和
```python
Name        : loop2.py
計算固定中的支出，媽媽每天會將家裡的花費記錄下來，並且計算本週的花費總和

顯示:
請輸入星期1 的支出567
請輸入星期2 的支出456
請輸入星期3 的支出567
請輸入星期4 的支出890
請輸入星期5 的支出345
請輸入星期6 的支出534
請輸入星期日 的支出678
本星期的支出為:4037元
```

[解題](loop2.py)


### 使用break跳出迴圈
- 使用無限迴圈+break的語法

```python
#使用時機,不明確知道要執行幾次迴圈
#配合條件式if,並使用break停止迴圈

while(True):
    stuff = input("請輸入小寫英文字[按q會離開]:")
    if stuff == 'q':
        break
    print(stuff.capitalize())
print("程式結束")


結果:=================================
請輸入小寫英文字[按q會離開]:taipei
Taipei
請輸入小寫英文字[按q會離開]:q
程式結束
```

```python
#while1_s.py
#小美是一位教師，請你以while迴圈方式為小美設計一個輸入成績的程式，如果輸入負數表示成績輸入結束，在輸入成績結束後顯示班上總成績及平均成績。

#顯示===============
請輸入第1學生的成績:89
請輸入第2學生的成績:78
請輸入第3學生的成績:68
請輸入第4學生的成績:89
請輸入第5學生的成績:-1
全班總成績為: 324 平均分數為: 64.8
#=========================================


num = 0
sum = 0
while(True):
    num += 1
    score = int(input('請輸入第'+ str(num) +'學生的成績:'))    
    if(score < 0):
        break
    
    sum += score
    
#已經跳出while    
print('全班總成績為:', sum, "平均分數為:", "%.2f" % (sum/(num-1)) )
```


### 使用continue,中止現在迴圈,跳至下一輪迴圈,重頭執行

```python
while True:
	value = input("請輸入整數,輸入[q]離開: ") 
	if value == 'q': # quit
		break
	number = int(value)
	if number % 2 == 0: # 一個偶數值
		continue
	print(number, "平方是", number*number)
		
顯示:
奇數輸出平方
偶數不做任何動作
'q'要離開
==============================		
請輸入整數,輸入[q]離開:3
3的平方是9
請輸入整數,輸入[q]離開:5
5的平方是25
請輸入整數,輸入[q]離開:4
請輸入整數,輸入[q]離開:6
請輸入整數,輸入[q]離開:q
程式結束


```

```python
#continue.py
#請設計一個程式，讓使用者輸入數值，只有加總正偶數值，不加總正奇數值，如果輸入負數，結束程式。

顯示:========================================
請輸入第1個數值:456
請輸入第2個數值:455
請輸入第3個數值:123
請輸入第4個數值:-1
所有輸入的正偶數的加總是:xxxxxxx
=============================================

num = 0
sum = 0
while(True):
    num += 1
    inputNum = int(input("請輸入第"+ str(num) + "個數值:"))
    if(inputNum < 0):
        break
    elif (inputNum % 2 == 1):
        continue
    else:
        sum += inputNum
print("所有輸入的正偶數的加總是:", sum)
```

### 無限定次數的迴圈

```python
#============================================================================
# Name        : while2.py
#小明想要存錢買一輛機車,機車每輛30000元，他將每月存的錢輸入，當存款足夠買機車時，就顯示提示訊息告知。
#============================================================================

顯示:
請輸入第1個月份的存款:4567
請輸入第2個月份的存款:3456
請輸入第3個月份的存款:4567
請輸入第4個月份的存款:4567
請輸入第5個月份的存款:4567
請輸入第6個月份的存款:5678
請輸入第7個月份的存款:7890
恭喜! 已經存夠了，存了7個月的總存款為:35292元。
#============================================================================

deposit = 0
num = 0
while(deposit < 30000):
    num += 1
    inputNum = int(input('請輸入第'+str(num)+"個月份的存款:"))
    deposit += inputNum

print("恭喜!已經存夠了，存了",num,"個月的總存款為:",deposit,"元。")
```

```python
#============================================================================
# Name        : guess.py
#猜數字遊戲

===============猜數字遊戲=================:

猜數字範圍1~100:50
再小一點
您猜了 1 次

猜數字範圍1~50:25
再大一點
您猜了 2 次

猜數字範圍25~50:34
再大一點
您猜了 3 次

猜數字範圍34~50:46
再小一點
您猜了 4 次

猜數字範圍34~46:40
賓果!猜對了, 答案是: 40
您猜了 5 次
#====================================

import random
min = 1
max = 100
count = 0
target = random.randint(1, 100)
print("===============猜數字遊戲=================:\n")
while(True):
    count += 1
    keyin = int(input("猜數字範圍{0}~{1}:".format(min, max)))
    if(keyin >=min and keyin <= max):
        if(keyin == target):
            print("賓果!猜對了, 答案是:", target)
            print("您猜了",count,"次")
            break
        elif (keyin > target):
            max = keyin
            print("再小一點")
        elif (keyin < target):
            min = keyin
            print("再大一點")
        print("您猜了",count,"次\n")
    else:
        print("請輸入提示範圍內的數字")
```

### while ... else語法:
- 在while迴圈內,如果沒有使用到break跳出迴圈,則迴圈結束後要執行else的程式區塊

```python
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position] 
    if number%2==0:
        print('發現偶數', number)
        break
    position += 1
else: # 沒有執行break
    print('沒有偶數')
			
沒有偶數
```

### 使用range()產生數值串列
- 使用range()產一個範圍的數值list
- range()不會像list,tuple,set,dictionary先佔用大量記憶體空間
- 語法:range(start, stop, step).
- 如果省略start,只有stop,start預設為0
- 如同slice,產生的值並不包含stop
- step預設值為1


```python
for x in range(0,3): 
    print(x)
    
結果==========
0
1
2
```

```python
list( range(0, 3))

結果========
[0, 1, 2]
```

#### Homework:小王班上有五位學生，請您為小王設計一個輸入成績的程式，並且在輸入成績後顯示班上總成績及平均成績。
```python
#range1.py
#小王班上有五位學生，請您為小王設計一個輸入成績的程式，並且在輸入成績後顯示班上總成績及平均成績。

結果========
請輸入第1位學生的成績:89
請輸入第2位學生的成績:89
請輸入第3位學生的成績:89
請輸入第4位學生的成績:89
請輸入第5位學生的成績:89

全班總成績為: ***分，平均為89分
```
[解題](range1.py)

```python
#如果使用-1,則每次-1
for x in range(2, -1, -1):
    print(x)
    
結果========
2
1
0
```

```python
list(range(2, -1, -1)) 

結果=======
[2, 1, 0]
```

```python
#step為2,則每次加2
list( range(0, 11, 2))

結果========
[0,2,4,6,8,10]
```

 
```python
#for 迴圈兩個參數:請留意輸出結果
#for2.py

print("兩個參數") 
for i in range(4,8):
    print(i)
print("離開後i為",i)
```




```python
#Question: 請問執行後跑出哪些整數?(選擇題)
for x in range(6,10): 
	print(x)
```
(1) 6 7 8 9  
(2) 6 7 8 9 10  
(3) 7 8 9  

```python
#for3-1.py
#(1)for 迴圈三個參數:請留意輸出結果

print("三個參數") 
for i in range(4,0,-1):
    print(i) 
print("離開後i為",i)
```

```python
#(2)for 迴圈三個參數:請留意輸出結果
#for3-2.py

print("三個參數") 
for i in range(4,8,2):
    print(i) 
print("離開後i為",i)
```


```python
#Question: 請問執行後跑出哪些整數?(選擇題)

for x in range(0,8,2) :
    print(x)
```
(1) 0 2 4 6 8  
(2) 0 2 4 6  
(3) 0 2 8  


## 使用for in迴圈
- 使用時機,讀取所有集合物件元素1次。(list,tuple,string,dictionaries,sets)
- 使用時機,明確指定執行次數。

```python
#使用傳統的方式,讀取list內的每一個元素
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter'] 
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1
    
結果=======
Flopsy
Mopsy
Cottontail
Peter
```

```python
#使用更簡潔方式(for..in)
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
for rabbit in rabbits: 
    print(rabbit)
			
結果=======
Flopsy
Mopsy
Cottontail
Peter

```


### 字串每次取出一個字元

```python
word = 'cat'
for letter in word:
    print(letter)
			
結果=======
c
a
t
```

### 使用for in讀取dictionary,取出的元素是key, 也可以使用dictionary.keys()方法.
- 使用values()方法取出元素的值

```python

accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}

for card in accusation: # 或者使用 accusation.keys():
    print(card)

結果=======
room
weapon
person

```

```python
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}

#使用values()方法取出元素的值
for value in accusation.values(): 
    print(value)

結果=======
ballroom
lead pipe 
Col. Mustard
```

```python
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}

#使用items()方法,取出包含key和value的tuple, 
for item in accusation.items(): 
    print(item)

結果=======
('room', 'ballroom')
('weapon', 'lead pipe') 
('person', 'Col. Mustard')


```

```python
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}

#使用拆解法直接同時取出key和value
for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents 

			
Card weapon has the contents lead pipe
Card person has the contents Col. Mustard
Card room has the contents ballroom
```

###  迴圈中斷
- break 與 continue 都是迴圈中斷語法
	- break 代表迴圈中斷後跳出迴圈。
	- continue 代表迴圈中斷後繼續執行迴圈。


```python
#迴圈中斷:請留意輸出結果
#break.py

i = ['a', 'b', 'c', 'd'] 
for j in i:
    if j == 'c': 
        break
    print(j)

```


```python
#迴圈中斷:請留意輸出結果
#continue.py

i = ['a', 'b', 'c', 'd'] 
for j in i:
    if j == 'c': 
        continue
    print(j)
```

### 巢狀迴圈

```python
#=======================================================================
# Name        : forNest2.py
#利用2層迴圈列印九九乘法表
#=======================================================================
1*1=1   1*2=2   1*3=3   1*4=4   1*5=5   1*6=6   1*7=7   1*8=8   1*9=9
2*1=2   2*2=4   2*3=6   2*4=8   2*5=10  2*6=12  2*7=14  2*8=16  2*9=18
3*1=3   3*2=6   3*3=9   3*4=12  3*5=15  3*6=18  3*7=21  3*8=24  3*9=27
4*1=4   4*2=8   4*3=12  4*4=16  4*5=20  4*6=24  4*7=28  4*8=32  4*9=36
5*1=5   5*2=10  5*3=15  5*4=20  5*5=25  5*6=30  5*7=35  5*8=40  5*9=45
6*1=6   6*2=12  6*3=18  6*4=24  6*5=30  6*6=36  6*7=42  6*8=48  6*9=54
7*1=7   7*2=14  7*3=21  7*4=28  7*5=35  7*6=42  7*7=49  7*8=56  7*9=63
8*1=8   8*2=16  8*3=24  8*4=32  8*5=40  8*6=48  8*7=56  8*8=64  8*9=72
9*1=9   9*2=18  9*3=27  9*4=36  9*5=45  9*6=54  9*7=63  9*8=72  9*9=81


for i in range(1,10):
    for j in range(1,10):
        print(i, " * ", j, " = ", i*j, end='\t')
        print("%-2d*%2d =%2d" % (i,j,i*j),end="   ")
    print()
```


```python
#========================================================
# Name        : forNest1.py
#利用2層迴圈列印「井」字，將其排列成直角三角形
#=======================================================

顯示:
#
##
###
####
#####



for i in range(1,6):
    for _ in range(i):
        print("#",end='')
    print()
```



### for break else語法
檢查如果沒有使用break跳出迴圈,就執行else區塊

```python
#檢查是否cheeses為空list
cheeses = []
for cheese in cheeses:
    print('我喜歡的cheese有', cheese)
    break
else: # no break means no cheese
    print('沒有任何cheese') 
    
結果:=============			
沒有任何cheese
```

### 使用for in zip()同步平行讀取多個串列物件

```python
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts): 
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

結果:=============
Monday : drink coffee - eat banana - enjoy tiramisu
Tuesday : drink tea - eat orange - enjoy ice cream
Wednesday : drink beer - eat peach - enjoy pie
```

```python
#使用zip()組合每個串列內元素成為tuple
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
list( zip(english, french))

結果:==============
[('Monday', 'Lundi'), ('Tuesday', 'Mardi'), ('Wednesday', 'Mercredi')]
```

```python
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
dict(zip(english, french))

結果:=========
{'Monday': 'Lundi', 'Tuesday': 'Mardi', 'Wednesday': 'Mercredi'}
```

#### Homework:
```python
#問題various_loop1.py
以for迴圈計算1到100的和

顯示=================
1+2+3+~+100的總合是5050
```
[解題](various_loop1.py)

#### Homework:
```python
#問題 various_loop2.py
以while迴圈計算1到100的和

顯示============
1+2+3+~+100的總合是5050
```
[解題](various_loop1.py)

#### Homework:
```python
#問題 nestedLoop1.py
試寫出下列數字排列的程式 
顯示=================================

55555
4444
333
22
1
```
[解題](nestedLoop1.py)

#### Homework:
```python
#問題 inputLoop.py
設計一個程式，使用者輸入一個M, 再輸入另一個數N,然後程式可以求出M*1 + M*2 + M*3 + M*4 + M*5....... + M*N的值

顯示==========================
輸入M:5
輸入N:4
M*1 + M*2 + M*3 + ......+ M*N = 50
```
[解題](inputLoop.py)

#### Homework:
```python
#問題 commonfactor.py
設計一個程式，可以由鍵盤輸入兩個數值，並求出這2個數值的最大公因數和最小公倍數

顯示======================================
求兩數的最大公因數和最小公倍數
請輸入第一個整數:XXX
請輸入第二個整數:XXX

計算結果:
14 和 35 的最大公因數:7
14 和 35 的最小倍數是:70
```
[解題](commonfactor.py)


