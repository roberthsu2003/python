# Git 基本設定與使用

Git 是目前最廣泛使用的「分散式版本控制系統」，讓我們可以追蹤程式碼的每一次變更、與他人協作，以及在需要時回溯任何一個歷史版本。

---

## 第 1 章：安裝 Git

### macOS

macOS 通常已內建 Git。可先在終端機輸入以下指令確認是否已安裝：

```bash
git --version
```

若顯示版本號（例如 `git version 2.39.3`）則已安裝完成。若尚未安裝，推薦透過 **Homebrew** 安裝：

```bash
brew install git
```

### Windows

至官方網站下載安裝程式：[https://git-scm.com/download/win](https://git-scm.com/download/win)

安裝時建議選擇「**Git Bash Here**」選項，以便在右鍵選單快速開啟終端機。

安裝完成後，在「命令提示字元」或「Git Bash」輸入以下指令確認：

```bash
git --version
```

---

## 第 2 章：初始設定 — 告訴 Git 你是誰

Git 在每一次 commit（提交）時，都需要記錄「是誰做的」。因此安裝完成後，**第一件事**就是設定你的姓名和 Email。

### 2.1 設定使用者名稱

```bash
git config --global user.name "你的名字"
```

範例：
```bash
git config --global user.name "Robert Hsu"
```

### 2.2 設定電子郵件

```bash
git config --global user.email "你的Email"
```

範例：
```bash
git config --global user.email "robert@example.com"
```

> [!IMPORTANT]
> `--global` 代表此設定套用於「這台電腦上所有的 Git 專案」。若只想針對單一專案設定，可以省略 `--global`，在該專案資料夾內執行即可。

### 2.3 確認所有設定

使用 `--list` 查看目前所有的 Git 設定值：

```bash
git config --list
```

##### 🖥️ 終端機輸出範例：
```text
user.name=Robert Hsu
user.email=robert@example.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
```

---

## 第 3 章：基本工作流程

Git 的核心流程可以用以下三個步驟概括：

```
工作目錄 (Working Directory)
    ↓  git add
暫存區 (Staging Area / Index)
    ↓  git commit
本地倉庫 (Local Repository)
    ↓  git push
遠端倉庫 (Remote Repository, e.g. GitHub)
```

---

## 第 4 章：`git status` — 查看目前狀態

在執行任何操作前，`git status` 是最重要的指令，用來查看目前工作目錄與暫存區的狀態。

```bash
git status
```

### 常見的狀態說明

| 狀態訊息 | 說明 |
| :--- | :--- |
| `Untracked files` | 新建立的檔案，Git 尚未追蹤 |
| `Changes not staged for commit` | 已追蹤的檔案被修改，但尚未加入暫存區 |
| `Changes to be committed` | 檔案已加入暫存區，等待 commit |
| `nothing to commit, working tree clean` | 工作目錄乾淨，沒有任何變更 |

##### 🖥️ 終端機輸出範例（有新檔案尚未追蹤）：
```text
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.py

nothing added to commit but untracked files present (use "git add" to track)
```

---

## 第 5 章：`git add` — 加入暫存區

`git add` 指令會將指定的檔案從「工作目錄」加入「暫存區」，準備好待 commit。

### 加入單一檔案

```bash
git add 檔案名稱
```

範例：
```bash
git add hello.py
```

### 加入所有變更的檔案

```bash
git add .
```

> [!TIP]
> `git add .` 會將目前目錄下**所有**新增或修改的檔案一次加入暫存區，是最常用的寫法。

執行後再次執行 `git status` 確認：

##### 🖥️ 終端機輸出範例（加入暫存區後）：
```text
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   hello.py
```

---

## 第 6 章：`git commit` — 建立版本快照

`git commit` 將暫存區的所有變更，正式記錄為一個版本節點（Commit）。每次 commit 都必須附上一段說明訊息（Message）。

```bash
git commit -m "你的提交說明"
```

範例：
```bash
git commit -m "新增 hello.py，完成第一章練習"
```

> [!TIP]
> 好的 commit 訊息應簡短說明「**做了什麼**」。常見格式範例：
> - `新增：新增使用者登入功能`
> - `修正：修正購物車金額計算錯誤`
> - `更新：更新 README 安裝說明`

##### 🖥️ 終端機輸出範例：
```text
[main (root-commit) a1b2c3d] 新增 hello.py，完成第一章練習
 1 file changed, 1 insertion(+)
 create mode 100644 hello.py
```

---

## 第 7 章：`git push` — 推送至遠端（GitHub）

`git push` 將本地的 commit 記錄上傳至遠端倉庫（如 GitHub），讓其他人可以看到你的變更，或在另一台電腦上繼續作業。

```bash
git push origin main
```

| 參數 | 說明 |
| :--- | :--- |
| `origin` | 遠端倉庫的預設名稱（即 GitHub 上的 Repo） |
| `main` | 要推送的分支名稱（舊版 Git 可能為 `master`） |

##### 🖥️ 終端機輸出範例：
```text
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 247 bytes | 247.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/yourname/yourrepo.git
   a1b2c3d..e4f5g6h  main -> main
```

---

## 第 8 章：完整操作流程總結

以下是從零開始到成功推送的完整指令流程：

```bash
# 1. 【一次性設定】設定使用者資訊
git config --global user.name "Robert Hsu"
git config --global user.email "robert@example.com"

# 2. 【查看設定】確認設定是否正確
git config --list

# 3. 【新增或修改檔案後】查看目前狀態
git status

# 4. 【將變更加入暫存區】
git add .

# 5. 【建立 commit 版本快照】
git commit -m "完成功能 XXX 的開發"

# 6. 【推送至 GitHub】
git push origin main
```
