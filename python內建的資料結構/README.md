
# python內建的資料結構
## Lists, Tuples, Dictionaries, and Sets
### tuple 與 list 的差異
- 括號不同:
	- tuple 是用小括號()將元素包起來。
	- list 是用中括號[]將元素包起來。

- 元素可否變更:
	- tuple 決定了元素的內容就不可以變更。
	- list 可以隨時修改。

### list 介紹
- list 內資料用逗號隔開，放置於中括號的範圍內。 
	- list_name = [1,2,3 ]
- list 可以儲存不同類型的值或項目，如數字和字串。
	- list_name = [1, 2, ‘Python’, ‘lists’ ]
- list 內的資料可以進行增加、更新與移除。
- 可透過.index( )方法取得指定資料的索引。

 
```python
# 使用中括號 [] or list() 建立空的list

>>> empty_list = [] #使用[]建立空的list
>>> weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'] 
>>> big_birds = ['emu', 'ostrich', 'cassowary'] 
>>> first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']


>>> another_empty_list = list() #使用list()建立空字串 
>>> another_empty_list
[]

```



```python
#使用list()轉換其它型態為list
>>> list('cat')
['c', 'a', 't']


>>> a_tuple = ('ready', 'fire', 'aim') 
>>> list(a_tuple)
['ready', 'fire', 'aim']


>>> birthday = '1/6/1952' 
>>> birthday.split('/') 
['1', '6', '1952']


>>> splitme = 'a/b//c/d///e'
>>> splitme.split('/')
['a', 'b', '', 'c', 'd', '', '', 'e']


>>> splitme = 'a/b//c/d///e' 
>>> splitme.split('//')
['a/b', 'c/d', '/e']

```

---

###  索引標籤
- 索引編號放在 [ ] 內。
- 由左向右 ( 由前向後 ) 存取，編號由 0 開始遞增。
- 由右向左 ( 由後向前 ) 存取，編號由 -1 開始遞減。

| 0 | 1 | 2 | 3 | 4 | 5 |
|:--|:--|:--|:--|:--|:--|
| -6 | -5 | -4 | -3 | -2 | -1 |

```python
#使用索引編號取出內容

>>> citys = ['台北', '台中', '高雄']
>>> citys[0]
    '台北'
>>> citys[1]
	'台中'
>>> citys[2]
	'高雄'

>>> citys[-1] 
'高雄'
>>> citys[-2] 
'台中'
>>> citys[-3] 
'台北'


>>> citys = ['台北', '台中', '高雄'] 
>>> citys[3]

IndexError                               
Traceback (most recent call last)
<ipython-input-5-73d59aebae96> in <module>
----> 1 citys[3]

IndexError: list index out of range
>>> citys[-5]
IndexError                               
Traceback (most recent call last)
<ipython-input-5-73d59aebae96> in <module>
----> 1 citys[-5]

IndexError: list index out of range

```

---

```python
#list0.py
#list 與 tuple,請留意輸出結果

 list1=['H','i'] 
 tuple1=('H','i') 
 
 print(tuple1) 
 print(list1) 
 
 tuple1[1]='a' 
 list1[1]='a' 
 
 print(tuple1) 
 print(list1)
```

---

```python
#Question: 請問執行後的結果哪一個是對的?(選擇題)

tuple1=('1','2') 
tuple1[1]='0' 
print(tuple1)

(1) 02   
(2) 10   
(3) 120   
(4)錯誤  
```


---

  
```python
#請問執行後的結果哪一個是對的?(選擇題)

list1=['1','2'] 
list1[1]='0' 
print(list1)

(1) ['0','2']   
(2) ['1', '0']   
(3) ['1', '20']   
(4) 錯誤
```
  

---


```python
#操作範例:請動手操作，並留意輸出結果
#list1.py

list1=['H','e','l','l','o', 'W','o','r','l','d']
print(list1[0])
print(list1[1])
print(list1[-1])
print(list1[-3])
```

---



```python
#請問執行後的結果哪一個是對的?(選擇題)

list1=['p','y','t','h','o','n']
print(list1[-2])


(1) y   
(2) n   
(3) o   
(4) p 
```
 

---

#### Homework:建立一個包含3個元素的整數陣列並設定初始值，代表個人的三科成績，再依序顯示各科成績。
```python
#array1.py
#建立一個包含3個元素的整數陣列並設定初始值，代表個人的三科成績，再依序顯示各科成績。
```
[顯示](array1.py)

---


###  使用切割語法,取出部份值
- list內部分取值採用[ n:m ]方式，n與m是整數。
	- n 代表起始位置，第一個為 0。
	- m 代表結束位置，不包含這個位置。

