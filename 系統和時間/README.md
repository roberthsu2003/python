# Python 系統操作與時間處理

Python 透過內建的 `os`、`shutil`、`datetime` 和 `time` 等模組，讓我們可以輕鬆地操作檔案系統、管理目錄路徑，以及處理日期與時間資料。本章由淺入深，逐步掌握這些實用的系統層級操作技能。

---

## 1. 檔案操作（`os` 模組）

`os` 模組提供了一組與作業系統互動的介面，讓 Python 程式可以跨平台地操作檔案與路徑。

### 1.1 建立與寫入檔案

```python
import os

# 建立並寫入一個文字檔
fout = open('memo.txt', 'wt', encoding='UTF-8')
print('這是一個備忘錄檔案。', file=fout)
fout.close()
```

### 1.2 檢查路徑與檔案狀態

```python
import os

# 檢查路徑是否存在（檔案或目錄皆可）
print(os.path.exists('memo.txt'))    # True
print(os.path.exists('no_file.txt')) # False

# 判斷是否為檔案
print(os.path.isfile('memo.txt'))    # True

# 判斷是否為目錄
print(os.path.isdir('memo.txt'))     # False
print(os.path.isdir('.'))            # True（目前目錄）

# 取得絕對路徑
print(os.path.abspath('memo.txt'))   # /Users/.../memo.txt
```

### 1.3 複製、重新命名與刪除

```python
import os
import shutil

# 複製檔案
shutil.copy('memo.txt', 'memo_backup.txt')

# 移動或重新命名
os.rename('memo_backup.txt', 'memo_v2.txt')

# 刪除檔案
os.remove('memo_v2.txt')
print(os.path.exists('memo_v2.txt'))  # False
```

### 💡 實戰生活主題範例：安全寫入並驗證設定檔
> **為什麼此場景需要 `os` 模組？**  
> 在程式初始化時，我們需要確認設定檔是否存在，若不存在則自動建立；
> 若已存在則顯示其路徑。這是許多實際應用程式常見的啟動流程。
```python
import os

CONFIG_FILE = 'app_config.txt'

def ensure_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"【初始化】找不到設定檔，正在建立 '{CONFIG_FILE}'...")
        with open(CONFIG_FILE, 'wt', encoding='UTF-8') as f:
            f.write("language=zh-TW\n")
            f.write("theme=dark\n")
            f.write("font_size=14\n")
        print("設定檔建立完成！")
    else:
        abs_path = os.path.abspath(CONFIG_FILE)
        print(f"【載入中】設定檔已存在：{abs_path}")

ensure_config()
```
##### 🖥️ 終端機預期輸出結果（第一次執行）：
```text
【初始化】找不到設定檔，正在建立 'app_config.txt'...
設定檔建立完成！
```

---

## 2. 目錄操作（`os` 模組）

### 2.1 建立與刪除目錄

```python
import os

# 建立單層目錄
os.mkdir('reports')
print(os.path.exists('reports'))  # True

# 建立多層目錄（makedirs 可一次建立巢狀目錄）
os.makedirs('data/2025/january', exist_ok=True)

# 刪除空目錄
os.rmdir('reports')
```

### 2.2 列出與切換目錄

```python
import os

# 列出指定目錄內的所有檔案與子目錄名稱
contents = os.listdir('.')
print(contents)

# 取得目前工作目錄
print(os.getcwd())

# 切換工作目錄
os.chdir('..')
print(os.getcwd())  # 上一層目錄
```

### 2.3 遍歷整個目錄樹（`os.walk`）

```python
import os

# os.walk 可遞迴遍歷所有子目錄
for dirpath, dirnames, filenames in os.walk('.'):
    print(f"目錄：{dirpath}")
    for filename in filenames:
        print(f"  └─ {filename}")
```

### 💡 實戰生活主題範例：整理下載資料夾（依副檔名分類）
> **為什麼此場景需要目錄操作？**  
> 下載資料夾經常混雜著圖片、文件和程式碼。透過 `os.listdir()` 和 `shutil.move()`，
> 可以自動掃描目前目錄並依副檔名將檔案分類移入對應子資料夾，省去手動整理的時間。
```python
import os
import shutil

# 副檔名對應的分類資料夾
CATEGORY_MAP = {
    '.jpg': 'images', '.jpeg': 'images', '.png': 'images',
    '.pdf': 'documents', '.docx': 'documents', '.txt': 'documents',
    '.py': 'scripts', '.ipynb': 'scripts',
}

def organize_folder(target_dir='.'):
    for filename in os.listdir(target_dir):
        # 跳過目錄本身
        if os.path.isdir(os.path.join(target_dir, filename)):
            continue

        ext = os.path.splitext(filename)[1].lower()
        folder = CATEGORY_MAP.get(ext, 'others')
        dest_dir = os.path.join(target_dir, folder)

        # 若分類資料夾不存在則建立
        os.makedirs(dest_dir, exist_ok=True)

        src = os.path.join(target_dir, filename)
        dst = os.path.join(dest_dir, filename)
        shutil.move(src, dst)
        print(f"已移動：{filename}  →  {folder}/")

# organize_folder('.')  # 執行整理
print("目錄整理完成！")
```

