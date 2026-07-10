# 實務應用三：AQI 空氣品質 CSV 與自訂驗證

本單元將對比前面的 JSON 解析，學習如何使用 Pydantic 解析 **CSV 格式** 的空氣品質資料。
主要學習重點包括：
1. 如何使用 Python 標準庫 `csv.DictReader` 讀取 CSV 資料。
2. 如何使用清單推導式批次驗證與解析 CSV 清單資料。
3. 如何將驗證並清洗後的模型資料，再次序列化並輸出回新 CSV 與 JSON 檔案。

---

## 1. 傳統 CSV 讀取方式 (不進行驗證)

在引入 Pydantic 之前，我們可以使用 Python 的 `csv.DictReader` 將 CSV 的每一列讀取為一個 `dict`。但這種方法無法對資料型別進行自動轉換與合法性檢查。

```python
#一般寫法
from csv import DictReader
with open('空氣品質aqi.csv',encoding='utf-8',newline='') as csvFile:
    dictReader:DictReader = DictReader(csvFile)
    aqi_list:list[dict] = list(dictReader)
    for item in aqi_list:
        print(item)
```

**輸出結果：**
```text
{'sitename': '屏東(枋山)', 'county': '屏東縣', 'aqi': '64', 'pollutant': '臭氧八小時', 'status': '普通', 'so2': '0.4', 'co': '0.18', 'o3': '58.1', 'o3_8hr': '60.0', 'pm10': '25', 'pm2.5': '14', 'no2': '2.1', 'nox': '2.4', 'no': '0.3', 'windspeed': '7.3', 'winddirec': '91', 'datacreationdate': '2024-03-15 09:00', 'unit': '', 'co_8hr': '0.1', 'pm2.5_avg': '12.5', 'pm10_avg': '25', 'so2_avg': '0', 'longitude': '120.651472', 'latitude': '22.260899', 'siteid': '313'}
{'sitename': '新北(樹林)', 'county': '新北市', 'aqi': '78', 'pollutant': '細懸浮微粒', 'status': '普通', 'so2': '0.8', 'co': '0.76', 'o3': '5.4', 'o3_8hr': '9.8', 'pm10': '44', 'pm2.5': '27', 'no2': '24.5', 'nox': '50', 'no': '25.4', 'windspeed': '0', 'winddirec': '109', 'datacreationdate': '2024-03-15 09:00', 'unit': '', 'co_8hr': '0.4', 'pm2.5_avg': '26.6', 'pm10_avg': '37', 'so2_avg': '0', 'longitude': '121.38352778', 'latitude': '24.94902778', 'siteid': '311'}
{'sitename': '屏東(琉球)', 'county': '屏東縣', 'aqi': '94', 'pollutant': '細懸浮微粒', 'status': '普通', 'so2': '2.9', 'co': '0.38', 'o3': '51.9', 'o3_8hr': '51.6', 'pm10': '74', 'pm2.5': '33', 'no2': '8', 'nox': '9.3', 'no': '1.3', 'windspeed': '1', 'winddirec': '61', 'datacreationdate': '2024-03-15 09:00', 'unit': '', 'co_8hr': '0.3', 'pm2.5_avg': '33', 'pm10_avg': '67', 'so2_avg': '2', 'longitude': '120.37722', 'latitude': '22.35222', 'siteid': '204'}
... (以下省略)
```



```python
#pydantic的validator

---

## 2. 使用 Pydantic 解析 CSV 列表

💡 **學習觀念 1：批次驗證與解析清單資料**
由於 `csv.DictReader` 讀出的是扁平的字典清單 `list[dict]`，在 Pydantic V2 中，我們可以直接使用清單推導式對每一列 `dict` 呼叫 `SiteName.model_validate(row)` 來進行批次解析，而不需要額外定義 `RootModel` 封裝。

💡 **學習觀念 2：mode='before' 清洗 CSV 空值**
與 JSON 解析相同，CSV 檔案中常有遺漏的欄位（空字串 `""`），透過 `@field_validator("pm25", mode='before')` 我們可以將這些空字串在轉型成 `float` 前預先替換為 `'0.0'`，避免轉型出錯。

```python
from pydantic import BaseModel, Field, field_validator
from csv import DictReader