| 0 | 1 | 2 | 3 | 4 | 5 |
|:--|:--|:--|:--|:--|:--|
| -6 | -5 | -4 | -3 | -2 | -1 |

 
```python
#操作範例:請動手操作，並留意輸出結果
#list2.py

list1=['H','e','l','l','o', 'W','o','r','l','d']
print(list1[2:])
print(list1[:3])
print(list1[3:5])
```



```python
#操作範例:請動手操作，並留意輸出結果
#list2.py

list1=['H','e','l','l','o', 'W','o','r','l','d']
print(list1[2:])
print(list1[:3])
print(list1[3:5])
```
---

| H | e | l | l | o | W | o | r | l | d |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

 
```python
#請選出以下程式碼跑出的結果。

list1=['H','e','l','l','o', 'W','o','r','l','d']
print(list1[0])


(1)'H'  
(2)'W'  
(3)'l'  
(4)'d'
```
  


```python
#請選出以下程式碼跑出的結果。
list1=['H','e','l','l','o', 'W','o','r','l','d']
print(list1[-1])


(1)'H'  
(2)'W'  
(3)'l'  
(4)'d'
```
  



```python
#slice
>>> citys = ['台北', '台中', '高雄']
>>> citys[0:2]
['台北', '台中']


>>> citys[::2]
['台北', '高雄']


>>> citys[::-2] 
['高雄', '台北']


>>> citys[::-1]
['高雄', '台中', '台北']

```

---

###  更新資料
- 指定 list 的索引編號就可以給予新的資料，將這個項目內容更新。
	- List1[2]=123



```python
#請問最後輸出結果會是什麼?(選擇題)
list1=['a','b','c']  
list1[2]='dd' 
print(list1)


(1) ['a','dd','b','c']    
(2) ['a','b','dd','c']    
(3) ['a','b','dd']   
(4) ['a','dd','c']
```

  
 



```python
#請依照下列問題找出正確的答案。(選擇題)
你有一個list x:
x = ["a", "b", "b"]
請改變第2個"b"成為"c"


(1) x[2] = "c"  
(2) x[2] = c  
(3) x[3] = "c"  
(4) x[3] = c 
```

 

---

### 2維List
```python
>>> nb = ['筆記電腦', '商用筆電']
>>> mobile = ['APPLE', 'ASUS', 'HTC'] 
>>> home = [3, '冰箱', 2, '洗衣機']
>>> all3c = [nb, mobile, home]


>>> all3c
[['筆記電腦', '商用筆電'], ['APPLE', 'ASUS', 'HTC'], [3, '冰箱', 2, '洗衣機']]


>>> all3c[0]
['筆記電腦', '商用筆電']


>>> all3c[1]
['APPLE', 'ASUS', 'HTC']


>>> all3c[2][1] 
'冰箱'

```

---


###  list 項目附加資料
- append 附加資料:
	-  你提供的資料就以一筆資料方式加入到 list。
	-  一次只能加入一個資料。
- 也可利用 + list 的方式於原本的 list 之後附加新的資料。

```python
#list5.py

list1= ['a', 'b', 'c'] 
print("附加之前:", list1) 
print("附加之前長度 = ", len(list1))
list1.append(["def","ghij"]) 
print("附加之後:", list1) 
print("附加之後長度 = ", len(list1))
print(list1[3])
```

--- 
#### Homework:建立一個包含五個元素的整數陣列，讓使用者輸入五位學生的成績，然後計算班級總成績及平均成績
```python
# Name        : score1.py
#建立一個包含五個元素的整數陣列，讓使用者輸入五位學生的成績，然後計算班級總成績及平均成績
#============================================================
請輸入第1位學的成績78
請輸入第2位學的成績89
請輸入第3位學的成績67
請輸入第4位學的成績90
請輸入第5位學的成績89
全班總成績為:413分,平均為82.6分
#============================================================
```
[解題](score1.py)

---

##### Homework:
```python
#問題 sale_s.py
#小英是百貨公司結帳員,請您為她設計一個程式，先輸入客戶購買的貨品件數，再依此件數宣告陣列來儲存貨品價格，最後計算全部貨品總價

顯示=======
請輸入購買貨品件數:4
請輸入第1件貨品的價格:xxx
請輸入第2件貨品的價格:xxx
請輸入第3件貨品的價格:xxx
請輸入第4件貨品的價格:xxx
全部貨品總價為:xxxxx元
```
[解題](sale_s.py)

--- 

