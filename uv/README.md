## 使用 uv 取代 Conda：更快速、現代化的 Python 虛擬環境管理工具

對於習慣使用 Conda 管理 Python 虛擬環境的開發者來說，新興的工具 `uv` 提供了一個更快速、更符合現代 Python 開發流程的替代方案。`uv` 由 `ruff` 的開發團隊 Astral 使用 Rust 語言打造，其目標是成為一個極速的 Python 套件安裝與專案管理工具。本指南將引導您如何安裝 `uv`，並使用它來建立與管理虛擬環境，以無縫接軌您習慣的開發流程。

### 為什麼考慮使用 uv 取代 Conda？

  - **速度**：`uv` 在安裝和解析依賴項方面，速度顯著優於 Conda。這在大型專案或需要頻繁建立環境的場景中尤其有感。
  - **現代化的專案管理**：`uv` 鼓勵使用 `pyproject.toml` 檔案來管理專案依賴，這是目前 Python 社群推崇的最佳實踐，有助於提高專案的可重現性和標準化。
  - **單一工具鏈**：`uv` 整合了虛擬環境管理、套件安裝、依賴解析等多種功能，無需像 Conda 那樣在 `conda` 和 `pip` 之間切換。

### 第一步：安裝 uv

您可以根據您的作業系統選擇以下任何一種方式來安裝 `uv`。建議使用獨立安裝腳本，以避免與系統現有的 Python 環境產生衝突。

**macOS 和 Linux：**

使用 `curl` 進行安裝：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

或者，如果您是 macOS 用戶且已安裝 [Homebrew](https://brew.sh/)：

```bash
brew install uv
```

**Windows：**

在 PowerShell 中執行以下命令：

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

安裝完成後，您可以透過以下命令來驗證 `uv` 是否成功安裝：

```bash
uv --version
```

### 第二步：使用 uv 建立與管理虛擬環境

`uv` 的虛擬環境管理指令直觀易懂，以下將其與您熟悉的 Conda 指令進行對照：

#### 1\. 建立虛擬環境

  - **Conda 的做法：**

    ```bash
    conda create --name myenv python=3.10
    ```

  - **uv 的做法：**
    `uv` 預設會在您當前的專案目錄下建立一個名為 `.venv` 的虛擬環境資料夾。這是現代 Python 開發的慣例。

    ```bash
    # 進入您的專案目錄
    cd my-project

    # 建立虛擬環境 (uv 會自動偵測並使用您系統上已安裝的 Python 版本)
    uv venv
    ```

    如果您想指定特定的 Python 版本來建立虛擬環境 (例如 Python 3.10)，可以這樣做：

    ```bash
    uv venv --python 3.10
    ```

    `uv` 甚至可以協助您安裝所需的 Python 版本：

    ```bash
    uv python install 3.10
    ```

#### 2\. 啟用虛擬環境

  - **Conda 的做法：**

    ```bash
    conda activate myenv
    ```

  - **uv 的做法：**
    啟用虛擬環境的方式與 Python 內建的 `venv` 模組相同。

    **macOS 和 Linux (使用 bash/zsh)：**

    ```bash
    source .venv/bin/activate
    ```

    **Windows (使用 Command Prompt)：**

    ```bash
    .venv\Scripts\activate.bat
    ```

    **Windows (使用 PowerShell)：**

    ```powershell
    .venv\Scripts\Activate.ps1
    ```

    啟用後，您的命令提示字元前會出現 `(.venv)` 的字樣。

#### 3\. 安裝套件

  - **Conda 的做法：**

    ```bash
    conda install numpy
    # 或者使用 pip
    pip install pandas
    ```

  - **uv 的做法：**
    在已啟用的虛擬環境中，使用 `uv pip install` 來安裝套件。

    ```bash
    uv pip install numpy pandas
    ```

    `uv` 的套件安裝速度通常會比 `pip` 或 `conda` 快上許多。

#### 4\. 停用虛擬環境

  - **Conda 和 uv 的做法：**
    停用虛擬環境的指令是相同的。

    ```bash
    deactivate
    ```

### 專案導向的工作流程：`uv init` 和 `pyproject.toml`

`uv` 強烈建議以專案為中心來管理依賴。您可以透過 `uv init` 來初始化一個新專案，這會自動建立一個 `pyproject.toml` 檔案。

```bash
mkdir new-awesome-project
cd new-awesome-project
uv init
```

接著，您可以使用 `uv add` 來新增專案依賴，`uv` 會自動將其記錄在 `pyproject.toml` 中，並安裝到您的虛擬環境。

```bash
# 建立虛擬環境
uv venv

# 啟用虛擬環境
source .venv/bin/activate

# 新增依賴
uv add requests
uv add "fastapi[all]" --dev # 新增開發依賴
```

這種方式取代了傳統 `requirements.txt` 的管理方式，讓您的專案依賴更加清晰且易於重現。

### 結論

`uv` 憑藉其卓越的速度和現代化的專案管理理念，為 Python 開發者提供了一個取代 Conda 的絕佳選擇。透過遵循本指南，您可以輕鬆地將您現有的開發流程從 Conda 轉移到 `uv`，並享受到更高效、更流暢的 Python 開發體驗。從今天起，嘗試在您的新專案中使用 `uv`，感受下一代 Python 工具所帶來的變革。
