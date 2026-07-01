# Python 課堂練習設計

## 今日教學重點

接收不定數量的引數:`*args` 與 `**kwargs`

---

# 課堂範例回顧(學生剛才已練習)

## 原始程式

```python
#*args 接收任意數量的位置引數
def print_args(required_item, *args):
    print("必填項目:", required_item)
    print("其他位置引數 Tuple:", args)

print_args("外套", "圍巾", "手套", "帽子")
# 輸出:
# 必填項目: 外套
# 其他位置引數 Tuple: ('圍巾', '手套', '帽子')


#**kwargs 接收任意數量的關鍵字引數
def print_kwargs(**kwargs):
    print("關鍵字引數 Dictionary:", kwargs)

print_kwargs(wine='紅酒', entree='牛排', dessert='蛋糕')
# 輸出:
# 關鍵字引數 Dictionary: {'wine': '紅酒', 'entree': '牛排', 'dessert': '蛋糕'}
```

## 使用的 Python 技術

- function 定義(def)
- `*args`(不定數量位置引數,打包成 Tuple)
- `**kwargs`(不定數量關鍵字引數,打包成 Dictionary)
- print() 輸出
- 函式呼叫時混用一般引數與多個額外引數

## 學習目標

學生可以學會:

- 理解 `*args` 會把多餘的位置引數自動打包成一個 Tuple
- 理解 `**kwargs` 會把多餘的關鍵字引數自動打包成一個 Dictionary
- 能自行設計 function,依情境選擇使用 `*args` 或 `**kwargs` 來接收不確定數量的資料

---

# 本次練習題目(全新題目,與課堂範例不同)

> 說明:以下是針對相同教學重點設計的「新題目」,情境與資料和課堂範例不同,但用到的 Python 語法一致。

## 題目敘述

請設計兩個 function:

1. `add_to_playlist(playlist_name, *args)`:第一個參數是必填的播放清單名稱,後面可以傳入任意數量的歌曲名稱(位置引數),要用 `*args` 打包成 Tuple,並印出「播放清單名稱」與「歌曲清單」。
2. `save_profile(**kwargs)`:接收任意數量的關鍵字引數,代表使用者的個人資料欄位(例如 `nickname`、`city`、`hobby` 等),要用 `**kwargs` 打包成 Dictionary,並印出整包個人資料。

分別呼叫這兩個 function 做測試:`add_to_playlist` 傳入一個播放清單名稱與至少 3 首歌;`save_profile` 傳入至少 3 個關鍵字引數。

## 與課堂範例的對應

- 沿用的語法/概念:`*args` 收集多餘位置引數成 Tuple、`**kwargs` 收集多餘關鍵字引數成 Dictionary、印出打包後的結果
- 換掉的部分:情境從「衣物清單、餐點訂購」換成「音樂播放清單、使用者個人資料」,參數名稱與資料內容不同

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。

```python
# 請完成:定義 add_to_playlist function,第一個參數是 playlist_name,
#         後面用 *args 接收任意數量的歌曲名稱
def add_to_playlist(playlist_name  ):
    print("播放清單名稱:", playlist_name)
    # 請完成:印出 "歌曲清單 Tuple:" 加上 args 的內容


# 請完成:定義 save_profile function,用 **kwargs 接收任意數量的關鍵字引數
def save_profile(  ):
    # 請完成:印出 "個人資料 Dictionary:" 加上 kwargs 的內容


# 請完成:呼叫 add_to_playlist,傳入播放清單名稱與至少 3 首歌曲名稱


# 請完成:呼叫 save_profile,傳入至少 3 個關鍵字引數,代表個人資料欄位
```

學生需要完成:

1. `add_to_playlist` 的參數設計(`playlist_name` 加上 `*args`)與印出歌曲 Tuple 的那一行
2. `save_profile` 的參數設計(`**kwargs`)與印出資料 Dictionary 的那一行
3. 兩個 function 的實際呼叫

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
def add_to_playlist(playlist_name, *args):
    print("播放清單名稱:", playlist_name)
    print("歌曲清單 Tuple:", args)


def save_profile(**kwargs):
    print("個人資料 Dictionary:", kwargs)