###  list 項目擴展資料
- extend 擴展資料
	- 如果引號括起來的字串有 [ ] 將會拆解成好幾個資料。
	- 可以把其他 list 加入到這個 list 內，擴展多個欄位。



```python
#操作範例:請動手操作，並留意輸出結果
#list6.py

list1= ['a', 'b', 'c']
print("擴展之前:", list1) 
print("擴展之前長度 = ", len(list1))
list1.extend(['d','e'])
print("擴展之後:", list1) 
print("擴展之後長度 = ", len(list1)) 
print(list1[3])
```


```python
#使用extend()或+=
>>> citys = ['台北', '台中', '高雄']
>>> citys.append('台南')
>>> citys
['台北', '台中', '高雄', '台南']


>>> citys = ['台北', '台中', '高雄', '台南'] 
>>> others = ['花蓮', '台東']
>>> citys.extend(others)
>>> citys
['台北', '台中', '高雄', '台南', '花蓮']


>>> citys = ['台北', '台中', '高雄', '台南', '花蓮']
>>> others = ['宜蘭', '新竹']
>>> citys += others
>>> citys
['台北', '台中', '高雄', '台南', '花蓮', '台東', '宜蘭', '新竹']


>>> citys = ['台北', '台中', '高雄', '台南', '花蓮'] 
>>> others = ['宜蘭', '新竹']
>>> citys.append(others)
>>> citys
['台北', '台中', '高雄', '台南', '花蓮', ['宜蘭', '新竹']]
```
---

### list 項目插入新資料
- list 可使用 insert 方式插入新的資料:
	- list.insert(索引值,插入的資料)。

```python
#操作範例:請動手操作，並留意輸出結果
#list7.py

 list1 = ['this', 'is', 'list'] 
 print(list1) 
 list1.insert(1, 'item') 
 print(list1) 
 list1.insert(88, '88') 
 print(list1)
```


```python
#Question:請問以下的結果會是什麼?(選擇題)

 list1 = ['a', 'b', 'c'] 
 list1.insert(1, 'x') 
 print(list1)
 
(1) ['x','a','b','c']   
(2) ['a','x','b','c']    
(3) ['a','b','x','c']   
(4) ['a','b','c','x'] 
```
  
 
 
 ```python
 #insert
>>> citys = ['台北', '台中', '高雄']
>>> citys.insert(3, '台南') 
>>> citys
['台北', '台中', '高雄', '台南']


>>> citys.insert(10, '花蓮')
>>> citys
['台北', '台中', '高雄', '台南', '花蓮']

 ```
 ---
 
###  list 移除項目
- list 可透過以下三種方式移除項目:
	- list.remove( )
	- list.pop( )
	- del list[ ]

```python
#del
#pop()
>>> citys = ['台北', '台中', '高雄', '台南', '花蓮']
>>> del citys[-1]
>>> citys
['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']


>>> citys = ['台北', '台中', '高雄', '台南', '花蓮'] 
>>> citys[2]
'高雄'
>>> del citys[2]
>>> citys
['台北', '台中', '台南', '花蓮']
>>>citys[2]
'台南'


>>> all3c = ['筆記電腦', '商用筆電', 'APPLE', 'ASUS', 'HTC'] 
>>> all3c.remove('APPLE')
>>> all3c
['筆記電腦', '商用筆電', 'ASUS', 'HTC']


>>> all3c = ['筆記電腦', '商用筆電', 'APPLE', 'ASUS', 'HTC'] 
>>> all3c.pop()
'HTC'
>>> all3c
['筆記電腦', '商用筆電', 'APPLE', 'ASUS']
>>> all3c.pop(1)
'商用筆電'
>>> all3c
['筆記電腦', 'APPLE', 'ASUS']
```
--- 

###  list.remove
- list 可透過 remove 方式移除資料
	- 依據內容進行刪除
	- list.remove(項目內容)
--- 
 
```python
#Question:請問以下的結果會是什麼?(選擇題)
#1. 有兩個以上的相同資料， 會先移除哪一個呢?
#2. 如果沒有資料那會如何呢?

list1 = ['1', 'x', '2', 'x', '3'] 
list1.remove('x') 
print(list1)


(1) ['x','1', '2', '3']
(2) ['1', '2', '3'] 
(3) ['1', '2', 'x', '3']
(4) ['1','x', '2', '3']
```


---
###  list.pop
- list 可透過 pop 方式移除指定位置資料。
	- 如果 pop( ) 內沒有參數，則移除最後一筆資料。
	- pop( ) 內若有參數，則移除指定位置的資料。


