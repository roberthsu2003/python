# Markdown

## 清單

您可以在一行或多行文字前加上 -、* 或 + 來建立無序列表。

```md
- George Washington
* John Adams
+ Thomas Jefferson
```

- George Washington
* John Adams
+ Thomas Jefferson

---

**若要對清單進行排序，請在每行前面加上一個數字。**

```md
1. James Madison
2. James Monroe
3. John Quincy Adams
```

1. James Madison
2. James Monroe
3. John Quincy Adams

---

## 巢狀清單

您可以將一個或多個清單項目縮排到另一個清單項目下方來建立巢狀清單。

要使用 GitHub 上的網頁編輯器或使用等寬字體的文字編輯器（例如 Visual Studio Code）建立嵌套列表，您可以直觀地對齊列表。在嵌套清單項目前面鍵入空格字符，直到列表標記字符（- 或 *）位於其上方項中文本的第一個字符的正下方。

```md
1. First list item
   - First nested list item
     - Second nested list item
```

![](./images/nested-list-alignment.webp)


## 任務清單

To create a task list, preface list items with a hyphen and space followed by [ ]. To mark a task as complete, use [x].

```md
- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:
```

![](task-list-rendered-simple.webp)

---

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

[//]: # (hello)
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