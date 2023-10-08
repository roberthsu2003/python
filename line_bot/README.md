
# line_bot
- python和linebot的使用
- ![](./images/pic18.png)

## 需求
- line帳號
- github帳號
- render帳號(https://render.com/)

## python套件需求
- line-bot-sdk
- flask
- requests
- gunicorn

## line-bot(line-MessageAPI)申請
- ### 申請開發者[https://developers.line.biz/zh-hant/](https://developers.line.biz/zh-hant/)


![](./images/pic1.png)

 - ### Line-MessageAPI的重要設定事項

	 - #### 登入後,進入Line Developers Console

	   ![](./images/pic2.png) 

	 - #### 使用預設的Providers(youngTalk),並且建立一個Messaging API Channels.  


		![](./images/pic3.png)
		
	 - #### 在Basic settings最重要的是取得Channel secret的密碼


		![](./images/pic4.png)
		
	 - #### 在Messaging API settings

		![](./images/pic5.png)
	
		![](./images/pic6.png)
		
		
## github repo內的設定

- ### [參考我的repo](https://github.com/roberthsu2003/line_bot)

- ![](./images/pic7.png)

- ### index.py

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
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

- ### requirements.txt

```
line-bot-sdk
flask
requests
gunicorn
```
		
## render內的設定

- ### [申請render帳號](https://render.com/)
- ![](./images/pic8.png)
- ### 建立一個web Service
- ![](./images/pic9.png)
- ### 使用連線至github repo
- ![](./images/pic10.png)
- ### 上傳repo至render
- ![](./images/pic11.png)
- ### render上傳的設定
- ![](./images/pic12.png)
- ![](./images/pic13.png)
- ![](./images/pic14.png)
- ### 將render的網址加入至Line Message內,記得最後加上/callback
- ![](./images/pic15.png)
- ![](./images/pic16.png)
- 最後將line的channel access token copy至render,還有channel secret copy 至 render
- ![](./images/pic17.png)

		