```python
#Question:請問以下的結果會是什麼?(選擇題)


list1 = ['1', 'x', '2', 'x', '3']
list1.pop( ) 
print(list1)


(1) ['x','2','x','3']   
(2) ['1','x','2','x']   
(3) ['x','2','x']
(4) ['1','2','x','3']
```


---

```python
#Question:請問以下的結果會是什麼?(選擇題)


list1 = ['1', 'x', '2', 'x', '3']
list1.pop(1) 
print(list1)

(1) ['x','2','x','3'] 
(2) ['1','x','2','x'] 
(3) ['x','2','x']
(4) ['1','2','x','3']
```



---

###  del list[ ]
- list 可透過 del 方式移除指定位置資料。
- del list[ ] 必須指定範圍:
	- del list[n] 代表移除第 n 位索引值資料。
	- del list[:n] 代表移除第 n 位索引值之前 ( 不包含 n ) 資料。
	- del list[m:n] 代表移除第 m 到 n 位索引值之前 ( 不包含 n ) 資料。


 
```python
#Question:請問以下的結果會是什麼?(選擇題)

list1 = ['1', 'x', '2', 'x', '3']
del list1[:1] 
print(list1)

(1) ['x','2','x','3'] 
(2) ['1','2','x','3'] 
(3) ['1','x','2','x']
(4) ['2','x','3']
```




 
```python
#請問以下的結果會是什麼?(選擇題)


list1 = ['1', 'x', '2', 'x', '3']
del list1[2:4] 
print(list1)

(1) ['2','x','3']
(2) ['1','x','3']
(3) ['x','2','x']
(4) ['1','x']
```

---

### list index(), in, count()

```python
#index(value)- 取出value索引編號
#in - 測試是否有值
#count(value) - value的數量

>>> citys = ['台北', '台中', '高雄', '台南', '花蓮'] 
>>> citys.index('台中')
1

>>> citys = ['台北', '台中', '高雄', '台南', '花蓮'] 
>>> citys.index('台中1')
ValueError                                
Traceback (most recent call last)
<ipython-input-78-e4644962e59d> in <module>
      1 #檢查
      2 citys = ['台北', '台中', '高雄', '台南', '花蓮']
----> 3 citys.index('台中1')

ValueError: '台中1' is not in list



>>> citys = ['台北', '台中', '高雄', '台南', '花蓮']  
>>> '高雄' in citys
True
>>> '新竹' in citys
False


>>> words = ['a', 'deer', 'a' 'female', 'deer'] 
>>> 'deer' in words
True


>>> citys = ['台北', '台中', '高雄', '台南', '花蓮']
>>> citys.count('台北')
1
>>> citys.count('新竹')
0
>>> snack = ['蛋糕', '蛋糕', '蛋糕'] 
>>> snack.count('蛋糕')
3

```
---

###  list 排序
- list 進行排序有 sorted( ) 與 sort( ) 兩個動作。
- 兩者差異:
	- sorted( )
		- 不會影響 list 本身結構，且可以輸出結果。
		- sorted(list項目)。
		- sorted( ) 可用來排序任何項目。
	- sort( )
		-  會影響 list 本身結構，且不可以於操作這個動作時進行輸出。
		-  list.sort( )
		-  sort( ) 只能用在list上排序。


###  排序原則與參數
- 排序原則:
	- 數字則依照大小排序。
	- 字串則依照 ASCII 編碼順序進行排序。


###  排序原則與參數
- 可加入的引數名稱:
	- reverse=True
		- 有這個參數由大到小排序
		- 若沒有這個參數則由小到大排序
	- key=len
		- 依照 list 內元素字串長度進行排序
	- key=str.upper
		- 將 list 內元素轉換為大寫，再依照 ASCII 編碼順序進行排序
	- key=str.lower
		- 將 list 內元素轉換為小寫，再依照 ASCII 編碼順序進行排序




```python
#sort(),sorted()

>>> marxes = ['Groucho', 'Chico', 'Harpo'] 
>>> sorted_marxes = sorted(marxes)
>>> sorted_marxes
['Chico', 'Groucho', 'Harpo']


>>> marxes
['Groucho', 'Chico', 'Harpo']
>>> marxes.sort()
>>> marxes
['Chico', 'Groucho', 'Harpo']
```


```python
#排序的原理:ASCII
list2 = ['c','b','a','A']
list2.sort()
print(list2)
print(ord('a'),ord('b'),ord('c'),ord('A'))


['A', 'a', 'b', 'c'] 
97 98 99 65
```
---


```python
#操作範例:請動手操作，並留意輸出結果
#list8.py

a = [5, 2, 1, 9, 6] 
print(sorted(a))
print(a)
print(sorted(a, reverse=True) ) 
print(a)
a.sort(reverse=True) 
print(a)

```



