
# Line Bot 完整教學：從 Echo Bot 到 Gemini AI 整合

## [線上說明](https://youtube.com/live/WoJWBVvuyWo)

> [!NOTE]
> **免費帳號限制**：Render 免費方案在無連線時會暫停服務，下一個連線需等約 20 秒才會回應。免費帳號僅適合學習用途，付費帳號則無此限制。

- ![Line Bot 架構示意圖](./images/pic18.png)

---

## 第 1 章：需求與環境準備

### 1.1 帳號需求
- Line 帳號
- GitHub 帳號
- Render 帳號（https://render.com/）

### 1.2 基礎 Echo Bot 所需套件（requirements.txt）

```
line-bot-sdk
flask
requests
gunicorn
```

### 1.3 Gemini 整合版額外套件

```
line-bot-sdk
flask
requests
gunicorn
google-genai
python-dotenv
```

### 1.4 環境變數（Render 或 .env 設定）

```
CHANNEL_ACCESS_TOKEN=xxxxxxxx
CHANNEL_SECRET=xxxxxxx
GEMINI_API_KEY=xxxxxxx
# 要求 Render 指定 Python 版本
PYTHON_VERSION=3.11.9
```

---

## 第 2 章：Line Messaging API 申請

### 2.1 官方帳號管理
- Line 官方帳號管理：https://manager.line.biz
- 申請開發者帳號：[https://developers.line.biz/zh-hant/](https://developers.line.biz/zh-hant/)

### 2.2 手動開啟 Messaging API 功能

網址：https://manager.line.biz/account

**設定 → 啟用 Messaging API**

![啟用 Messaging API](./images/pic1.png)

### 2.3 Line Message API 重要設定

#### 登入後，進入 Line Developers Console

![進入 Developers Console](./images/pic2.png)

#### 使用預設的 Providers，並建立一個 Messaging API Channel

![建立 Messaging API Channel](./images/pic3.png)

#### 在 Basic settings 取得 Channel Secret 密碼

![取得 Channel Secret](./images/pic4.png)

#### 在 Messaging API settings 設定 Webhook

![Messaging API settings（1）](./images/pic5.png)

![Messaging API settings（2）](./images/pic6.png)

---

## 第 3 章：GitHub Repo 與基礎 Echo Bot

### 3.1 Repo 設定參考

- [參考我的 Repo](https://github.com/roberthsu2003/line_bot)

![GitHub Repo 結構](./images/pic7.png)

### 3.2 基礎 Echo Bot：`index.py`

此版本為最簡單的 **Echo Bot**，將使用者傳入的訊息原封不動回傳。

```python
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 將使用者輸入的文字原封不動回傳
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

---

## 第 4 章：Render 部署設定

### 4.1 申請 Render 帳號

- [申請 Render 帳號](https://render.com/)

![Render 首頁](./images/pic8.png)

### 4.2 建立一個 Web Service

![建立 Web Service](./images/pic9.png)

### 4.3 連線至 GitHub Repo

![連線至 GitHub Repo](./images/pic10.png)

### 4.4 上傳 Repo 至 Render

![上傳 Repo](./images/pic11.png)

### 4.5 Render 部署設定

![Render 設定（1）](./images/pic12.png)

![Render 設定（2）](./images/pic13.png)

![Render 設定（3）](./images/pic14.png)

### 4.6 將 Render 的網址加入至 Line Webhook

> [!IMPORTANT]
> Webhook URL 的最後必須加上 `/callback`

![設定 Webhook URL（1）](./images/pic15.png)

![設定 Webhook URL（2）](./images/pic16.png)

### 4.7 設定環境變數

將 Line 的 **Channel Access Token** 與 **Channel Secret** 複製貼入 Render 環境變數設定。

![設定 Render 環境變數](./images/pic17.png)

---

## 第 5 章：進階整合 — Gemini AI（url_prompt 版）

此版本在原有 Echo Bot 基礎上，整合 Gemini AI。使用者在 Line 傳送訊息後，Bot 會呼叫 Gemini API 產生智慧回覆；同時支援透過 URL 路由（如 `/{問題}`）以瀏覽器查詢並以 HTML 格式呈現答案。

### 5.1 Render Build Command

```
pip install --upgrade pip && pip install -r requirements.txt
```

### 5.2 程式碼：`index.py`（url_prompt 版）

```python
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from google import genai
import os

app = Flask(__name__)
client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

@app.route("/")
@app.route("/<string:question>")
def index(question: str = ""):
    """透過 URL 路由接收問題，以 HTML 格式回傳 Gemini 的回覆"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{question},回應請輸出成為 html 格式"
    )
    html_format = response.text
    html_format = html_format.replace("```html", "").replace("```", "")
    return html_format

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """接收 Line 訊息，呼叫 Gemini 產生智慧回覆"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=event.message.text
    )
    message = TextSendMessage(text=response.text)
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

---

## 第 6 章：進階整合 — Gemini AI（webpage UI 版）

此版本在第 5 章的基礎上，進一步加入一個完整的網頁聊天介面，讓使用者也能直接透過瀏覽器與 Gemini 對話，達到「Line Bot + 網頁 UI」雙管道並行。

### 6.1 程式碼：`index.py`（webpage_prompt 版）

```python
from flask import Flask, request, abort, render_template_string, jsonify
from google import genai
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)
client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

@app.route("/")
def index():
    """提供網頁版聊天介面"""
    html = '''
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <title>Gemini 小助手 Chatbot</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f5f5f5; }
            .container { max-width: 500px; margin: 40px auto; background: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 2px 8px #ccc; }
            h1 { text-align: center; }
            #result { min-height: 100px; background: #f0f0f0; margin-top: 20px; padding: 15px; border-radius: 5px; }
            .btn { padding: 8px 20px; margin: 5px; border: none; border-radius: 5px; cursor: pointer; }
            .btn-start { background: #4CAF50; color: #fff; }
            .btn-clear { background: #f44336; color: #fff; }
            #question { width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Gemini 小助手 Chatbot</h1>
            <input type="text" id="question" placeholder="請輸入您的問題..." />
            <div>
                <button class="btn btn-start" onclick="startChat()">開始</button>
                <button class="btn btn-clear" onclick="clearAll()">清除</button>
            </div>
            <div id="result"></div>
        </div>
        <script>
            function startChat() {
                const q = document.getElementById('question').value.trim();
                if (!q) { alert('請輸入問題'); return; }
                document.getElementById('result').innerHTML = '請稍候...';
                fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ question: q })
                })
                .then(res => res.json())
                .then(data => {
                    document.getElementById('result').innerHTML = data.html || data.text || '無回應';
                })
                .catch(() => {
                    document.getElementById('result').innerHTML = '發生錯誤，請稍後再試';
                });
            }
            function clearAll() {
                document.getElementById('question').value = '';
                document.getElementById('result').innerHTML = '';
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route("/chat", methods=["POST"])
def chat():
    """接收網頁 AJAX 請求，呼叫 Gemini 並以 HTML 格式回傳"""
    data = request.get_json()
    question = data.get('question', '').strip()
    if not question:
        return jsonify({'error': '未輸入問題'}), 400
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{question},回應請輸出成為 html 格式"
        )
        html_format = response.text.replace("```html", "").replace("```", "")
        return jsonify({'html': html_format})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """接收 Line 訊息，呼叫 Gemini 產生智慧回覆"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=event.message.text
    )
    message = TextSendMessage(text=response.text)
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```