add_to_playlist("跑步歌單", "起飛", "追光者", "倒帶")

save_profile(nickname="小明", city="台北", hobby="打籃球")
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
# 步驟 1:定義 add_to_playlist function,參數為 playlist_name(必填)
#         以及 *args(用來接收任意數量的歌曲名稱,打包成 Tuple)


    # 步驟 2:印出 "播放清單名稱:" 加上 playlist_name


    # 步驟 3:印出 "歌曲清單 Tuple:" 加上 args


# 步驟 4:定義 save_profile function,參數為 **kwargs
#         (用來接收任意數量的關鍵字引數,打包成 Dictionary)


    # 步驟 5:印出 "個人資料 Dictionary:" 加上 kwargs


# 步驟 6:呼叫 add_to_playlist,傳入一個播放清單名稱與至少 3 首歌曲名稱(位置引數)


# 步驟 7:呼叫 save_profile,傳入至少 3 個關鍵字引數,代表個人資料欄位

```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
# 步驟 1:定義 add_to_playlist function,參數為 playlist_name(必填)
#         以及 *args(用來接收任意數量的歌曲名稱,打包成 Tuple)
def add_to_playlist(playlist_name, *args):
    # 步驟 2:印出 "播放清單名稱:" 加上 playlist_name
    print("播放清單名稱:", playlist_name)
    # 步驟 3:印出 "歌曲清單 Tuple:" 加上 args
    print("歌曲清單 Tuple:", args)


# 步驟 4:定義 save_profile function,參數為 **kwargs
#         (用來接收任意數量的關鍵字引數,打包成 Dictionary)
def save_profile(**kwargs):
    # 步驟 5:印出 "個人資料 Dictionary:" 加上 kwargs
    print("個人資料 Dictionary:", kwargs)


# 步驟 6:呼叫 add_to_playlist,傳入一個播放清單名稱與至少 3 首歌曲名稱(位置引數)
add_to_playlist("跑步歌單", "起飛", "追光者", "倒帶")

# 步驟 7:呼叫 save_profile,傳入至少 3 個關鍵字引數,代表個人資料欄位
save_profile(nickname="小明", city="台北", hobby="打籃球")
```

---

# 延伸挑戰題

## 題目

請設計一個「班級活動報名統計」的 function,名稱為 `register_activity(activity_name, *members, **details)`,同時使用 `*args` 與 `**kwargs`:

- `activity_name`:必填,活動名稱
- `*members`:任意數量的報名學生姓名(位置引數,打包成 Tuple)
- `**details`:任意數量的活動細節(關鍵字引數,例如 `location="體育館"`、`date="6/10"`,打包成 Dictionary)

function 內要印出活動名稱、報名人數(用 `len()` 算出 `members` 的長度)、報名學生名單,以及所有活動細節。

## 提示

可以思考:

- 一個 function 裡同時出現 `*members` 和 `**details` 時,呼叫的時候位置引數要放在關鍵字引數的前面還是後面?
- 如果想知道總共有幾位學生報名,要怎麼從 `members` 這個 Tuple 算出人數?
- 如果 `details` 這個 Dictionary 是空的(呼叫時沒有傳任何關鍵字引數),印出來會是什麼樣子?

---

# 思考問題

1. `*args` 打包出來的是 Tuple、`**kwargs` 打包出來的是 Dictionary,這兩種資料結構的差異,跟「位置引數」和「關鍵字引數」的特性有什麼關聯?
2. 如果呼叫 `add_to_playlist("跑步歌單")`,完全不傳入任何歌曲名稱,`args` 這個 Tuple 會是什麼內容?這說明了 `*args` 有什麼特性(是否一定要傳值)?
3. 為什麼「不確定使用者會傳入多少個引數」時,要用 `*args` 或 `**kwargs`,而不是乾脆多寫幾個「有預設值的參數」(例如寫 5 個 `song1=None, song2=None...`)?兩種做法差在哪裡?

---

# 建議查詢方向

學生可以搜尋:

1. Python *args 用法與意義
2. Python **kwargs 用法與意義
3. Python 函式參數 Tuple 與 Dictionary 差異

---