```python
#sort()-排序
#len()-數量
>>> numbers = [2, 1, 4.0, 3] 
>>> numbers.sort()
>>> numbers
[1, 2, 3, 4.0]


>>> numbers = [2, 1, 4.0, 3] 
>>> numbers.sort(reverse=True) 
>>> numbers
[4.0, 3, 2, 1]


>>> marxes = ['Groucho', 'Chico', 'Harpo']
>>> len(marxes)
3
```
---

#### Homework:  
試使用陣列配合for迴圈，找尋陣列中最小值的程式，程式執行時會要求連續輸入5個數值，輸入完畢會顯示所輸入5個數值中的最小值
```python
#問題 min.py
#試使用陣列配合for迴圈，找尋陣列中最小值的程式，程式執行時會要求將輸入數值的數量，輸入完畢會顯示所輸入數值中的最小值
#=====================================================================
請輸入數值:4
請輸入第1數值:4
請輸入第2數值:5
請輸入第3數值:6
請輸入第4數值:7
4 | 5 | 6 | 7 | 最小值是:4
#=====================================================================
```
[解題](min.py)

---

### copy()

```
#list copy()


>>> a=[1,2,3] 
>>> a
[1, 2, 3] 
>>> b=a


>>> b
[1, 2, 3]
>>> a[0] = 'surprise'
>>> a
['surprise', 2, 3]
>>> b
['surprise', 2, 3]


>>> b
['surprise', 2, 3]

>>> b[0] = 'I hate surprises'
>>> b
['I hate surprises', 2, 3]
>>> a
['I hate surprises', 2, 3]

#3種copy方式
>>> a=[1,2,3] 
>>> b = a.copy() 
>>> c = list(a) 
>>> d=a[:]


>>> a[0] = 'integer lists are boring'
>>> a
['integer lists are boring', 2, 3]
>>> b
[1, 2, 3]
>>> c
[1, 2, 3]
>>> d
[1, 2, 3]
```

---

#### Homework:任由使用者輸入任意個數的數值序列,程式會將此數值序列由小到大和由大到小排序後顯示
```pyhon
# Name        : bubble.py
#任由使用者輸入任意個數的數值序列,程式會將此數值序列由小到大和由大到小排序後顯示
#============================================================

請輸入要排序的數值個數:5
請輸入第1個數值:45
請輸入第2個數值:78
請輸入第3個數值:24
請輸入第4個數值:69
請輸入第5個數值:91
排序前
45.0 78.0 24.0 69.0 91.0 
由小到大排序後:
24.0 45.0 69.0 78.0 91.0 
由大到小排序後:
91.0 78.0 69.0 45.0 24.0 
#============================================================
```
[解題](bubble.py)

---

###  資料反向
- 可利用 reverse( ) 函數進行反向排序動作。
- 這函數沒有傳回值，list 執行後就會進行反向排序。

```python
#Question: 請問以下的結果會是什麼?(選擇題)

list2 = [12, 'ab', 'Ab', 'aB'] 
list2.reverse()
print (list2)


(1) ['aB', 'Ab', 'ab', 12] 
(2) ['Ab', 'aB', 'ab', 12] 
(3) ['ab', 'aB', 'Ab', 12] 
(4) [12,'ab', 'aB', 'Ab']
```


---


## Tuples

```python
#tuple
>>> empty_tuple = () 
>>> empty_tuple
()


>>> one_city = '台北', 
>>> one_city 
('台北',)


>>> citys = '台北', '台中', '高雄', '台南', '花蓮' 
>>> citys
('台北', '台中', '高雄', '台南', '花蓮')


>>> citys = ('台北', '台中', '高雄', '台南', '花蓮') 
>>> citys
('台北', '台中', '高雄', '台南', '花蓮')


>>> citys = ('台北', '台中', '高雄') 
>>> a, b, c = citys
>>> a
'台北'
>>> b
'台中'
>>> c
'高雄'

#內容交換
>>> password = 'swordfish'
>>> icecream = 'tuttifrutti'
>>> password, icecream = icecream, password
>>> password
'tuttifrutti'
>>> icecream
'swordfish'


>>> marx_list = ['Groucho', 'Chico', 'Harpo'] 
>>> tuple(marx_list)
('Groucho', 'Chico', 'Harpo')
```

---

#### Homework:
```python
#Name        : sequential.py
#百貨公司舉辦週年抽獎活動，將顧客的抽獎編號及姓名分別儲存於陣列中，使用者輸入編號，程式會搜尋出該編號的姓名並顯示。若查詢不到也會顯示無此編號的訊息

#============================================================

請輸入中獎者的編號943
中獎者的姓名為:stu3

#============================================================

```
[解題](sequential.py)
---

