#角度求弳度
import math
pi = 3.141592653
angle = eval(input("請輸入角度:"))
radian = pi/180 * angle
print(f"角度:{angle},弳度為:{radian}")
print(f"sin({angle}度)={math.sin(radian):.2f}")






#角度,半徑,求對角長度

import math
#pi = 3.141592653
angle = eval(input("請輸入角度:"))
radius = eval(input("請輸入半徑:"))
radian = math.pi/180 * angle
print(f"角度:{angle},弳度為:{radian}")
print(f"sin({angle}度)={math.sin(radian):.2f}")
print(f"對角高度為:{math.sin(radian) * radius:.2f}")