class SiteName(BaseModel):
    site_name: str = Field(validation_alias='sitename')
    county: str = Field(validation_alias='county')
    aqi: int
    status: str = Field(validation_alias='status')
    pm25: float = Field(validation_alias='pm2.5')

    # 自訂的前置驗證器
    @field_validator("pm25", mode='before')
    @classmethod
    def whitespace_to_zero(cls, value):
        if value == '':
            return '0.0'
        return value

with open('空氣品質aqi.csv', encoding='utf-8', newline='') as csvFile:
    dictReader: DictReader = DictReader(csvFile)
    # 使用清單推導式進行批次驗證
    taiwanAQI = [SiteName.model_validate(row) for row in dictReader]

for site in taiwanAQI:
    print(site)
```
```

**輸出結果：**
```text
site_name='屏東(枋山)' county='屏東縣' aqi=64 status='普通' pm25=14.0
site_name='新北(樹林)' county='新北市' aqi=78 status='普通' pm25=27.0
site_name='屏東(琉球)' county='屏東縣' aqi=94 status='普通' pm25=33.0
site_name='臺南(麻豆)' county='臺南市' aqi=152 status='對所有族群不健康' pm25=61.0
site_name='高雄(湖內)' county='高雄市' aqi=148 status='對敏感族群不健康' pm25=57.0
... (以下省略)
```



```python
---

## 3. 將資料序列化為 JSON

💡 **學習觀念：使用 TypeAdapter 進行清單序列化**
當資料儲存為標準 Python 清單 `list[SiteName]` 時，無法直接呼叫 `model_dump_json()`。我們可以使用 `TypeAdapter` 對 `list[SiteName]` 進行包裝並調用 `dump_json()` 來輸出 JSON 陣列，或直接使用清單推導式將每個 model dump 為 dict。

```python
from pydantic import TypeAdapter

# 使用 TypeAdapter 將 Model 列表序列化為 JSON 陣列
json_bytes = TypeAdapter(list[SiteName]).dump_json(taiwanAQI)
print(json_bytes.decode('utf-8'))
```

**輸出結果：**
```text
'[{"site_name":"屏東(枋山)","county":"屏東縣","aqi":64,"status":"普通","pm25":14.0},{"site_name":"新北(樹林)","county":"新北市","aqi":78,"status":"普通","pm25":27.0}, ... (以下省略)]
```




```python
#pydantic的serilizing,轉換為python的資料結構
from pprint import pprint
from pydantic import TypeAdapter
# 使用 TypeAdapter 將 Model 列表轉換為字典列表
dumped_data = TypeAdapter(list[SiteName]).dump_python(taiwanAQI)
print(pprint(dumped_data, indent=2))

```

**輸出結果：**
```text
[ {'aqi': 64, 'pm25': 14.0, 'status': '普通', 'county': '屏東縣', 'site_name': '屏東(枋山)'},
  {'aqi': 78, 'pm25': 27.0, 'status': '普通', 'county': '新北市', 'site_name': '新北(樹林)'},
  {'aqi': 94, 'pm25': 33.0, 'status': '普通', 'county': '屏東縣', 'site_name': '屏東(琉球)'},
  {'aqi': 152, 'pm25': 61.0, 'status': '對所有族群不健康', 'county': '臺南市', 'site_name': '臺南(麻豆)'},
  {'aqi': 148, 'pm25': 57.0, 'status': '對敏感族群不健康', 'county': '高雄市', 'site_name': '高雄(湖內)'},
  ... (以下省略)
]
```



```python
---

## 4. 取得模型屬性欄位名稱

💡 **學習觀念：欄位後設資料反射 (Metadata Reflection)**
我們可以使用 `Model.model_fields.keys()` 來取得模型中所有定義的欄位名稱列表。這在需要動態寫入資料表頭或資料庫欄位時非常實用。

print(SiteName.model_fields.keys())
```

**輸出結果：**
```text
dict_keys(['site_name', 'county', 'aqi', 'status', 'pm25'])
```




```python
---

## 5. 將驗證後的資料存回 CSV 與 JSON

💡 **學習觀念 1：使用 csv.DictWriter 寫入檔案**
利用前面取得的 `SiteName.model_fields.keys()` 作為 `fieldnames`，搭配 `csv.DictWriter`。我們使用 `TypeAdapter(list[SiteName]).dump_python(taiwanAQI)` 將資料以字典列表導出，便能直接整批寫入新的 CSV 檔案。