#### Homework:
```python
#問題 ninenine.py
#以程式建立 9 x 9 的二維整數陣列，陣列內容是九九乘法表的乘積，並將之輸出

#顯示==========
1*1=1   1*2=2   1*3=3   1*4=4   1*5=5   1*6=6   1*7=7   1*8=8   1*9=9
2*1=2   2*2=4   2*3=6   2*4=8   2*5=10  2*6=12  2*7=14  2*8=16  2*9=18
3*1=3   3*2=6   3*3=9   3*4=12  3*5=15  3*6=18  3*7=21  3*8=24  3*9=27
4*1=4   4*2=8   4*3=12  4*4=16  4*5=20  4*6=24  4*7=28  4*8=32  4*9=36
5*1=5   5*2=10  5*3=15  5*4=20  5*5=25  5*6=30  5*7=35  5*8=40  5*9=45
6*1=6   6*2=12  6*3=18  6*4=24  6*5=30  6*6=36  6*7=42  6*8=48  6*9=54
7*1=7   7*2=14  7*3=21  7*4=28  7*5=35  7*6=42  7*7=49  7*8=56  7*9=63
8*1=8   8*2=16  8*3=24  8*4=32  8*5=40  8*6=48  8*7=56  8*8=64  8*9=72
9*1=9   9*2=18  9*3=27  9*4=36  9*5=45  9*6=54  9*7=63  9*8=72  9*9=81
```
[解題](ninenine.py)

---

#### Homework:
```python
#============================================================================
# Name        : initial2.py
#建立一個2*3的二維陣列並初始化，用來儲存2個學生各三科成績，再以2層巢狀迴圈將所有成績顯示出來。

#============================================================

第1位學生第1科成績:85
第1位學生第2科成績:82
第1位學生第3科成績:90
#================================================
第2位學生第1科成績:76
第2位學生第2科成績:95
第2位學生第3科成績:89
#================================================

```
[解題](initial2.py)

---

## Dictionaries 介紹
- 可以想像你現在手上有一本電子英漢字典，當你輸入英文單字的時候，
就可以查得到它的唯一翻譯。
- 你所關心的英文單字與翻譯之間有著 一對一 的關係:
	- 你輸入的英文單字，就叫做 Key 
	- 而得到的翻譯，就叫做 Value 
- 一個 Dictionary 是一群 Key : Value 配對的集合
- 資料結構是由 key:value 所組成。
- key 不能夠重複，否則會被後面的結果蓋過去。
- 可輸入 key 找尋您要找出來的值。
- 如果輸入的 key 不存在，那就會出現錯誤訊息。

### 建立Dictionary

```python
#建立Dictionary

>>> empty_dict = {} 
>>> empty_dict
{}


>>> codes = {
"tw": "Taiwan",
"jp": "japan",
"hk": "Hong Kong"
 } 



>>> codes
{"tw": "Taiwan","jp": "japan","hk": "Hong Kong" } 

>>> codes['tw']
'taiwan'

>>> lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
>>> dict(lol)
{'c': 'd', 'a': 'b', 'e': 'f'}


>>> lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
>>> dict(lot)
{'c': 'd', 'a': 'b', 'e': 'f'}


>>> tol = ( ['a', 'b'], ['c', 'd'], ['e', 'f'] )
>>> dict(tol)
{'c': 'd', 'a': 'b', 'e': 'f'}


>>> los = [ 'ab', 'cd', 'ef' ]
>>> dict(los)
{'c': 'd', 'a': 'b', 'e': 'f'}


>>> tos = ( 'ab', 'cd', 'ef' )
>>> dict(tos)
{'c': 'd', 'a': 'b', 'e': 'f'}
``` 

---

###  key 與 value
- key 不能於程式內改變:
	- 可以用數字、字串或者 tuple
	- 不可以使用 list

- 如何找出所有的 key 與 value
	- 您可以透過 dict1.keys( ) 這個方法找出所有的 key
	- 您可以透過 dict1.values( ) 這個方法找出所有的 value


###  新增與修改
- 新增一筆資料
	- 請將 key 與 value 儲存至一個變數內
	- 透過 dict.update(新增的資料) 這個方法的方式就可以新增

- 元素可否變更:
	- 以 = 指派方式指派給 key 就可以變更資料

---

```python
#操作範例:請動手操作，並留意輸出結果
# dict1.py
dict1={'a':200,'b':400,'b':300} 
print(dict1)
print(dict1['a']) 
print(dict1['b']) 
print(dict1['d']) #不存在
```

