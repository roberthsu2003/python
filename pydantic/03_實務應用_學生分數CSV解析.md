# 實務應用一：學生分數 CSV 解析

本單元將帶您進入第一個真實資料處理的實務範例。我們將使用 Python 標準庫的 `csv.DictReader` 讀取 CSV 檔案，並透過 Pydantic 進行資料格式對齊、自動轉型與資料驗證。

---

## 1. CSV 資料結構映射與 Pydantic 整合

💡 **學習觀念 1：欄位別名 (Field Alias) 的應用**
在實務上，外部 CSV 檔案的欄位名稱經常是中文或不符合 Python 變數命名規範的字元（例如 `科目1`、`科目2`）。我們可以使用 `Field(alias='科目1')` 來進行對照。這樣做有兩個好處：
1. **符合 PEP 8 命名規範**：Python 程式內可以使用具備明確語意的英文變數（如 `name`、`chinese`）。
2. **自動型別轉換**：CSV 讀出來的資料預設全都是字串，Pydantic 會自動將它們轉成 `int`。

💡 **學習觀念 2：在 Pydantic Model 中加入業務邏輯與屬性**
Pydantic 模型不僅能用來驗證資料，還能當作一般的 Python 類別來使用。我們可以在模型內宣告一般方法（如 `def total(self) -> int`）或使用屬性裝飾器（`@property def sum(self)`）來計算學生的分數總和。

💡 **學習觀念 3：批次驗證與解析清單資料**
當 CSV 檔案內含有多行學生資料時，我們可以直接使用清單推導式 (List Comprehension)，對讀取出的每一列 `dict` 呼叫 `Student.model_validate(row)`。這樣做的好處是語法直覺且符合標準 Python 習慣，無需額外定義 `RootModel` 封裝，即可快速取得一個包含所有驗證後學生模型實例的標準 Python `list[Student]`。

```python
import csv
from pydantic import BaseModel, Field
from pprint import pprint

# 定義單一學生的資料結構與計算邏輯
class Student(BaseModel):
    name: str = Field(alias='姓名')
    chinese: int = Field(alias='科目1')
    english: int = Field(alias='科目2')
    math: int = Field(alias='科目3')
    geography: int = Field(alias='科目4')
    history: int = Field(alias='科目5')
    social: int = Field(alias='科目6')
    morality: int = Field(alias='科目7')

    # 自訂計算總分的方法
    def total(self) -> int:
        return self.chinese + self.english + self.math + self.geography + self.history + self.social + self.morality
    
    # 自訂屬性來取得總分
    @property
    def sum(self) -> int:
        return self.total() 

# 讀取 CSV 檔案並使用 Pydantic 進行解析與驗證
with open('學生分數.csv', encoding='utf8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # 使用清單推導式批次驗證與轉換每一列資料
    students = [Student.model_validate(row) for row in reader]

# 遍歷所有學生並列印計算出的總分
for student in students:
    print(student.total())
    print(student.sum)
```


**輸出結果：**
```text
597
597
463
463
569
569
... (以下省略)
```

---

## 2. FastAPI 實務整合與最佳設計

當我們需要將此 CSV 解析邏輯整合至 FastAPI 專案中，且 **CSV 檔案已預先配置於伺服器端** 時，設計上會有以下調整：
1. **對外 API 欄位英文化**：輸入的 CSV 雖然是中文欄位（如 `科目1`），但 API 回傳的 JSON 應該是標準的英文 `snake_case`（如 `chinese`）。
2. **自動序列化總分**：原始的 `@property` 在 FastAPI 直接回傳時**不會**被包含在 JSON 中，需要使用 Pydantic v2 的 `@computed_field`。
3. **避免 I/O 阻塞**：讀取伺服器本地檔案（Disk I/O）為阻塞行為。我們應該在 FastAPI 中使用 **同步路由（使用 `def` 而非 `async def`）**，這樣 FastAPI 會自動將其分配至執行緒池（Thread Pool）中執行，避免阻塞 Event Loop。

### 💡 核心設計實踐
* **`validation_alias`**：僅在**輸入驗證**時將中文欄位映射到英文變數，回傳 JSON 時依然輸出英文變數名稱。
* **`ConfigDict(populate_by_name=True)`**：允許同時透過變數名（如 `chinese`）或別名（如 `科目1`）來初始化模型，提升測試彈性。
* **`@computed_field`**：讓計算欄位（如 `total_score`）自動被序列化輸出。
* **`utf-8-sig` 編碼與同步讀取**：使用 `open(..., encoding='utf-8-sig')` 讀取伺服器本地的 CSV 檔案，防範 Windows Excel 產生的 BOM（Byte Order Mark）問題，並搭配標準 `def` 路由安全執行。

### 💻 FastAPI 整合程式碼範例

```python
import csv
import os
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, computed_field, ConfigDict

app = FastAPI(title="學生分數管理系統")

# 預先配置在伺服器端的 CSV 檔案路徑
CSV_FILE_PATH = "學生分數.csv"

# 定義單一學生的資料結構、驗證別名與計算屬性
class Student(BaseModel):
    # 允許使用屬性名稱（如 name）與驗證別名（如 姓名）兩種方式來進行資料代入或實例化
    model_config = ConfigDict(populate_by_name=True)

    # validation_alias：僅在輸入驗證（解析）時對照中文欄位，序列化輸出時仍會保留並輸出英文變數名稱。
    # 註：alias 則是會同時變更輸入驗證與輸出序列化的欄位別名。
    name: str = Field(validation_alias="姓名")
    chinese: int = Field(validation_alias="科目1")
    english: int = Field(validation_alias="科目2")
    math: int = Field(validation_alias="科目3")
    geography: int = Field(validation_alias="科目4")
    history: int = Field(validation_alias="科目5")
    social: int = Field(validation_alias="科目6")
    morality: int = Field(validation_alias="科目7")

    # 使用 Pydantic v2 的 @computed_field，回傳 JSON 時會自動包含此欄位
    @computed_field
    @property
    def total_score(self) -> int:
        return (
            self.chinese
            + self.english
            + self.math
            + self.geography
            + self.history
            + self.social
            + self.morality
        )

# API 回傳的標準包裹格式（Container Model）
class ScoreResponse(BaseModel):
    success: bool = True
    count: int
    students: list[Student]

# 注意：此處使用 def 而非 async def，FastAPI 會自動在個別執行緒中執行，避免 Disk I/O 阻塞主事件循環
@app.get(
    "/students/scores", 
    response_model=ScoreResponse,
    status_code=status.HTTP_200_OK,
    summary="讀取伺服器預置 CSV 並計算分數"
)
def get_student_scores():
    # 檢查伺服器端檔案是否存在
    if not os.path.exists(CSV_FILE_PATH):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"伺服器上找不到配置的 CSV 檔案：{CSV_FILE_PATH}"
        )
    
    try:
        students_list = []
        # utf-8-sig 能自動處理 Excel 產生的 BOM
        with open(CSV_FILE_PATH, encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for index, row in enumerate(reader, start=1):
                try:
                    # Pydantic 自動進行型別轉換與欄位映射
                    student = Student.model_validate(row)
                    students_list.append(student)
                except Exception as val_error:
                    raise HTTPException(
                        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        detail=f"CSV 檔案第 {index} 行資料驗證錯誤: {str(val_error)}"
                    )
        
        return ScoreResponse(
            count=len(students_list),
            students=students_list
        )

    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"伺服器讀取或解析 CSV 時發生錯誤: {str(e)}"
        )
```