💡 **學習觀念 2：匯出 JSON 檔案**
利用 `TypeAdapter(list[SiteName]).dump_json(taiwanAQI)` 產生 JSON 位元組，解碼後使用標準 `write` 方法寫入 json 檔案。

```python
#pydantic 儲存為csv檔
from csv import DictWriter
from pydantic import TypeAdapter

with open('新空氣品質aqi.csv',mode='w',encoding='utf-8',newline='') as csvFile:
    dictWriter:DictWriter = DictWriter(csvFile,fieldnames=SiteName.model_fields.keys()) #要用SiteName
    dictWriter.writeheader()
    dictWriter.writerows(TypeAdapter(list[SiteName]).dump_python(taiwanAQI))
```

```python
#pydantic 儲存為json檔
from pydantic import TypeAdapter

with open('新空氣品質aqi.json',mode='w',encoding='utf-8') as jsonFile:
    json_str = TypeAdapter(list[SiteName]).dump_json(taiwanAQI).decode('utf-8')
    jsonFile.write(json_str)
```

---

## 6. FastAPI 實務整合與最佳設計

當我們需要將此 CSV 解析與驗證邏輯整合至 FastAPI 專案中，且 **CSV 檔案已預先配置於伺服器端** 時，設計上會有以下調整：
1. **對外 API 欄位英文化**：輸入的 CSV 雖然是中文欄位（如 `sitename`, `county`），但 API 回傳的 JSON 應該是標準的英文 `snake_case`（如 `site_name`, `county`）。
2. **前置驗證與清洗**：使用 Pydantic 的 `@field_validator(..., mode='before')` 在 API 層面過濾掉因為儀器故障產生的空字串 `" "` 髒資料，避免型別轉型失敗。
3. **避免 I/O 阻塞**：使用同步的 `def` 路由處理本地 Disk I/O，以利 FastAPI 自動透過外部執行緒池執行，防止主事件循環被阻塞。

### 💻 FastAPI 整合程式碼範例

```python
import csv
import os
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, field_validator, ConfigDict

app = FastAPI(title="AQI CSV 空氣品質監測系統")

# 預先配置在伺服器端的 CSV 檔案路徑
CSV_FILE_PATH = "空氣品質aqi.csv"

# 定義單一觀測站點的資料結構、驗證別名與資料清洗邏輯
class SiteAQI(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    site_name: str = Field(validation_alias="sitename")
    county: str = Field(validation_alias="county")
    aqi: int
    status: str = Field(validation_alias="status")
    pm25: float = Field(validation_alias="pm2.5")

    # 前置驗證器：在型別檢查前，將空字串清洗為 0.0，避免轉型 float 錯誤
    @field_validator("pm25", mode='before')
    @classmethod
    def whitespace_to_zero(cls, value):
        if value == '':
            return '0.0'
        return value

# API 回傳的標準包裹格式（Container Model）
class ScoreResponse(BaseModel):
    success: bool = True
    count: int
    records: list[SiteAQI]

# 注意：此處使用 def 而非 async def，FastAPI 會自動在個別執行緒中執行，避免 Disk I/O 阻塞主事件循環
@app.get(
    "/aqi/csv-records", 
    response_model=ScoreResponse,
    status_code=status.HTTP_200_OK,
    summary="讀取伺服器預置 AQI CSV 檔案"
)
def get_aqi_csv_records():
    # 檢查伺服器端檔案是否存在
    if not os.path.exists(CSV_FILE_PATH):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"伺服器上找不到指定的 CSV 檔案：{CSV_FILE_PATH}"
        )
    
    try:
        records_list = []
        # utf-8-sig 能自動處理 Excel 產生的 BOM
        with open(CSV_FILE_PATH, encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for index, row in enumerate(reader, start=1):
                try:
                    # Pydantic 自動進行型別轉換與欄位映射
                    record = SiteAQI.model_validate(row)
                    records_list.append(record)
                except Exception as val_error:
                    raise HTTPException(
                        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        detail=f"CSV 檔案第 {index} 行資料驗證錯誤: {str(val_error)}"
                    )
        
        return ScoreResponse(
            count=len(records_list),
            records=records_list
        )

    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"伺服器讀取或解析 CSV 時發生錯誤: {str(e)}"
        )
```

