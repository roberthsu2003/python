# uv：現代化 Python 套件管理工具

`uv` 是由 Astral 團隊（也是 `ruff` 的開發者）以 Rust 語言打造的現代化 Python 套件管理與虛擬環境工具。它的設計目標是以「單一工具」取代 `pip`、`venv`、`conda` 等多種工具，提供極速且可重現的 Python 開發環境。

## 目錄
- [第 1 章：為什麼選擇 uv？](#第-1-章為什麼選擇-uv)
  - [1.1 核心優勢](#11-核心優勢)
  - [1.2 與常見工具的比較](#12-與常見工具的比較)
- [第 2 章：安裝 uv](#第-2-章安裝-uv)
  - [2.1 系統需求](#21-系統需求)
  - [2.2 安裝方法](#22-安裝方法)
  - [2.3 確認安裝成功](#23-確認安裝成功)
- [第 3 章：專案管理與套件依賴 (推薦流程)](#第-3-章專案管理與套件依賴-推薦流程)
  - [3.1 初始化新專案 (`uv init`)](#31-初始化新專案-uv-init)
  - [3.2 管理專案套件 (`uv add` / `uv remove`)](#32-管理專案套件-uv-add--uv-remove)
  - [3.3 執行腳本與程式碼 (`uv run`)](#33-執行腳本與程式碼-uv-run)
  - [3.4 依賴鎖定與環境同步 (`uv lock` / `uv sync` / `uv.lock`)](#34-依賴鎖定與環境同步-uv-lock--uv-sync--uvlock)
- [第 4 章：虛擬環境與 Python 版本管理 (進階控制)](#第-4-章虛擬環境與-python-版本管理-進階控制)
  - [4.1 Python 版本管理 (`uv python`)](#41-python-版本管理-uv-python)
  - [4.2 建立虛擬環境 (`uv venv`)](#42-建立虛擬環境-uv-venv)
  - [4.3 啟用 / 停用虛擬環境](#43-啟用--停用虛擬環境)
  - [4.4 虛擬環境進階指令](#44-虛擬環境進階指令)
- [第 5 章：Pip 相容模式 (傳統相容流程)](#第-5-章pip-相容模式-傳統相容流程)
  - [5.1 使用 `uv pip` 管理套件](#51-使用-uv-pip-管理套件)
- [第 6 章：開發流程總結](#第-6-章開發流程總結)
- [第 7 章：常見問題 (FAQ)](#第-7-章常見問題-faq)
- [參考資料](#參考資料)

---

## 第 1 章：為什麼選擇 uv？

### 1.1 核心優勢

| 特性 | 說明 |
| :--- | :--- |
| ⚡ **極速性能** | 套件安裝與依賴解析比 `pip` 快 **10 ～ 100 倍** |
| 🔧 **一體化工具** | 整合虛擬環境、套件管理、依賴解析、Python 版本管理 |
| 📦 **現代化專案管理** | 以 `pyproject.toml` 為中心，符合 Python 社群最新標準 |
| 🔒 **可重現環境** | 自動產生 `uv.lock` 鎖定檔，確保團隊環境一致 |

### 1.2 與常見工具的比較

| 功能 | uv | pip | conda | poetry |
| :--- | :---: | :---: | :---: | :---: |
| 安裝速度 | ⚡ 極快 | 🐌 慢 | 🐌 慢 | 🐌 慢 |
| 依賴解析 | ✅ 智能 | ❌ 基本 | ✅ 智能 | ✅ 智能 |
| 虛擬環境整合 | ✅ 自動 | ❌ 需手動 | ✅ 整合 | ✅ 整合 |
| Python 版本管理 | ✅ 自動 | ❌ 無 | ✅ 支援 | ❌ 無 |
| 鎖定檔案 | ✅ uv.lock | ❌ 無 | ❌ 無 | ✅ poetry.lock |
| 現代化專案管理 | ✅ | ❌ | ❌ | ✅ |

---

## 第 2 章：安裝 uv

### 2.1 系統需求

- 支援的作業系統：**Windows、macOS、Linux**
- Python 版本：3.8+（uv 也可以自動幫你管理 Python 版本）

### 2.2 安裝方法

#### 方法一：官方腳本安裝（推薦）

**macOS / Linux：**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows（PowerShell）：**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### 方法二：套件管理器

**macOS（Homebrew）：**
```bash
brew install uv
```

**Windows（Scoop）：**
```powershell
scoop install uv
```

#### 方法三：pip 安裝
```bash
pip install uv
```

### 2.3 確認安裝成功

```bash
uv --version
```

##### 🖥️ 終端機輸出範例：
```text
uv 0.4.10 (...)
```

---

## 第 3 章：專案管理與套件依賴 (推薦流程)

### 3.1 初始化新專案 (`uv init`)

```bash
# 建立全新專案資料夾並切換進去
uv init my-project
cd my-project

# 或：在現有目錄就地初始化（建立 pyproject.toml）
uv init
```

初始化後，uv 會自動建立以下專案結構：

```text
my-project/
├── .venv/              # 虛擬環境（由 uv 自動管理）
├── pyproject.toml      # 專案設定與依賴清單
├── uv.lock             # 依賴鎖定檔案（請納入版本控制）
└── src/
    └── mypackage/
```

> [!TIP]
> **uv 初始化與虛擬環境建立流程：**
> 1. 執行 `uv init` 初始化專案。
> 2. 如需指定特定 Python 版本，可修改 `.python-version` 或 `pyproject.toml` 中的 Python 版本設定。
> 3. 當你第一次執行如 `uv add` 或 `uv run` 時，uv 會自動建立 `.venv` 並下載對應的 Python 版本，無須手動執行 `uv venv`。

### 3.2 管理專案套件 (`uv add` / `uv remove`)

在專案目錄下，推薦使用 `uv add` 來新增套件。此指令會自動將套件寫入 `pyproject.toml` 的依賴清單，並更新 `uv.lock` 鎖定檔。

```bash
# 安裝單一套件
uv add requests

# 一次安裝多個套件
uv add numpy pandas matplotlib

# 安裝指定版本範圍
uv add "django>=4.0,<5.0"

# 安裝帶有可選功能 (extras) 的套件
uv add "fastapi[all]"

# 安裝開發用套件（寫入 pyproject.toml 的 dev-dependencies，不進入生產環境）
uv add pytest --dev
```

#### 移除套件

```bash
uv remove requests
```

### 3.3 執行腳本與程式碼 (`uv run`)

使用 `uv run` 可以直接在虛擬環境中執行程式或指令，**無需手動啟用/切換虛擬環境**：

```bash
# 執行 Python 腳本
uv run python script.py

# 執行模組
uv run -m mymodule

# 執行已安裝的 CLI 工具（例如 pytest）
uv run pytest
```

### 3.4 依賴鎖定與環境同步 (`uv lock` / `uv sync` / `uv.lock`)

```bash
# 根據 pyproject.toml 產生或更新 uv.lock 鎖定檔
uv lock

# 嚴格根據鎖定檔安裝（確保環境 100% 一致，常用於 CI/CD 或部署）
uv sync --locked

# 將所有依賴套件更新至相容的最新版本
uv sync --upgrade

# 更新特定套件
uv add requests --upgrade
```

> [!TIP]
> 請將 `uv.lock` 納入 Git 版本控制，以確保所有協作者和部署環境使用完全相同的套件版本。

---

## 第 4 章：虛擬環境與 Python 版本管理 (進階控制)

在非專案目錄，或需要手動、低階管理虛擬環境與多版本 Python 的情境下，可以使用以下指令：

### 4.1 Python 版本管理 (`uv python`)

uv 可以自動下載並管理多個 Python 版本，無需依賴 pyenv 或手動安裝。

```bash
# 列出所有可用的 Python 版本與安裝狀態
uv python list

# 安裝特定版本的 Python
uv python install 3.11
```

### 4.2 建立虛擬環境 (`uv venv`)

```bash
# 在當前目錄建立虛擬環境（預設資料夾名稱：.venv）
uv venv

# 建立並指定 Python 版本
uv venv --python 3.11

# 指定自訂名稱
uv venv --name myenv
```

### 4.3 啟用 / 停用虛擬環境

#### 啟用

```bash
# macOS / Linux
source .venv/bin/activate

# Windows（命令提示字元）
.venv\Scripts\activate.bat

# Windows（PowerShell）
.venv\Scripts\Activate.ps1
```

#### 停用

```bash
deactivate
```

### 4.4 虛擬環境進階指令

```bash
# 列出所有虛擬環境
uv venv list

# 移除虛擬環境
uv venv remove .venv

# 同步環境（根據 pyproject.toml 安裝/更新套件至當前虛擬環境）
uv sync
```

---

## 第 5 章：Pip 相容模式 (傳統相容流程)

若您想保留傳統 `pip`、`requirements.txt` 的工作流程，`uv` 提供了 `uv pip` 子命令，操作方式與 `pip` 幾乎完全一致，但速度快上百倍。

> [!NOTE]
> 使用 `uv pip` 前，請確保已手動建立並啟用了虛擬環境（例如執行 `uv venv` 並 `source .venv/bin/activate`），否則 uv 會提示錯誤以避免污染系統 Python 環境。

### 5.1 使用 `uv pip` 管理套件

```bash
# 安裝套件
uv pip install requests

# 從 requirements.txt 安裝
uv pip install -r requirements.txt

# 列出已安裝的套件
uv pip list

# 顯示套件詳細資訊
uv pip show requests

# 更新套件
uv pip install --upgrade requests

# 檢查依賴衝突
uv pip check

# 匯出 requirements.txt
uv pip freeze > requirements.txt
```

---

## 第 6 章：開發流程總結

以下是從建立新專案到部署的完整推薦指令流程：

```bash
# 1. 建立並初始化新專案
uv init my-project
cd my-project

# 2. 安裝生產環境所需的套件（自動建立 .venv）
uv add requests fastapi

# 3. 安裝開發與測試用套件
uv add pytest --dev

# 4. 執行程式（無需啟用虛擬環境）
uv run python main.py

# 5. 執行測試
uv run pytest

# 6. 部署：根據鎖定檔同步環境（不包含開發用套件）
uv sync --locked --no-dev
```

---

## 第 7 章：常見問題 (FAQ)

### Q：如何從現有的 `requirements.txt` 遷移？

```bash
# 1. 初始化專案
uv init

# 2. 安裝 requirements.txt 中的依賴至虛擬環境
uv pip install -r requirements.txt

# 3. 將這些依賴寫入 pyproject.toml
uv add $(uv pip freeze | cut -d'=' -f1)
```

### Q：如何設定私有 PyPI 伺服器？

在 `pyproject.toml` 中新增以下設定：

```toml
[[tool.uv.index]]
name = "private"
url = "https://pypi.company.com/simple/"
```

### Q：如何區分開發環境與生產環境的套件？

```bash
# 安裝只在開發/測試時使用的套件
uv add pytest --dev

# 部署時同步環境，並排除開發用套件
uv sync --no-dev
```

---

## 參考資料

- [uv 官方文件](https://docs.astral.sh/uv/)
- [uv GitHub 儲存庫](https://github.com/astral-sh/uv)
- [pyproject.toml 規範](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
