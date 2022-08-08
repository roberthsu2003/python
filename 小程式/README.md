# 小遊戲

### 畢氏定理

```python
import cmath
對邊 = int(input("請輸入對邊:"))
鄰邊 = int(input("請輸入鄰邊:"))
斜邊 = cmath.sqrt(對邊 ** 2 + 鄰邊 ** 2)
print("斜邊=",斜邊.real)
```

### 畢氏定理
```python
import cmath
對邊 = int(input("請輸入對邊:"))
斜邊 = int(input("請輸入斜邊:"))
鄰邊 = cmath.sqrt(斜邊 ** 2 - 對邊 ** 2)
print("鄰邊=",鄰邊.real)
```


### 三角函數計算角度(對邊,斜邊)
```python
import cmath
對邊 = int(input("請輸入對邊:"))
斜邊 = int(input("請輸入斜邊:"))
角度 = cmath.asin(對邊 / 斜邊) * 180 / cmath.pi
print("角度:",角度.real)
```

### 三角函數計算角度(角度,斜邊)

```python
import cmath
角度 = int(input("請輸入角度:"))
斜邊 = int(input("請輸入斜邊:"))
對邊 = cmath.sin(角度/180*cmath.pi) * 斜邊
print("對邊:",對邊.real)
```

### 

```python
import random
first = random.randint(1,100)
second = random.randint(1,100)
answer = float(input(f"{first}+{second}="))

if answer == (first + second):
  print("恭喜!答對了")
else:
  print("您錯了!")
  print(f"答案是{first+second}")
```


### 
```python
import random
first = random.randint(1,100)
second = random.randint(1,100)
answer = float(input(f"{first}*{second}="))

if answer == (first * second):
  print("恭喜!答對了")
else:
  print("您錯了!")
  print(f"答案是{first*second}")
```

### 
```python
import random
min = 1
max = 100
count = 0

target = random.randint(1, 100)
#print(target)

print("============猜數字遊戲===================\n\n")
while(True):
  keyin = int(input(f"猜數字的範圍{min}~{max}:"))
  count += 1
  if keyin >= min and keyin <= max:
    if keyin == target:
      print("您答對了")
      print(f"您猜了{count}次")
      break
    elif (keyin > target):
      print("再小一點")
      max = keyin
    elif(keyin < target):
      print("再大一點")
      min = keyin
    print(f"您猜了{count}次")
  else:
    print("請輸入提示範圍內的數字")

```

### 

```python
from IPython.display import clear_output
import random

玩家1 = []
name1 = input("請輸入玩家1的姓名:")
玩家1.append(name1)
print(玩家1)

玩家2 = []
name2 = input("請輸入玩家2的姓名:")
玩家2.append(name2)
print(玩家2)
for i in range(1,6):
  手示1=int(input(f"{玩家1[0]},請出第{i}次手示:(1:剪刀,2:石頭,3:布)"))
  玩家1.append(手示1)
clear_output()

for i in range(1,6):
  手示2=int(input(f"{玩家2[0]},請出第{i}次手示:(1:剪刀,2:石頭,3:布)"))
  玩家2.append(手示2)
clear_output()

print(玩家1)
print(玩家2)

結果 = []

for i in range(1,6):
  手示1 = 玩家1[i]
  手示2 = 玩家2[i]

  if(手示1==1):
    if(手示2==1):
      結果.append("平手")
    elif(手示2==2):
      結果.append(玩家2[0])
    elif(手示2==3):
      結果.append(玩家1[0])

  elif(手示1==2):
    if(手示2==1):
      結果.append(玩家1[0])
    elif(手示2==2):
      結果.append("平手")
    elif(手示2==3):
      結果.append(玩家2[0])
  elif(手示1==3):
    if(手示2==1):
      結果.append(玩家2[0])
    elif(手示2==2):
      結果.append(玩家1[0])
    elif(手示2==3):
      結果.append("平手")

print(結果)

玩家1贏次數=0
玩家2贏次數=0
平手次數=0
for item in 結果:
  if 玩家1[0] == item:
    玩家1贏次數 +=1;
  elif 玩家2[0] == item:
    玩家2贏次數 +=1;
  else:
    平手次數 += 1;

print(f"{玩家1[0]}贏次數:{玩家1贏次數}")
print(f"{玩家2[0]}贏次數:{玩家2贏次數}")
print(f"平手次數:{平手次數}")


```

```python
from IPython.display import clear_output
from time import sleep

current_index = 0
nums = 0
while True:  
  input("請執行:")
  clear_output()
  sleep(1)
  nums += 1
  value = random.randint(1,6)
  current_index += value
  if(current_index >= 49):
      break;
  while grid[current_index] != 0:
    current_index += grid[current_index]
    
  print(current_index)

print("過關")
print(f"您使用了次數:{nums}")
```

```python
#骰子
import random
from IPython.display import clear_output
from time import sleep

def dice():
  x1=random.randint(1,6)
  x2=random.randint(1,6)
  x3=random.randint(1,6)
  x4=random.randint(1,6)
  print(x1,x2,x3,x4)
  scores=0

  #4骰子一樣
  if(x1==x2==x3==x4):
    scores=(x1+x2+x3+x4)*10

  elif(x1==x2==x3) or (x1==x2==x4) or (x2==x3==x4) or (x1==x3==x4):
    return None

  elif(x1==x2):
    if(x3 == x4):
      scores = max(x1+x2,x3+x4) 
    else:
      scores=x3+x4

  elif(x3==x4):
    if(x1 == x2):
      scores = max(x1+x2,x3+x4) 
    else:
      scores=x1+x2
    
  elif(x1==x3):
    if(x2 == x4):
      scores = max(x1+x3,x2+x4) 
    else:
      scores=x2+x4

  elif(x1==x4):
    if(x2 == x3):
      scores = max(x1+x4,x2+x3) 
    else:
      scores=x2+x3

  elif(x4==x2):
    if(x1 == x3):
      scores = max(x1+x3,x2+x4) 
    else:
      scores=x1+x3

  elif(x3==x2):
    if(x1 == x4):
      scores = max(x2+x3,x1+x4) 
    else:
      scores=x1+x4
  else:  
    return None

  return scores

def playGame():
  bet = eval(input("本次賭金為:"))
  input("請play1擲骰子:")
  play1 = dice()
  while play1 is None:
    input("請重新擲骰子:")
    play1 = dice()

  print(f"玩家1的分數是:{play1}\n\n")

  input("請play2擲骰子:")
  play2 = dice()
  while play2 is None:
    input("請重新擲骰子:")
    play2 = dice()

  print(f"玩家2的分數是:{play2}\n\n")

  if play1 == play2:
    print("平手")
  elif play1 > play2:
    print("玩家1:贏")
    marker[0] += bet

  else:
    print("玩家2:贏")
    marker[1] += bet

marker = [0,0]


while True:
  playGame()
  play_again = input("還繼續遊戲嗎?(y,n):")
  if play_again == 'n':
    break
  else:
    clear_output()
    sleep(1)


print("遊戲結束")
print(f"玩家1所得金額為:{marker[0]}")
print(f"玩家2所得金額為:{marker[1]}")

```