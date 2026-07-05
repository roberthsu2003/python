# JupyterLab 安裝與 LSP 型別提示設定指引

JupyterLab 是專為 Python 與資料科學開發設計的現代互動式環境。本指南將引導您使用 **uv** 套件管理器安裝 JupyterLab，並透過 **LSP (Language Server Protocol)** 機制與 **Basedpyright** 靜態分析器，為網頁端 JupyterLab 加上與 VS Code 同等強大的「智慧型型別提示」與「自動補齊」功能。

---

## 1. 安裝與啟動 JupyterLab

我們使用 **uv** 來管理專案相依性。建議直接將 JupyterLab、LSP 介面與 Basedpyright 加入為專案的開發相依套件：

### 步驟 1：安裝相關套件
請在您的專案根目錄下，執行以下指令：

```bash
# 安裝 LSP 介面與 Basedpyright（會自動連帶安裝 JupyterLab）
uv add --dev jupyterlab-lsp basedpyright
```

### 步驟 2：啟動 JupyterLab
安裝完成後，使用 `uv run` 啟動：

```bash
uv run jupyter lab
```
執行後，系統會自動在瀏覽器中開啟 `http://localhost:8888/lab` 介面。

---

## 2. 在 JupyterLab 網頁端開啟自動提示

啟動 JupyterLab 並進入瀏覽器網頁後，請進行以下設定以開啟自動提示與檢查（不需要每次都按 `Tab` 鍵）：

1. 點選網頁上方選單的 **Settings (設定) -> Settings Editor (設定編輯器)**。
2. 在左側選單中找到 **Code Completion (程式碼補齊)**。
3. 確保勾選啟用 **`autoCompletion`**。
4. 勾選 **`Continuous Hinting` (持續提示)**。
5. （選用）若您同時裝有其他語言伺服器，可在左側選單的 **Language Servers (語言伺服器)** 中，手動將 `basedpyright` 調整為最高優先權。
6. 自訂型別檢查規則可以直接在專案根目錄的 `pyproject.toml` 內加入 `[tool.basedpyright]` 進行設定。

---

## 3. 驗證設定
在 JupyterLab 中新建一個 Python Notebook (`.ipynb`)，輸入以下程式碼進行測試：

```python
# 宣告型別提示
name: str = "羅伯特"

# 當您輸入「name.」時，應會自動跳出所有字串方法 (例如 upper, lower, title)
name.
```
若畫面中能出現方法選單，且當指派錯誤型別（例如 `name: str = 123`）時會出現底線提示，即代表 LSP 型別提示設定成功！