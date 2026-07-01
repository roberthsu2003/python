# 字串的處理 (String Processing)

字串（String）是 Python 中最常用的資料類型之一。舉凡網頁文字、使用者輸入、資料庫記錄，或是檔案路徑，都是以字串的形式在程式中傳遞。本單元將帶您由淺入深掌握字串的表示、基本運算、切片、搜尋取代、對齊排版，以及輸入驗證等核心技巧。

---

## 1. 字串表示與基礎概念

在 Python 中，字串是不可變的（Immutable）字元序列，可以使用單引號或雙引號建立。

### 1.1 字串宣告與引號表示式
當字串內部本身含有單引號（例如英文縮寫 `'s`）時，外層可以使用雙引號宣告；反之亦然，這能避免 Python 語法解析錯誤。
```python
# 1. 外層使用雙引號，內部便可直接使用單引號
words1 = "那是愛麗絲的貓。"
print(words1)  # 輸出: 那是愛麗絲的貓。

# 2. 外層使用單引號，內部若有單引號會導致語法解析錯誤
# words2 = 'That is Alice's cat.'  # ❌ 語法錯誤 (SyntaxError)
```

### 1.2 脫逸字元 (Escape Characters)
如果必須在單引號字串中置入單引號，或在雙引號字串中置入雙引號，可以使用反斜線（`\`）作為**脫逸字元**。
```markdown
\'  -> 單引號
\"  -> 雙引號
\n  -> 換行
\t  -> Tab 鍵縮排
\\  -> 反斜線
```

#### 📝 程式碼範例：
```python
print("哈囉，大家好！\n你好嗎？\n我過得很好。")
# 輸出結果：
# 哈囉，大家好！
# 你好嗎？
# 我過得很好。
```

### 1.3 原始字串 (Raw Strings)
如果在字串前面加上字母 `r` 或 `R`，該字串就會被視為**原始字串**。原始字串會忽略所有的脫逸字元，直接將反斜線當成一般字元印出，這在設計「正則表達式」或「Windows 檔案路徑」時非常實用。
```python
print(r'That is Carol\'s cat.')
# 輸出結果： That is Carol\'s cat.
```

### 1.4 單行折行與多行文字
* **單行折行**：當一行程式碼過長時，可以在行末加上反斜線 `\` 進行折行，但輸出時依然是一整行單行文字。
```python
sentence = "親愛的愛麗絲，\
伊芙的貓因為綁架貓、入室盜竊和敲詐勒索而被逮捕了。\
Sincerely，\
鮑伯"

