## Gemini 和 line bot整合

#### requirements.txt

```
line-bot-sdk
flask
requests
gunicorn
google-genai
python-dotenv
```

#### 環境變數

```
CHANNEL_ACCESS_TOKEN=xxxxxxxx
CHANNEL_SECRET=xxxxxxx
Gemini_API_KEY=xxxxxxx
#註解:要求render 指定python version
PYTHON_VERSION=3.11.9
```

#### Build Command

```
pip install --upgrade pip && pip install -r requirements.txt
```


#### 程式碼

**url_prompt版**

```python
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from google import genai
from dotenv import load_dotenv
import os

app = Flask(__name__)
client = genai.Client(api_key=os.environ['Gemini_API_KEY'])


line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

@app.route("/")
@app.route("/<string:question>")
def index(question:str=""):
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=f"{question},回應請輸出成為html格式")
    html_format = response.text
    html_format = html_format.replace("```html","").replace("```","")
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
    #response = model.generate_content(event.message.text)
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=event.message.text
    )
    message = TextSendMessage(text=response.text)
    line_bot_api.reply_message(event.reply_token, message)
```


**webpage_prompt版**

```python
from flask import Flask,request, abort, render_template_string, jsonify
from google import genai
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
# from dotenv import load_dotenv

# load_dotenv()

app = Flask(__name__)
client = genai.Client()

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

@app.route("/")
def index():
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
    data = request.get_json()
    question = data.get('question', '').strip()
    if not question:
        return jsonify({'error': '未輸入問題'}), 400
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=f"{question},回應請輸出成為html格式"
        )
        html_format = response.text.replace("```html","").replace("```","")
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
    
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=event.message.text
    )
    message = TextSendMessage(text=response.text)
    line_bot_api.reply_message(event.reply_token, message)
```