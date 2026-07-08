# Pydantic 資料驗證與資料處理教學

本單元設計了一系列**「由淺入深、漸進式學習」**的 Markdown 教材，幫助你從零開始學習如何使用 **Pydantic V2** 進行資料驗證、型態轉換與實務資料清洗。


## 📖 各單元詳細說明

### 01. [Pydantic 基礎模型與巢狀結構](./01_pydantic基礎模型與巢狀結構.md)
- **單元目標**：理解 Pydantic 的基本運作機制，掌握資料型態的自動轉換與約束。
- **使用數據源**：無
- **重點知識**：
  - `BaseModel` 的繼承與定義。
  - Pydantic 如何自動將字串 `"42"` 轉換為整數 `42`（型態自動轉換 Type Coercion）。
  - Required (必要) vs. Optional (選用) vs. Nullable (可為 None) 欄位的宣告方式。
  - 欄位別名 `Field(alias=...)` 與配置項目 `populate_by_name` 的應用。
  - 巢狀結構模型（一個 BaseModel 作為另一個 BaseModel 的欄位）。
  - `TypeAdapter` 適用於最外層資料結構為 `List` 或 `Dict` 等非 `BaseModel` 類型的資料驗證與解析。
 
### 02. [Pydantic 預設值與自訂驗證及序列化](./02_pydantic預設值與自訂驗證及序列化.md)
- **單元目標**：學會如何動態產生欄位的預設值，以及在資料輸入與輸出時自訂處理邏輯。
- **使用數據源**：無
- **重點知識**：
  - 解決「共享預設物件」的問題：使用 `Field(default_factory=...)` 動態生成物件/時間/亂數。
  - 自訂輸出序列化：使用 `@field_serializer` 調整 JSON 輸出的數值格式（例如限制小數點位數）。
  - 自訂驗證器：使用 `@field_validator` 針對特定欄位進行邏輯檢查（例如不能為負數）。
  - 模型層級驗證：使用 `@model_validator(mode='after')` 進行跨欄位的邏輯檢查。
 
### 03. [實務應用一：學生分數 CSV 解析](./03_實務應用_學生分數CSV解析.md)
- **單元目標**：結合 Python 標準庫 `csv.DictReader` 讀取外部資料，並載入至 Pydantic Model 中。
- **使用數據源**：`學生分數.csv`
- **重點知識**：
  - 使用 `DictReader` 讀取並迭代 CSV 檔案中的每一行。
  - 使用 `alias` 將 CSV 中的中文欄位名稱（如 `科目1`）對照到 Pydantic Model 中更直觀的名稱（如 `國文`）。
  - 實作自訂方法 `def total(self) -> int` 與屬性 `@property def sum(self)` 計算學生成績總分。
 
### 04. [實務應用二：AQI 空氣品質 JSON 解析](./04_實務應用_AQI空氣品質JSON解析.md)
- **單元目標**：解析結構較為複雜的環保署空氣品質 JSON 資料。
- **使用數據源**：`空氣品質aqi.json`
- **重點知識**：
  - 使用 `model_validate_json()` 解析 JSON 字串。
  - 設計 `SiteName` (站點模型) 與 `Records` (包含 site 列表的外層模型)。
  - 利用 `mode='before'` 的驗證器，在資料被轉成 float 之前將空字串 `""` 預先清理為 `"0.0"`，避免轉換出錯。
 
### 05. [實務應用三：AQI 空氣品質 CSV 與自訂驗證](./05_實務應用_AQI空氣品質CSV與自訂驗證.md)
- **單元目標**：與單元 04 做對照，練習如何解析 CSV 版本的空氣品質資料。
- **使用數據源**：`空氣品質aqi.csv`
- **重點知識**：
  - 使用清單推導式配合 `SiteName.model_validate` 批次載入並驗證 CSV 清單。
  - 搭配 `@field_validator` 解決 CSV 中缺少資料的空字串問題。
  - 利用 `TypeAdapter` 進行列表資料的序列化（`.dump_json()`、`.dump_python()`）與檔案儲存。
 
### 06. [實務應用四：個股日成交複雜資料清理](./06_實務應用_個股日成交複雜資料清理.md)
- **單元目標**：掌握實務中最常見的「髒資料」清洗方法，提升資料工程實戰力。
- **使用數據源**：`個股日成交資訊.csv`
- **重點知識**：
  - 清理數值字串中的逗號（如 `1,463,020` $\rightarrow$ `1463020`）與處理特殊字符。
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