print(sentence)
# 輸出結果： 親愛的愛麗絲，伊芙的貓因為綁架貓、入室盜竊和敲詐勒索而被逮捕了。Sincerely，鮑伯
```

* **多行文字**：使用三個單引號（`'''`）或三個雙引號（`"""`）包覆字串，可以完整保留字串內的換行與格式。
```python
multiline = '''親愛的愛麗絲，
伊芙的貓因為綁架貓、入室盜竊和敲詐勒索而被逮捕了。
Sincerely，
鮑伯'''

print(multiline)
# 輸出結果會保留完整的四行格式。
```

* **多行文字當作註解**：在 Python 中，若三引號字串沒有指派給任何變數，通常會被當作「多行註解（Docstring）」使用。
```python
"""
這是一段多行說明註解。
本程式是由羅伯特撰寫，電子信箱為 robert@gmail.com。
本程式是為 Python 3 設計，非 Python 2。
"""
```

### 1.5 計算字元數：`len()`
使用內建的 `len()` 函數可以取得字串的總字元長度（包含空格、標點符號與脫逸字元）。
```python
letters = 'abcdefghijklmnopqrstuvwxyz'
print(len(letters))  # 輸出: 26

empty = ""
print(len(empty))    # 輸出: 0
```

### 1.6 字串基礎運算子
* **加號 `+` 拼接**：將兩個字串串接在一起（注意：非字串資料必須先以 `str()` 轉型）。
```python
name = '羅伯特'
age = 40
info = '哈囉，我的名字是 ' + name + '。我今年 ' + str(age) + ' 歲。'
print(info)
# 輸出: 哈囉，我的名字是 羅伯特。我今年 40 歲。
```
* **`in` 與 `not in` 成員運算子**：判斷某個子字串是否存在於目標字串中，回傳布林值（`True` / `False`）。
```python
print('哈囉' in '哈囉，世界')  # 輸出: True
print('哈囉' in '哈羅')      # 輸出: False (字元不同)
print('' in '你好')          # 輸出: True (空字串永遠為真)
```

---

## 2. 字串的索引與切片 (Indexing & Slicing)

### 2.1 字元索引
字串中的每一個字元都有其對應的編號，稱為**索引 (Index)**：
* **正向索引**：由左向右，從 `0` 開始遞增。
* **反向索引**：由右向左，從 `-1` 開始遞減。

| 索引取值示意表 | H | e | l | l | o |   | W | o | r | l | d |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **正向索引 (Index)** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| **反向索引 (Index)** | -11 | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

```python
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])   # 'a'
print(letters[-1])  # 'z'
print(letters[25])  # 'z'

# ❌ 超出範圍會引發 IndexError
# print(letters[100])  # IndexError: string index out of range

# ❌ 字串是 Immutable (不可變的)，無法直接修改其中字元
name = 'Henny'
# name[0] = 'P'  # TypeError: 'str' object does not support item assignment
```

### 2.2 字串的切片 slice
切片語法可以讓我們從一個字串中擷取出子字串。
* **語法**：`字串[start:end:step]`
  - `start`：起始索引（包含），預設為 0。
  - `end`：結束索引（**不包含**），預設為字串結尾。
  - `step`：步長（每次跳越的間隔），預設為 1。如果步長為負數，代表**由右向左反向讀取**。

```python
letters = 'abcdefghijklmnopqrstuvwxyz'

print(letters[:])        # 輸出完整字串: 'abcdefghijklmnopqrstuvwxyz'
print(letters[20:])      # 從索引 20 到最後: 'uvwxyz'
print(letters[12:15])    # 索引 12 到 14: 'mno'
print(letters[-3:])      # 倒數 3 個字元: 'xyz'
print(letters[18:-3])    # 索引 18 到 倒數第 4 個: 'stuvw'
print(letters[::7])      # 每隔 7 個字元取一個: 'ahov'
print(letters[4:20:3])   # 索引 4 到 19，每隔 3 個字元取一個: 'ehknqt'
print(letters[::-1])     # **字串反轉技巧**: 'zyxwvutsrqponmlkjihgfedcba'
```

#### 🧠 自我檢驗小測驗：
> **Q1. 設 `myString = "Hello World"`，請問 `myString[1:4]` 的輸出結果為何？**  
> (1) `Hell`  
> (2) `ell`  
> (3) `llo`  
>
> **Q2. 請問 `myString[:3]` 的輸出結果為何？**  
> (1) `Hel`  
> (2) `ell`  
> (3) `Hello`  

---

## 3. 字串內容搜尋與取代 (Search & Replace)

### 3.1 `find()` 與 `rfind()` 搜尋位置
* **語法**：`字串.find(sub_str, start, end)`
  - 搜尋子字串 `sub_str` 出現的**第一個正向索引位置**（從 0 開始）。
  - 可以指定 `start` (起始搜尋位置) 與 `end` (結束搜尋位置，不包含)。
  - 若**搜尋不到，會回傳 `-1`**。
* `rfind()`：如同 `find()`，但它是由右向左搜尋，回傳子字串最後一次出現的索引位置。

```python
sentence = "this is Python Tutorial, there"

print(sentence.find("Python"))       # 輸出: 8
print(sentence.find("not"))          # 輸出: -1 (搜尋不到)
print(sentence.find("t"))            # 輸出: 0 (第一個字母)
print(sentence.find("t", 4))         # 輸出: 10 (從索引 4 開始往後找的第一個 't')
print(sentence.find("t", 11, 20))    # 輸出: 17 (在索引 11 到 19 之間搜尋)
print(sentence.rfind("the"))         # 輸出: 25 (由右側開始算起最後一次出現 'the' 的位置)
```

### 3.2 `replace()` 取代文字
* **語法**：`字串.replace(old, new, max_replace)`
  - 將字串中的舊子字串 `old` 替換為新子字串 `new`。
  - `max_replace`：可選參數，指定最多替換幾次。

```python
str1 = "This is Python, That is Java; This is SQLite, That is MySQL"

# 1. 替換全部的 "is"
print(str1.replace("is", "-"))
# 輸出: Th- - Python, That - Java; Th- - SQLite, That - MySQL

# 2. 僅替換前 2 個遇到的 "is"
print(str1.replace("is", "-", 2))
# 輸出: Th- - Python, That is Java; This is SQLite, That is MySQL
```

### 3.3 `startswith()`, `endswith()`, `count()` 狀態判定
* `startswith(prefix)`：檢查字串是否以 `prefix` 開頭，回傳布林值。
* `endswith(suffix)`：檢查字串是否以 `suffix` 結尾，回傳布林值。
* `count(sub_str)`：計算子字串 `sub_str` 在整個字串中出現的總次數。

```python
poem = "All that doth flow we cannot liquid name..."
print(poem.startswith('All'))  # 輸出: True
print(poem.endswith('folks!'))  # 輸出: False
print(poem.count('that'))       # 輸出: 2
```

---

## 4. 字串連接與分割 (Join & Split)

### 4.1 `split()`：將字串切割成 List
* **語法**：`字串.split(delimiter, max_split)`
  - 以指定的分隔符號 `delimiter` 將字串切開，存入一個 List（串列）中。
  - 預設分隔符號為所有的空白字元（包含空格、Tab、換行）。

```python
# 1. 以逗號分割
todos = '買手套,買口罩,給貓吃維他命,叫救護車'
print(todos.split(','))
# 輸出: ['買手套', '買口罩', '給貓吃維他命', '叫救護車']

# 2. 以橫線分割
str4 = "python-java-c++-ruby"
print(str4.split('-'))
# 輸出: ['python', 'java', 'c++', 'ruby']
```

### 4.2 `join()`：以特定字元連接序列
* **語法**：`連接符號.join(sequence)`
  - 將 List、Tuple 或字串序列中的各元素以「連接符號」串接成一個全新的字串。

```python
# 1. 以橫線連接 Tuple 元素
str1 = "-"
str2 = ("a", "b", "c")
print(str1.join(str2))  # 輸出: a-b-c

# 2. 將 List 串接成段落 (繁中化範例)
crypto_list = ['雪人', '大腳怪', '尼斯湖水怪']
crypto_string = ', '.join(crypto_list)
print('發現並簽約的神秘生物專題:', crypto_string)
# 輸出: 發現並簽約的神秘生物專題: 雪人, 大腳怪, 尼斯湖水怪

# 3. 將字串中每個字元插入冒號
print(":".join("Python"))  # 輸出: P:y:t:h:o:n
```

---

### 💡 實戰範例：文字接龍小遊戲
結合字串輸入、`for` 迴圈迭代、索引取值以及 `join()` 拼接，實作一個文字接龍遊戲。若輸入的首字元與上一次接龍的指定尾字元不符，遊戲即結束：
```python
# wordLink.py
print('失敗就會退出遊戲!')
inputString = input('請輸入起始字串: ')
sampleString = '接龍開始'

for single in sampleString:
    print('當前累計字串:', inputString)
    outputWords = f"請輸入以 - {single} - 開始的字串: "
    keyin = input(outputWords)
    
    # 檢查輸入字串的首字是否與指定字元相符
    if keyin[0] != single:
        print('遊戲失敗！首字不相符。')
        print('您最終的接龍字串是:', inputString)
        break
    inputString += '-' + keyin
else:
    print('恭喜! 成功完成文字接龍遊戲！')
    print('完整字串是:', inputString)
```

---

## 5. 字串操控與輸入檢查 (Formatting & Validation)

### 5.1 字串大小寫與符號修飾
* `strip(chars)`：移除字串首尾的指定字元（預設為首尾所有空格與換行）。
* `capitalize()`：將字串第一個英文字母轉大寫，其餘轉小寫。
* `title()`：將字串中每個單字的首字母轉大寫。
* `upper()` / `lower()`：字串全部轉大寫 / 全部轉小寫。
* `swapcase()`：大小寫反轉。

> [!NOTE]
> 這些大小寫轉換方法是專為英文字母設計的。如果處理的是繁體中文字串，這些大小寫方法不會改變中文內容。因此以下我們使用英文字串進行展示：

```python
setup = 'a duck goes into a bar...'

print(setup.strip('.'))       # 移除首尾句點: 'a duck goes into a bar'
print(setup.capitalize())     # 首字大寫: 'A duck goes into a bar...'
print(setup.title())          # 每個單字首字大寫: 'A Duck Goes Into A Bar...'
print(setup.upper())          # 全大寫: 'A DUCK GOES INTO A BAR...'
print(setup.swapcase())       # 大小寫互換: 'A DUCK GOES INTO A BAR...'
```

### 5.2 文字對齊方法
`rjust()`, `ljust()`, 與 `center()` 分別用於將字串靠右、靠左、居中對齊，並可設定填充字元。
```python
print('Hello'.rjust(10))        # 靠右對齊，寬度 10 (預設補空白): '     Hello'
print('Hello'.rjust(20, '*'))   # 靠右對齊，寬度 20，補星號: '***************Hello'
print('Hello'.ljust(20, '-'))   # 靠左對齊，寬度 20，補橫線: 'Hello---------------'
print('Hello'.center(20, '='))  # 居中對齊，寬度 20，補等號: '=======Hello========'
```

#### 💡 操作範例：野餐食物清單印出並輸出為文字檔
此範例使用 `ljust()` 與 `rjust()` 格式化輸出字典內容，並使用 `with open` 將輸出格式同步寫入到一個 `.txt` 文字檔中：
```python
def generate_picnic_report(itemsDict, leftWidth, rightWidth, filename="picnic.txt"):
    lines = []
    # 居中對齊標題
    header = '野餐食物清單'.center(leftWidth + rightWidth, '-')
    lines.append(header)
    
    for k, v in itemsDict.items():
        # 以特定點符號對齊
        line = k.ljust(leftWidth, '.') + str(v).rjust(rightWidth)
        lines.append(line)
        
    # 印出至螢幕
    for line in lines:
        print(line)
        
    # 輸出寫入為實體文字檔
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"\n報告已成功儲存至 {filename}")

picnicItems = {'三明治': 4, '蘋果': 12, '杯子': 4, '餅乾': 8000}
generate_picnic_report(picnicItems, 20, 6)
```

---

### 5.3 字串狀態檢查 `isX()` 方法
我們常需要確認使用者輸入的內容是否完全符合某種類型（如純數字、純英文字母）：
* `isalpha()`：若字串「只包含英文字母」且不為空值，則回傳 `True` (不可有空白、數字)。
* `isalnum()`：若字串「只包含英文字母或數字」且不為空值，則回傳 `True` (不可有空白)。
* `isdecimal()`：若字串「只包含 0-9 數字」且不為空值，則回傳 `True` (可用於整數轉換前防錯)。
* `isspace()`：若字串「只包含空白字元」（空格、Tab、換行），則回傳 `True`。
* `istitle()`：若字串內所有單字皆符合首字母大寫的規則，則回傳 `True`。

```python
print('hello123'.isalpha())   # False (含數字)
print('hello123'.isalnum())   # True  (英數混合)
print('123'.isdecimal())      # True  (純數字)
print(' '.isspace())          # True  (純空白)
print('This Is Title'.istitle())  # True
```

---

### 5.4 輸入欄位驗證應用

#### 💡 操作範例 1：年齡與密碼合法性檢查
使用 `while True` 無限迴圈接收輸入，並使用 `isdecimal()` 與 `isalnum()` 做防錯攔截，直到輸入正確才允許結束：
```python
# 欄位防錯驗證
while True:
    age = input('請輸入年齡: ')
    if age.isdecimal():
        break
    print('錯誤：請輸入有效的數字！\n')

while True:
    password = input('請輸入密碼 (限制只能是英文字母或數字): ')
    if password.isalnum():
        break
    print('錯誤：密碼不允許特殊字元或空白！\n')

print(f"年齡登錄成功: {age}")
print(f"密碼設定成功: {password}")
```

#### 💡 操作範例 2：身分證字號格式驗證
引入正規表達式 `re.match` 快速檢驗身份證字號是否符合「首字大寫英文，後接 9 碼數字」的結構：
```python
# taiwanId.py
import re

taiwanId = input('請輸入身份證字號: ').strip()
# 使用 re.I 忽略英文大小寫
mobj = re.match(r'^[A-Z]\d{9}$', taiwanId, re.I)

if mobj:
    print(f"身分證字號 {taiwanId} 結構格式正確")
else:
    print(f"身分證字號 {taiwanId} 格式有誤！必須為1碼英文字母 + 9碼數字。")
```

#### 💡 操作範例 3：多筆 Email 格式提取
使用 `re.findall` 在使用者輸入的一長串凌亂文字中，精準過濾並取出所有合法的 Email 地址：
```python
# email.py
import re

emails_input = input('請輸入包含多筆 Email 的文字:\n')
# 正規表達式比對 Email 結構
getEmails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', emails_input)

print('\n成功取出的 Email 列表有:')
for email in getEmails:
    print(email)
```

---

## 6. 綜合練習與挑戰

### 6.1 多行文字格式轉換 (自動加前綴)
將一整段多行文字的每一行首端加上 `*`（清單符號）或數字序號：
```python
raw_text = """動物清單
水族生物清單
作者簡稱的羅伯特清單
栽培品種清單"""

# 1. 轉變為項目符號清單
lines = raw_text.split('\n')
bullet_lines = [f"* {line}" for line in lines]
print('\n'.join(bullet_lines))
# 輸出:
# * 動物清單
# * 水族生物清單
# ...

# 2. 轉變為數字編號清單
numbered_lines = [f"{i+1}. {line}" for i, line in enumerate(lines)]
print('\n'.join(numbered_lines))
# 輸出:
# 1. 動物清單
# 2. 水族生物清單
# ...
```

### 6.2 二維列表轉置與對齊排版
給予一個包含多個 List 的二維矩陣，將其進行行列互換（轉置），並以右對齊格式整齊印出：
```python
tableData = [
    ['蘋果', '橘子', '櫻桃', '香蕉'],
    ['愛麗絲', '鮑伯', '卡蘿', '大衛'],
    ['狗狗', '貓咪', '駝鹿', '鵝']
]

# 計算每一列（原 tableData 的每一行）的最大字元寬度
# 注意：在包含中文字元時，由於中文是全形字元，其實際顯示寬度約為半形英文字元的兩倍。
# 此範例採用簡單的 max() 長度計算來示範轉置邏輯：
colWidths = [0] * len(tableData)
for i in range(len(tableData)):
    colWidths[i] = max(len(item) for item in tableData[i])

# 行列轉置並格式化輸出
# 外層迴圈代表行數 (4行)，內層迴圈代表列數 (3列)
for x in range(len(tableData[0])):
    for y in range(len(tableData)):
        # 以該列最大寬度靠右對齊
        print(tableData[y][x].rjust(colWidths[y] + 2), end='')
    print()

# 輸出結果：
#    蘋果  愛麗絲    狗狗
#    橘子    鮑伯    貓咪
#    櫻桃    卡蘿    駝鹿
#    香蕉    大衛      鵝
```

---

### 🧠 小測驗解答：
* **Q1**：`(2) ell` —— 切片 `myString[1:4]` 包含索引 1, 2, 3，不包含 4。即 'H(0) e(1) l(2) l(3) o(4)' 擷取出 'ell'。
* **Q2**：`(1) Hel` —— `myString[:3]` 代表從頭開始擷取到索引 3 之前（即索引 0, 1, 2），輸出 'Hel'。