```python
#Question: 請問執行後的結果哪一行是錯的?(選擇題)

dict1={'a':100,'b':200, 'b':300} 
print(dict1)
print(dict1['a']) 
print(dict1['d'])

(1) print(dict1)   
(2) print(dict1['a'])  
(3) print(dict1['d'])  
(4) 沒有錯誤.
```
 
```python
#請問執行後的結果是哪一個答案呢?(選擇題)

dict1={'a':100,'b':200,'b':300}
print(dict1['b'])

(1) 100  
(2) 200   
(3) 300  
(4) 0  
```


---




```python
#操作範例 1:請動手操作，並留意輸出結果
#dict3.py

dict1={'a':100,'b':200, 'c':300} 
print(dict1)
add_dic={'d':400} 
dict1.update(add_dic) 
print(dict1)
```

```python
#dict4.py

dict1={'a':100,'b':200, 'c':300} 
print(dict1)
dict1['a']='test'
print(dict1)
```



```python
#Question:請問執行後的結果哪一個是對的?(選擇題)

dict1={'a':100,'b':200, 'c':300} 
add_dic={'d':400} 
dict1.update(add_dic) 
print(dict1['d'])

(1) 產生錯誤  
(2) 200  
(3) 300  
(4) 400
```



```python
#請問執行後的結果哪一個是對的?(選擇題)
dict1={'a':100,'b':200, 'c':300} 
add_dic={'d':400} 
dict1.update(add_dic) 
print(dict1['e'])

(1) 產生錯誤  
(2) 200  
(3) 300  
(4) 400   
``` 

```python
#{}
>>> nums = {
1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five',
}

>>> nums
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

#沒有key就新增
>>> nums[6] = 'six'
>>> nums
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}

#有key就更新
>>> nums[6] = 'SIX'
>>> nums
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'SIX'}

```
---

```python
>>> nums = {
1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five',
}

>>> nums
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

#利用update(dictionary), 一次增加多個key,value
>>> others = {6:'six', 7:'seven'}
>>> nums.update(others)
>>> nums
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven'}
```
---

#### Homework:
```python
#============================================================================
# Name        : vote.py
#設計一個投票統計表，包含計算各四位歌手3個地區投票數及總得票數，最後顯示得票數和得票率(計算至小數2位)
#===============================================================

names[0]:周華見
names[1]:劉得華
names[2]:張學有
names[3]:梁朝為
周華見總票數為:1623
周華見得票率為22.7025%

劉得華總票數為:1726
劉得華得票率為24.1432%

張學有總票數為:1519
張學有得票率為21.2477%

梁朝為總票數為:2281
梁朝為得票率為31.9066%

#============================================================
```
[解題](vote.py)

---

###  刪除動作
- 刪除動作可分刪除資料、清除所有項目與刪除字典三種:
	- del dict[key]  刪除某一個 key 的資料
	- dict.clear( )  清除所有項目
	- del dict  刪除字典

-
###  關於 key 的判斷
- 請以 (key in dict1.keys( )) 方式進行判斷
- 存在傳回 true
- 不存在傳回 false




```python
#操作範例 :請動手操作，並留意輸出結果
#dict5.py

dict1={'a':100,'b':200, 'c':300} 
print(dict1)
del dict1['c']
print(dict1)
print('c' in dict1) 
print('a' in dict1)
```


```python
#Question:請問執行後的結果哪一個是對的?(選擇題)

dict1={'a':100,'b':200, 'c':300} 
del dict1['b']
print ('b' in dict1)



(1) 產生錯誤  
(2) True  
(3) 200  
(4) False  
```



```python
#Question: 請問執行後的結果哪一個是對的?(選擇題)
dict1={'a':100,'b':200, 'c':300} 
dict1.clear( )
print ('b' in dict1)


(1) 產生錯誤  
(2) True  
(3) 200  
(4) False 

```

---

```python
#update()
>>> first = {'a': 1, 'b': 2} 
>>> second = {'b': 'platypus'} 
>>> first.update(second)
>>> first
{'b': 'platypus', 'a': 1}

>>> del pythons['Marx']
``` 

---

```python
#clear()

>>> nums = {
1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five',
}

>>> del nums[1]
>>> nums
{2: 'two', 3: 'three', 4: 'four', 5: 'five'}


>>> nums.clear() 
>>> nums
{}
>>> nums = {}
>>> nums
{}

>>> del nums
>>> nums
NameError                                 
Traceback (most recent call last)
<ipython-input-119-55a5412c7eee> in <module>
----> 1 del nums
      2 nums

NameError: name 'nums' is not defined
```
---


