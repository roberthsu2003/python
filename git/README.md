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

## 第 3 章：`git init` — 初始化本地倉庫

在開始使用 Git 追蹤你的專案之前，必須先在專案目錄中建立一個 Git 本地倉庫（Repository）。

請在終端機中切換至你的專案資料夾，然後執行：

```bash
git init
```

> [!NOTE]
> 執行此指令後，Git 會在該專案目錄下建立一個隱藏的 `.git` 資料夾。這個資料夾包含了 Git 所需的所有元數據和歷史記錄。一旦建立，就代表該專案已正式由 Git 進行版本控制。

##### 🖥️ 終端機輸出範例：
```text
Initialized empty Git repository in /Users/roberthsu2003/Documents/GitHub/python/git/.git/
```

---

## 第 4 章：基本工作流程

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

## 第 5 章：`git status` — 查看目前狀態

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

## 第 6 章：`git add` — 加入暫存區

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

## 第 7 章：`git commit` — 建立版本快照

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

## 第 8 章：`git log` — 查看提交歷史紀錄

當你建立了一些 commit 之後，可以使用 `git log` 指令來查看歷史的提交紀錄。

```bash
git log
```

### 常用的參數選項

| 參數 | 說明 |
| :--- | :--- |
| `git log` | 顯示詳細的提交歷史（包含作者、時間、Commit ID 與完整說明） |
| `git log --oneline` | 以「單行」簡短格式顯示提交歷史（常用） |
| `git log -p` | 顯示歷史紀錄的同時，列出檔案具體的修改差異（Diff） |
| `git log -n <數量>` | 限制只顯示最近的 `<數量>` 筆紀錄（例如 `git log -n 5`） |

##### 🖥️ 終端機輸出範例 (`git log --oneline`)：
```text
e4f5g6h (HEAD -> main, origin/main) 修正：修正購物車金額計算錯誤
a1b2c3d 新增 hello.py，完成第一章練習
```

---

## 第 9 章：`git push` — 推送至遠端（GitHub）

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

## 第 10 章：完整操作流程總結

以下是從零開始到成功推送的完整指令流程：

```bash
# 1. 【一次性設定】設定使用者資訊
git config --global user.name "Robert Hsu"
git config --global user.email "robert@example.com"

# 2. 【查看設定】確認設定是否正確
git config --list

# 3. 【初始化專案】在專案目錄中初始化 Git 倉庫
git init

# 4. 【新增或修改檔案後】查看目前狀態
git status

# 5. 【將變更加入暫存區】
git add .

# 6. 【建立 commit 版本快照】
git commit -m "完成功能 XXX 的開發"

# 7. 【查看提交歷史紀錄】
git log --oneline

# 8. 【推送至 GitHub】
git push origin main
```

---

## 第 11 章：進階工具 — `git worktree`（適合 AI 協作 / Vibe Coding）

在現代開發中（特別是使用 AI 輔助編程或 Vibe Coding 時），我們常常需要同時開發多個功能、修復緊急 Bug，或者在不同的分支間快速對照程式碼。傳統上我們需要使用 `git stash` 暫存工作進度，再執行 `git checkout` 切換分支；但使用 `git worktree` 可以讓我們**在不同的資料夾中同時開啟多個不同的分支**。

### 為什麼要使用 Worktree？
- **無需頻繁切換分支**：可以同時開好幾個編輯器視窗，每個視窗對應同一個專案的不同分支。
- **免除 Stash 困擾**：工作目錄有寫到一半的程式碼時，不需要 `git stash` 或隨意 `git commit`，直接建立新 worktree 即可開始做新分支的事情。
- **適合 Vibe Coding / AI Agents**：可以讓 AI Agent 在另一個 worktree 獨立進行程式碼編寫與測試，不影響你目前的開發目錄。

### 11.1 建立新的工作區 (Worktree)

```bash
git worktree add <路徑> <分支名稱>
```

- 如果該分支還不存在，可以加上 `-b` 來建立新分支：
```bash
git worktree add ../my-feature-branch -b feature-branch
```
這會在目前專案上一層的 `my-feature-branch` 資料夾中，建立並檢出一個乾淨的新分支 `feature-branch`。

### 11.2 查看目前所有的工作區

```bash
git worktree list
```

##### 🖥️ 終端機輸出範例：
```text
/Users/roberthsu2003/Documents/GitHub/python/git        a1b2c3d [main]
/Users/roberthsu2003/Documents/GitHub/python/my-feature-branch  a1b2c3d [feature-branch]
```

### 11.3 刪除/清理工作區

當你完成該分支的開發並合併（Merge）後，可以將該工作區移除：

```bash
git worktree remove <工作區資料夾路徑>
```

範例：
```bash
git worktree remove ../my-feature-branch
```

> [!TIP]
> 刪除 worktree 資料夾後，可以使用 `git worktree prune` 來清理 Git 內部殘留的無效工作區記錄。
