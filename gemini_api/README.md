# Gemini API

## 必需申請Gemini API key

### Google Gemini
- Google Gemini的免費版本，每分鐘限制呼叫60次. 
- Google Gemini文本生成的history歷史查閱，目前中文會出現亂碼
- Google Gemini可以解析圖片

### 1.登入:https://ai.google.dev

![](./images/pic1.png)

### 建立 API Key

![](./images/pic2.png)

### 安裝套件

```
> pip install google-generativeai
> pip install python-dotenv
```

### 載入api

```python
import google.generativeai as genai 
```

### 簡單範例
#### .env file

```
Gemini_API_KEY='您的API_KEY'
```

```python
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

genai.configure(api_key=os.environ['Gemini_API_KEY'])
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('我想要學習 演算法')
print(response.text)
```