```python
#Question:請問執行後的結果哪一個是對的?(選擇題)
dict1={'a':100,'b':200, 'c':300} 
del dict1
print('b' in dict1.keys( ))

(1) 產生錯誤   
(2) True    
(3) 200     
(4) False 
```
 

---
### keys(),values(),items(),copy()

```python

>>> signals = {'綠燈': '走', '黃燈': '走快些', '紅燈': '停等'} 
>>> signals.keys()
dict_keys(['綠燈', '黃燈', '紅燈'])


>>> list( signals.values() )
['走', '走快些', '停等']


>>> list( signals.items() )
[('綠燈', '走'), ('黃燈', '走快些'), ('紅燈', '停等')]


>>> signals = {'綠燈': '走', '黃燈': '走快些', '紅燈': '停等'} 
>>> save_signals = signals
>>> signals['blue'] = 'confuse everyone'
>>> save_signals
    {'blue': 'confuse everyone', '綠燈': '走', '黃燈': '走快些', '紅燈': '停等'}


>>> signals = {'綠燈': '走', '黃燈': '走快些', '紅燈': '停等'}

>>> original_signals = signals.copy()
>>> signals['blue'] = 'confuse everyone'
>>> signals
{'blue': 'confuse everyone','綠燈': '走', '黃燈': '走快些', '紅燈': '停等'}
>>> original_signals
{'綠燈': '走', '黃燈': '走快些', '紅燈': '停等'}

```

---


### for in

```python
#操作範例:請動手操作，並留意輸出結果
dict1={'a':100,'b':200,'c':300} 
for c in dict1.keys( ):
	print(c) 
print("-----")

for c in dict1.keys( ):
	print(dict1[c]) 
print("-----")

for c in dict1: 
	print(c)
print("-----")

for c in dict1.values( ):
	print(c)
 
```
---
###  in
```python
#in


>>> pythons = {'Chapman': 'Graham', 'Cleese': 'John',
'Jones': 'Terry', 'Palin': 'Michael'}
>>> 'Chapman' in pythons 
True
>>> 'Palin' in pythons 
True
>>> 'Gilliam' in pythons 
False


>>> pythons['Cleese']
'John'


>>> pythons['Marx']
    Traceback (most recent call last):
File "<stdin>", line 1, in <module> KeyError: 'Marx'


>>> 'Marx' in pythons 
False


>>> pythons.get('Cleese') 
'John'

#get()方法，可以加入第2個參數, 以表示如何沒有這個key時,將輸出的錯誤
>>> pythons.get('Marx', 'Not a Python')
'Not a Python'

```

---

#### Homework:
```python
// Name        : sequential1.py
//百貨公司舉辦週年抽獎活動，將顧客的抽獎編號及姓名儲存於Dictionary，使用者輸入編號，程式會搜尋出該編號的姓名並顯示。若查詢不到也會顯示無此編號的訊息

//============================================================

請輸入中獎者的編號943
中獎者的姓名為:stu3

//============================================================
```
[解題](sequential1.py)

---


## Sets

```python
#set()

>>> empty_set = set()
>>> empty_set
set()
>>> even_numbers = {0, 2, 4, 6, 8} 
>>> even_numbers
{0,8,2,4,6}
>>> odd_numbers = {1, 3, 5, 7, 9} 
>>> odd_numbers
{9,3,1,5,7}


>>> set( 'letters' )
{'l', 'e', 't', 'r', 's'}


>>> set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] ) 
{'Dancer', 'Dasher', 'Prancer', 'Mason-Dixon'}


>>> set( ('Ummagumma', 'Echoes', 'Atom Heart Mother') )
{'Ummagumma', 'Atom Heart Mother', 'Echoes'}


>>> set( {'apple': 'red', 'orange': 'orange', 'cherry': 'red'} )
{'apple', 'cherry', 'orange'}


>>> drinks = {
... 'martini': {'vodka', 'vermouth'},
... 'black russian': {'vodka', 'kahlua'},
... 'white russian': {'cream', 'kahlua', 'vodka'},
... 'manhattan': {'rye', 'vermouth', 'bitters'},
... 'screwdriver': {'orange juice', 'vodka'}
... }



```

---

#### Homework:
```python
#============================================================================
#Name        : biglottery.py
#撰寫一個大樂透電腦自動選號程式，程式執行會以亂數的方式顯示1-49之間七個不重複的大樂透號碼。

#============================================================

本期大樂透電腦選號號碼如下:

2 28 8 42 49 20 15

特別號:15
```
[解題](biglottery.py)




