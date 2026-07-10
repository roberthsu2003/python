# 實務應用二：AQI 空氣品質 JSON 解析

本單元將帶您學習如何處理真實世界的複雜 JSON 資料。我們將直接解析環保署發布的 AQI 空氣品質資料，這份資料具有兩大特色：
1. **多層巢狀結構**：最外層是包含 metadata 與 `records` 列表的物件。
2. **髒資料（空字串）**：某些觀測站的數值可能缺漏（表現為空字串 `""`），如果直接讓 Pydantic 進行型別轉換會導致程式崩潰。

---

## 1. 巢狀 JSON 解析與前置驗證

💡 **學習觀念 1：使用 `model_validate_json()` 解析多層巢狀 JSON**
我們的目標是提取外層 JSON 內 `records` 欄位下的觀測站清單。因此我們定義了：
* `SiteName` 模型：對應單一觀測站的資訊，並利用 `Field(alias=...)` 來處理包含點號的 JSON 屬性名（如 `pm2.5`）。
* `Records` 模型：作為最外層的包裹，內含一個 `records: list[SiteName]` 屬性。

💡 **學習觀念 2：使用前置驗證器 (Before Validator) 預先清洗髒資料**
當外部資料的某個欄位可能為空字串 `""`，而我們宣告的型別是 `float` 時，Pydantic 的預設驗證器在嘗試將 `""` 轉為 `float` 時會直接失敗。
為了解決這個問題，我們必須使用：
```python
@field_validator("pm25", mode='before')
```
* `mode='before'` 裝飾器可以讓我們在 Pydantic 進行型別檢查與轉換**之前**，先對原始輸入資料（此處為字串）進行自訂處理。
* 在自訂的 `whitespace_to_zero` 方法中，如果偵測到值為空字串 `''`，我們主動將其替換為 `'0.0'` 字串，隨後交給 Pydantic 預設驗證器時，便能安全地將其轉型為浮點數 `0.0`。

```python
#paydntic validator josn檔
from pydantic import BaseModel,Field,field_validator

class SiteName(BaseModel):
    站點名稱:str = Field(alias='sitename')
    城市:str = Field(alias='county')
    aqi:int
    品質:str = Field(alias='status')
    pm25:float =  Field(alias='pm2.5') 

    #自訂的驗證
    @field_validator("pm25",mode='before') #pydantic有自已的validator和自訂的validator,如果使用它的預設是先做預設的validator,目前欄位內會有空字串'',轉成float會出錯,所以必需先讓自訂的validator先運做,mode='before'
    @classmethod
    def whitespace_to_zero(cls,value):
        #print(f'{type(value)=}') #value值可以知道預設還是自訂的validator先做
        if value == '':
            return '0.0'
        else:
            return value

class Records(BaseModel):
    records:list[SiteName]

with open('空氣品質aqi.json',mode='r',encoding='utf-8') as readFile:
    json_str = readFile.read()
    taiwanAQI = Records.model_validate_json(json_str)
for sitename in taiwanAQI.records:
    print(sitename)
```

**輸出結果：**
```text
站點名稱='屏東(枋山)' 城市='屏東縣' aqi=64 品質='普通' pm25=14.0
站點名稱='新北(樹林)' 城市='新北市' aqi=78 品質='普通' pm25=27.0
站點名稱='屏東(琉球)' 城市='屏東縣' aqi=94 品質='普通' pm25=33.0
站點名稱='臺南(麻豆)' 城市='臺南市' aqi=152 品質='對所有族群不健康' pm25=61.0
站點名稱='高雄(湖內)' 城市='高雄市' aqi=148 品質='對敏感族群不健康' pm25=57.0
... (以下省略)
```

---

## 2. FastAPI 實務整合與最佳設計

當我們需要將此 AQI JSON 解析邏輯整合至 FastAPI 專案中，且 **JSON 檔案已預先配置於伺服器端** 時，設計上會有以下調整：
1. **對外 API 欄位設計**：輸入的原始 JSON 欄位（如 `sitename`, `pm2.5`）可透過 `validation_alias` 映射到 PEP 8 的 Python 變數名（如 `site_name`, `pm25`），讓 API 回傳的 JSON 回應欄位保持統一的命名規範。
2. **前置驗證與清洗**：使用 Pydantic 的 `@field_validator(..., mode='before')`，在 API 層面過濾掉因為儀器故障產生的空字串 `" "` 髒資料，避免型別轉型失敗。
3. **避免 I/O 阻塞**：使用同步的 `def` 路由處理本地 Disk I/O，以利 FastAPI 自動透過外部執行緒池執行，防止主事件循環被阻塞。

### 💻 FastAPI 整合程式碼範例

```python
import os
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, field_validator, ConfigDict

app = FastAPI(title="AQI 空氣品質監測系統")

# 預先配置在伺服器端的 JSON 檔案路徑
JSON_FILE_PATH = "空氣品質aqi.json"

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
class RecordsResponse(BaseModel):
    success: bool = True
    count: int
    records: list[SiteAQI]

# 注意：此處使用 def 而非 async def，FastAPI 會自動在個別執行緒中執行，避免 Disk I/O 阻塞主事件循環
@app.get(
    "/aqi/records", 
    response_model=RecordsResponse,
    status_code=status.HTTP_200_OK,
    summary="讀取伺服器預置 AQI JSON 檔案"
)
def get_aqi_records():
    # 檢查伺服器端檔案是否存在
    if not os.path.exists(JSON_FILE_PATH):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"伺服器上找不到指定的 JSON 檔案：{JSON_FILE_PATH}"
        )
    
    try:
        # 讀取 JSON 檔案內容
        with open(JSON_FILE_PATH, mode='r', encoding='utf-8') as file:
            json_str = file.read()
            
        # 定義內部的解析模型，結構對應外層 JSON {"records": [...]}
        class RecordsParser(BaseModel):
            records: list[SiteAQI]
            
        # 直接使用 model_validate_json 進行高效的 Rust 底層解析與驗證
        parsed_data = RecordsParser.model_validate_json(json_str)
        
        return RecordsResponse(
            count=len(parsed_data.records),
            records=parsed_data.records
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"伺服器讀取或解析 JSON 時發生錯誤: {str(e)}"
        )
```


