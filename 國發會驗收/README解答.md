# python(人門)


```
1以下程式碼，執行時輸出值為何?

lst_1 = [1, 2]
lst_2 = [3, 4]
lst_3 = lst_1 + lst_2 
lst_4 = lst_3 * 2 
print(lst_4)

① [8, 12]
② [[1, 2], [3, 4], [1, 2], [3, 4]]
③ [1, 2, 3, 4, 1, 2, 3, 4]
④ [[1, 2, 3, 4], [1, 2, 3, 4]]
--------------------------------
③
```

```
2以下是計算跑步平均時速的程式碼，輸出結果要盡可能精準。
請問A、B處的程式碼應該為何？

distance = ____A_____(input('請輸入距離(單位：公尺)：'))
time =_____B_____ (input('請輸入時間(單位：秒)'))
avg = (distance / 1000) / (time / 3600)
print('平均時速 = ', avg, ' 公里/小時')

A: ① int    ② string    ③ float   ④ bool
B: ① int    ② float     ③ string  ④ bool

---------------------------
A:③
B:②
```

```
3已知商店營業額(total)和顧客人數(num)，要顯示顧客的平均消費金額，輸出時必須去除小數部分，請問下列哪兩個程式碼正確？

① avg = total / num
② avg = int(total / num)
③ avg = float(total // num)
④ avg = total // num

-------------------------------
②
④
```

```
4列各種資料，其正確資料型別為何？請填入下列型別 bool、float、int、str

A：  _______height = 172  
B：  _______pass1 = True
C：  _______name = "張無忌"
D：  _______score = 98.0
E：  _______tel = '0928000000'  

--------------------------
A:int
B:bool
C:str
D:float
E:str
```

```
5下列是年齡計算程式，請問程式中變數的資料型別為何？請填入下列型別 bool、float、int、str：

01 born = input("請輸入出生的民國年： ")
02 year = input("請輸入現在的民國年： ")
03 age = eval(year) - eval(born)
04 msg = "你的年齡是： " + str(age)
05 print(msg)

A: 在 01 行中 born 的資料型別為何？
B: 在 03 行中 age 的資料型別為何？
C: 在 04 行中 msg 的資料型別為何？

---------------------------
A:str
B:int
C:str
```

```
6下列程式碼執行後，變數的資料型別是否正確，請填入 是 、 否。

01 x1 = '5'
02 y1 = 4
03 a = x1 * y1  
04 x2, y2 = 6, 3   05 b = x2 / y2
06 x3, y3 = 1.0, 2
07 c = x3 + y3

A：_________變數 a 的資料類型為 str。
B：_________變數 b 的資料類型是 float。
C：_________變數 c 的資料類型為 int。 

----------------------
A:是
B:是
C:否
```


```
7下列常值請用bool、float、int、str填入正確的資料型別：

A：______type(+5E10)
B：______type(4.0)
C：______type("False")
D：______type(True)

-----------------------------
A:float
B:float
C:str
D:bool
```

```
8下列程式碼是用來以座號查詢學生姓名，但執行結果並不正確，請回答下列問題，來找出可能的錯誤。

01 datas = {1: '張三', 2: '李四', 3: '王五'}
02 num = input('請輸入座號: ')
03 if not num in datas:
04     print('該座號不存在！')
05 else:
06     print("學生姓名為： " + datas[num])

A：第01 行敘述的datas 字典中，儲存哪兩種資料類型？
① string、bool    ② float、string   ③ int、string      ④ int、float

B：第 02 行敘述的 num 變數的資料型別為何？
① bool    ② float     ③ int   ④ string   

C：第 03 行敘述執行時，為何在 datas 字典中找不到資料?  ① 程式邏輯錯誤    ② 資料型別不匹配     ③ 變數名稱誤用保留字   ④ 語法不正確

----------------------------
A:③ 
B:④
C:②
```

```
9下列是用來查詢傳入值資料型別的函式，請根據執行結果回答下列問題

01 def dataType(val):
02      return type(val)
03 print(dataType(False))
04 print(dataType(3.0))
05 print(dataType(3))
06 print(dataType("False"))

A：第03 行敘述的執行結果為何？
① <class'bool'>    ② <class'float'>    ③ <class'int'>      ④ <class'str'>

B：第04 行敘述的執行結果為何？
① <class'bool'>    ② <class'float'>    ③ <class'int'>      ④ <class'str'>

C：第05 行敘述的執行結果為何？
① <class'bool'>    ② <class'float'>    ③ <class'int'>      ④ <class'str'>

D：第06 行敘述的執行結果為何？
① <class'bool'>    ② <class'float'>    ③ <class'int'>      ④ <class'str'>

---------------------------
A:①
B:②
C:③
D:④
```

```
10讓使用者輸入一個整數值，但即使輸入小數也能轉換為整數，請問下列哪個敘述符合要求？

① num = input("請輸入整數：")
② num = int((input("請輸入整數："))
③ num = float(input("請輸入整數："))
④ num = str(input("請輸入整數："))

-------------------------------
②
```

