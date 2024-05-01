## Gemini 和 line bot整合

#### requirements.txt

```
line-bot-sdk
flask
requests
gunicorn
google-generativeai
python-dotenv
```

#### 環境變數

```
CHANNEL_ACCESS_TOKEN=xxxxxxx
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

```python
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()


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
    genai.configure(api_key=os.environ['Gemini_API_KEY'])
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(event.message.text)
    message = TextSendMessage(text=response.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```