---

## 3. 日期與時間（`datetime` 模組）

`datetime` 模組是 Python 處理日期與時間的核心工具，提供四個主要類別：

| 類別 | 用途 | 範例 |
| :--- | :--- | :--- |
| `date` | 年、月、日 | `date(2025, 7, 1)` |
| `time` | 時、分、秒、微秒 | `time(14, 30, 0)` |
| `datetime` | 年月日＋時分秒 | `datetime(2025, 7, 1, 14, 30)` |
| `timedelta` | 一段時間間隔 | `timedelta(days=7)` |

### 3.1 建立日期物件

```python
from datetime import date

# 建立指定日期
birthday = date(2000, 5, 20)
print(birthday)            # 2000-05-20
print(birthday.year)       # 2000
print(birthday.month)      # 5
print(birthday.day)        # 20
print(birthday.isoformat()) # '2000-05-20'

# 取得今天日期
today = date.today()
print(today)  # 2025-07-01（依當日而定）
```

### 3.2 使用 `timedelta` 計算日期差

```python
from datetime import date, timedelta

today = date.today()
one_day = timedelta(days=1)

tomorrow  = today + one_day
yesterday = today - one_day
next_week = today + timedelta(weeks=1)

print(f"昨天：{yesterday}")
print(f"今天：{today}")
print(f"明天：{tomorrow}")
print(f"下週：{next_week}")

# 兩個日期相差幾天
delta = date(2025, 12, 31) - today
print(f"距離年底還有 {delta.days} 天")
```

### 3.3 建立時間物件

```python
from datetime import time

noon = time(12, 0, 0)
print(noon.hour)    # 12
print(noon.minute)  # 0
print(noon.second)  # 0
```

### 3.4 `datetime`：日期與時間的組合

```python
from datetime import datetime

# 取得現在的日期和時間
now = datetime.now()
print(now)            # 2025-07-01 14:32:05.123456
print(now.year)       # 2025
print(now.hour)       # 14
print(now.minute)     # 32

# 從 datetime 分別取出日期和時間
print(now.date())     # 2025-07-01
print(now.time())     # 14:32:05.123456
```

### 💡 實戰生活主題範例：生日倒數計時器
> **為什麼此場景需要 `datetime`？**  
> `timedelta` 可以直接計算兩個日期之間的差值，讓我們輕鬆得知距離生日還有幾天、
> 今年幾歲，以及生日是星期幾，而不需要自行處理跨月、跨年的複雜邏輯。
```python
from datetime import date

def birthday_countdown(birth_year: int, birth_month: int, birth_day: int):
    today = date.today()
    birthday_this_year = date(today.year, birth_month, birth_day)

    # 若今年生日已過，計算明年的
    if birthday_this_year < today:
        birthday_this_year = date(today.year + 1, birth_month, birth_day)

    days_left = (birthday_this_year - today).days
    age = today.year - birth_year - (
        1 if (today.month, today.day) < (birth_month, birth_day) else 0
    )

    weekday_names = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    birthday_weekday = weekday_names[birthday_this_year.weekday()]

    print(f"今天日期：{today}")
    print(f"今年（或明年）生日：{birthday_this_year}（{birthday_weekday}）")
    print(f"目前年齡：{age} 歲")
    print(f"距離下次生日還有：{days_left} 天")

birthday_countdown(2000, 10, 31)
```
##### 🖥️ 終端機預期輸出結果：
```text
今天日期：2025-07-01
今年（或明年）生日：2025-10-31（星期五）
目前年齡：24 歲
距離下次生日還有：122 天
```

---

## 4. 時間格式化與解析

### 4.1 `strftime()`：將日期/時間轉成字串

`strftime()` 是 `date`、`time`、`datetime` 物件的方法，可將物件格式化為自訂的字串格式。

#### 常用格式符號表

| 符號 | 說明 | 範例輸出 |
| :---: | :--- | :--- |
| `%Y` | 四位數西元年 | `2025` |
| `%m` | 月份（補零） | `07` |
| `%B` | 月份英文全名 | `July` |
| `%d` | 日（補零） | `01` |
| `%A` | 星期英文全名 | `Tuesday` |
| `%H` | 小時（24 小時制） | `14` |
| `%I` | 小時（12 小時制） | `02` |
| `%M` | 分鐘 | `30` |
| `%S` | 秒數 | `05` |
| `%p` | AM / PM | `PM` |

