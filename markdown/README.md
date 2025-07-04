# Markdown

**‼️標示list結束**

**問題:**

```md
- one
- two
- three

    not a list item
```

- one
- two
- three

    not a list item
    
**使用Html標籤解決**

```md
- one
- two
- three
<a/>
    not a list item
```

- one
- two
- three
<a/>  
    not a list item
    
 **使用markdown註解**
 
 ```
 - one
- two
- three

[//]: # (Hello)
    not a list item
 ```  
 
  - one
- two
- three

[//]: 
    not a list item 

## 使用表格組織資訊

您可以建立表格來組織評論、問題、拉取請求和 wiki 中的資訊。

您可以使用垂直線 | 和連字符 - 建立表格。連字符用於建立每列的標題，而豎線用於分隔每列。為了確保表格能夠正確呈現，必須在表格前面加上一個空白行。

```md
| First Header | Second Header |
| ------------ | ------------- |
| Content Cell | Content Cell  |
| Content Cell | Content Cell  |
```

| First Header | Second Header |
| ------------ | ------------- |
| Content Cell | Content Cell  |
| Content Cell | Content Cell  |

---
### ‼️單元格寬度可以變化，且無需在列內完全對齊。標題行的每一列必須至少有三個連字符。

```md
| Command | Description |
| --- | --- |
| git status | List all new or modified files |
| git diff | Show file differences that haven't been staged |
```

| Command | Description |
| --- | --- |
| git status | List all new or modified files |
| git diff | Show file differences that haven't been staged |

---

### 格式化表格中的內容

您可以在表格中使用連結、單行程式碼區塊和文字樣式等格式：

```md
| Command | Description |
| --- | --- |
| `git status` | List all *new or modified* files |
| `git diff` | Show file differences that **haven't been** staged |
```

| Command | Description |
| --- | --- |
| `git status` | List all *new or modified* files |
| `git diff` | Show file differences that **haven't been** staged |

---

**您可以透過在標題行中的連字符左側、右側或兩側添加冒號 : 將文字對齊到列的左側、右側或中央。**

```md
| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
```

| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |

---

**若要將管道 | 作為內容包含在單元格中，請在管道前使用 \：**

```md
| Name     | Character |
| ---      | ---       |
| Backtick | `         |
| Pipe     | \|        |
```

| Name     | Character |
| ---      | ---       |
| Backtick | `         |
| Pipe     | \|        |