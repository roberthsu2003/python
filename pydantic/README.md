# Pydantic 資料驗證與資料處理教學

本單元設計了一系列**「由淺入深、漸進式學習」**的 Jupyter Notebook，幫助你從零開始學習如何使用 **Pydantic V2** 進行資料驗證、型態轉換與實務資料清洗。

---

## 🎯 學習路徑與教材地圖

| 步驟 | 單元名稱 | 核心學習重點 | 使用數據源 | 檔案連結 |
|:---:|:---|:---|:---:|:---:|
| **01** | **Pydantic 基礎模型與巢狀結構** | `BaseModel` 基礎、型態自動轉換 (Type Coercion)、選用與必要欄位、`RootModel`、巢狀模型 (Nested Models) | - | [開啟 Notebook](./01_pydantic基礎模型與巢狀結構.ipynb) |
| **02** | **Pydantic 預設值與自訂驗證及序列化** | `default_factory` 動態預設值、`@field_serializer` 自訂序列化、`@field_validator` 自訂驗證、`@model_validator` 整體模型驗證 | - | [開啟 Notebook](./02_pydantic預設值與自訂驗證及序列化.ipynb) |
| **03** | **實務應用一：學生分數 CSV 解析** | 結合 `csv.DictReader` 讀取 CSV、欄位別名 (`Field(alias=...)`)、在 Model 中實作自訂方法 (Methods) 與屬性 (Property) | `學生分數.csv` | [開啟 Notebook](./03_實務應用_學生分數CSV解析.ipynb) |
| **04** | **實務應用二：AQI 空氣品質 JSON 解析** | 使用 `model_validate_json()` 解析巢狀 JSON、利用 `@field_validator(mode='before')` 清理空字串或異常數值 | `空氣品質aqi.json` | [開啟 Notebook](./04_實務應用_AQI空氣品質JSON解析.ipynb) |
| **05** | **實務應用三：AQI 空氣品質 CSV 與自訂驗證** | 使用 `RootModel` 封裝 List 結構、搭配 `@field_validator` 解決 CSV 中缺少資料的空字串問題 | `空氣品質aqi.csv` | [開啟 Notebook](./05_實務應用_AQI空氣品質CSV與自訂驗證.ipynb) |
| **06** | **實務應用四：個股日成交複雜資料清理** | 清理數值字串中的逗號 (如 `1,463,020` $\rightarrow$ `1463020`)、處理特殊字符、使用 `Annotated` 搭配 `BeforeValidator` 封裝重複使用的清理邏輯 | `個股日成交資訊.csv` | [開啟 Notebook](./06_實務應用_個股日成交複雜資料清理.ipynb) |

---

## 📖 各單元詳細說明

### 01. [Pydantic 基礎模型與巢狀結構](./01_pydantic基礎模型與巢狀結構.ipynb)
- **單元目標**：理解 Pydantic 的基本運作機制，掌握資料型態的自動轉換與約束。
- **重點知識**：
  - `BaseModel` 的繼承與定義。
  - Pydantic 如何自動將字串 `"42"` 轉換為整數 `42`。
  - Required (必要) vs. Optional (選用) vs. Nullable (可為 None) 欄位的宣告方式。
  - 欄位別名 `Field(alias=...)` 與配置項目 `populate_by_name` 的應用。
  - 巢狀結構模型（一個 BaseModel 作為另一個 BaseModel 的欄位）。
  - `RootModel` 適用於最外層資料結構為 `List` 或 `Dict` 的情境。

### 02. [Pydantic 預設值與自訂驗證及序列化](./02_pydantic預設值與自訂驗證及序列化.ipynb)
- **單元目標**：學會如何動態產生欄位的預設值，以及在資料輸入與輸出時自訂處理邏輯。
- **重點知識**：
  - 解決「共享預設物件」的問題：使用 `Field(default_factory=...)` 動態生成物件/時間/亂數。
  - 自訂輸出序列化：使用 `@field_serializer` 調整 JSON 輸出的數值格式（例如限制小數點位數）。
  - 自訂驗證器：使用 `@field_validator` 針對特定欄位進行邏輯檢查（例如不能為負數）。
  - 模型層級驗證：使用 `@model_validator(mode='after')` 進行跨欄位的邏輯檢查。

### 03. [實務應用一：學生分數 CSV 解析](./03_實務應用_學生分數CSV解析.ipynb)
- **單元目標**：結合 Python 標準庫 `csv.DictReader` 讀取外部資料，並載入至 Pydantic Model 中。
- **重點知識**：
  - 使用 `DictReader` 讀取並迭代 CSV 檔案中的每一行。
  - 使用 `alias` 將 CSV 中的中文欄位名稱（如 `科目1`）對照到 Pydantic Model 中更直觀的名稱（如 `國文`）。
  - 實作自訂方法 `def total(self) -> int` 與屬性 `@property def sum(self)` 計算學生成績總分。

### 04. [實務應用二：AQI 空氣品質 JSON 解析](./04_實務應用_AQI空氣品質JSON解析.ipynb)
- **單元目標**：解析結構較為複雜的環保署空氣品質 JSON 資料。
- **重點知識**：
  - 使用 `model_validate_json()` 解析 JSON 字串。
  - 設計 `SiteName` (站點模型) 與 `Records` (包含 site 列表的外層模型)。
  - 利用 `mode='before'` 的驗證器，在資料被轉成 float 之前將空字串 `""` 預先清理為 `"0.0"`，避免轉換出錯。

### 05. [實務應用三：AQI 空氣品質 CSV 與自訂驗證](./05_實務應用_AQI空氣品質CSV與自訂驗證.ipynb)
- **單元目標**：與單元 04 做對照，練習如何解析 CSV 版本的空氣品質資料。
- **重點知識**：
  - 以 `RootModel` 搭配 `list[SiteName]` 直接載入 CSV 清單。
  - 實現 `__iter__` 與 `__getitem__` 魔術方法，讓 `RootModel` 實體可以直接像標準 Python 串列一樣被迭代與索引。

### 06. [實務應用四：個股日成交複雜資料清理](./06_實務應用_個股日成交複雜資料清理.ipynb)
- **單元目標**：掌握實務中最常見的「髒資料」清洗方法，提升資料工程實戰力。
- **重點知識**：
  - 使用 `typing.Annotated` 搭配 `BeforeValidator`，將「清除千分位逗號」與「去除字串前後空格與特殊字符 `X`」的清理邏輯封裝成自訂型別。
  - 自訂型別如 `CommaSeperatedInt` 與 `CommaSeperatedFloat` 可以直接應用於多個欄位，極大簡化 Model 的程式碼。

---

## 📁 數據源檔案清單

此資料夾內附有以下實務練習所需的數據源檔案：
- 📄 `學生分數.csv`：學生各科目分數的 CSV 檔案（包含中文欄位）。
- 📄 `空氣品質aqi.json`：環保署 AQI 資料（JSON 格式，包含巢狀 `records` 結構）。
- 📄 `空氣品質aqi.csv`：環保署 AQI 資料（CSV 格式）。
- 📄 `個股日成交資訊.csv`：台股日成交資訊（CSV 格式，包含千分位逗號以及帶有 `X` 等特殊符號的數值）。
- 📄 `新北市食品工廠清冊.json` & `data.json`：供學生自主練習與挑戰的 JSON 數據集。