```python
from datetime import datetime

now = datetime.now()

# 轉成易讀的中文格式
fmt = "%Y 年 %m 月 %d 日 %H:%M:%S"
print(now.strftime(fmt))
# 輸出範例：2025 年 07 月 01 日 14:32:05

# ISO 8601 標準格式
print(now.strftime("%Y-%m-%dT%H:%M:%S"))
# 輸出範例：2025-07-01T14:32:05
```

### 4.2 `strptime()`：將字串解析為 `datetime` 物件

```python
from datetime import datetime

date_str = "2025-07-01 14:30:00"
fmt = "%Y-%m-%d %H:%M:%S"

dt_object = datetime.strptime(date_str, fmt)
print(dt_object)         # 2025-07-01 14:30:00
print(type(dt_object))   # <class 'datetime.datetime'>
print(dt_object.year)    # 2025
```

### 4.3 `time` 模組（Unix Timestamp）

`time` 模組提供的 `time()` 函式回傳的是從 **1970/1/1 00:00:00 UTC** 至今的秒數，常用於程式計時與效能測量。

```python
import time

# 取得目前的 Unix Timestamp
timestamp = time.time()
print(timestamp)  # 例如：1751376720.123

# 轉成可讀字串
print(time.ctime(timestamp))
# 輸出範例：Tue Jul  1 14:32:00 2025

# 轉成結構化的本地時間物件
local_t = time.localtime(timestamp)
print(local_t.tm_year)   # 2025
print(local_t.tm_hour)   # 14
```

> [!IMPORTANT]
> **儲存時間請使用 UTC；儲存字串請使用 UTF-8。**  
> 在多時區的應用系統中，始終以 UTC 時間存入資料庫，在顯示時再轉換為使用者的本地時區，可避免夏令時間（DST）等時區轉換錯誤。

### 💡 實戰生活主題範例：程式執行時間計量器
> **為什麼此場景需要 `time` 模組？**  
> 在比較不同演算法效能時，需要精確測量程式段的執行時間。
> `time.time()` 可在程式開始和結束各取一次 Timestamp，兩者相減即為執行耗時秒數。
```python
import time

def measure_time(func, *args, label=""):
    """計量並回報函式的執行耗時"""
    start = time.time()
    result = func(*args)
    elapsed = time.time() - start
    print(f"[{label or func.__name__}] 執行完成，耗時：{elapsed:.4f} 秒")
    return result

# 比較兩種求總和的方法
def sum_with_loop(n):
    total = 0
    for i in range(n):
        total += i
    return total

def sum_with_builtin(n):
    return sum(range(n))

N = 5_000_000
measure_time(sum_with_loop,    N, label="for 迴圈")
measure_time(sum_with_builtin, N, label="內建 sum()")
```
##### 🖥️ 終端機預期輸出結果：
```text
[for 迴圈]   執行完成，耗時：0.2451 秒
[內建 sum()] 執行完成，耗時：0.0623 秒
```

---

## 5. 常用指令速查表

### 5.1 `os` 模組常用指令

| 指令 | 用途 |
| :--- | :--- |
| `os.path.exists(path)` | 檢查路徑是否存在 |
| `os.path.isfile(path)` | 判斷是否為檔案 |
| `os.path.isdir(path)` | 判斷是否為目錄 |
| `os.path.abspath(path)` | 取得絕對路徑 |
| `os.path.splitext(name)` | 分離檔名與副檔名 |
| `os.mkdir(path)` | 建立單層目錄 |
| `os.makedirs(path, exist_ok=True)` | 建立多層巢狀目錄 |
| `os.rmdir(path)` | 刪除空目錄 |
| `os.listdir(path)` | 列出目錄內容 |
| `os.getcwd()` | 取得目前工作目錄 |
| `os.chdir(path)` | 切換工作目錄 |
| `os.remove(path)` | 刪除檔案 |
| `os.rename(src, dst)` | 重新命名或移動 |

### 5.2 `datetime` 模組常用指令

| 指令 | 用途 |
| :--- | :--- |
| `date.today()` | 取得今天日期 |
| `datetime.now()` | 取得現在日期時間 |
| `timedelta(days=N)` | 建立 N 天的時間間隔 |
| `dt.strftime(fmt)` | 日期物件 → 格式化字串 |
| `datetime.strptime(s, fmt)` | 字串 → datetime 物件 |
| `datetime.combine(date, time)` | 合併 date 與 time |
| `dt.date()` / `dt.time()` | 從 datetime 分拆出日期/時間 |
