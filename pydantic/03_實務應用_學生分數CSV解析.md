# 實務應用一：學生分數 CSV 解析

本單元將帶您進入第一個真實資料處理的實務範例。我們將使用 Python 標準庫的 `csv.DictReader` 讀取 CSV 檔案，並透過 Pydantic 進行資料格式對齊、自動轉型與資料驗證。

---

## 1. CSV 資料結構映射與 Pydantic 整合

💡 **學習觀念 1：欄位別名 (Field Alias) 的應用**
在實務上，外部 CSV 檔案的欄位名稱經常是中文或不符合 Python 變數命名規範的字元（例如 `科目1`、`科目2`）。我們可以使用 `Field(alias='科目1')` 來進行對照。這樣做有兩個好處：
1. **符合 PEP 8 命名規範**：Python 程式內可以使用具備明確語意的英文變數（如 `國文`、`英文`）。
2. **自動型別轉換**：CSV 讀出來的資料預設全都是字串，Pydantic 會自動將它們轉成 `int`。

💡 **學習觀念 2：在 Pydantic Model 中加入業務邏輯與屬性**
Pydantic 模型不僅能用來驗證資料，還能當作一般的 Python 類別來使用。我們可以在模型內宣告一般方法（如 `def total(self) -> int`）或使用屬性裝飾器（`@property def sum(self)`）來計算學生的分數總和。

💡 **學習觀念 3：以 RootModel 封裝外部清單**
當 CSV 檔案內含有多行學生資料時，我們可以用 `RootModel` 封裝 `list[Student]`。藉由實作 `__iter__` 與 `__getitem__` 魔術方法，我們便可以直接對整個 `Students` 實例進行 `for` 迴圈遍歷，或使用索引值（如 `students[0]`）來存取特定學生。

```python
import csv
from pydantic import RootModel, BaseModel, Field
from pprint import pprint

# 定義單一學生的資料結構與計算邏輯
class Student(BaseModel):
    姓名: str
    國文: int = Field(alias='科目1')
    英文: int = Field(alias='科目2')
    數學: int = Field(alias='科目3')
    地理: int = Field(alias='科目4')
    歷史: int = Field(alias='科目5')
    社會: int = Field(alias='科目6')
    品德: int = Field(alias='科目7')

    # 自訂計算總分的方法
    def total(self) -> int:
        return self.國文 + self.英文 + self.數學 + self.地理 + self.歷史 + self.社會 + self.品德
    
    # 自訂屬性來取得總分
    @property
    def sum(self) -> int:
        return self.國文 + self.英文 + self.數學 + self.地理 + self.歷史 + self.社會 + self.品德

# 使用 RootModel 封裝學生列表，並擴充為可迭代與可索引
class Students(RootModel):
    root: list[Student]

    def __iter__(self):
        return iter(self.root)
    
    def __getitem__(self, item):
        return self.root[item]

# 讀取 CSV 檔案並使用 Pydantic 進行解析與驗證
with open('學生分數.csv', encoding='utf8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    students = Students(reader)

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
534
534
467
467
476
476
503
503
515
515
470
470
512
512
495
495
490
490
498
498
486
486
558
558
478
478
509
509
475
475
506
506
499
499
524
524
510
510
499
499
527
527
465
465
527
527
465
465
519
519
404
404
531
531
531
531
490
490
527
527
475
475
560
560
434
434
507
507
512
512
538
538
533
533
501
501
515
515
453
453
534
534
542
542
475
475
500
500
491
491
406
406
500
500
```
