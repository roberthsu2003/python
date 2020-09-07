# Line Notify服務
## 整合LINE Notify讓訊息發送至Line群組

### 申請步驟
#### 1. 登入至[https://notify-bot.line.me/my/](https://notify-bot.line.me/my/). 

#### 2. 登入您自已的line帳號  
![](line_log_in.png)

#### 3. 點選發行存取權杖  
![](image1.png)

#### 4. 建立發行服務
	- 按下發行後,您的line將會收到提醒通知
	- 記得在line內將line Notify加入到您想要加入的line群組內
	
![](image2.png)  

#### 5.保留發行權杖(沒有保留,未來將無法找到這個金鑰)  
![](image3.png)

#### 6.line會建立一個新的連動服數
![](image5.png)

### 安裝line的開發者套件
	pip install lineTool
![](image6.png)

### 安裝requests套件
	pip install requests
![](image7.png)

### 測試是否安裝成功  
```python
>>> import lineTool
>>> token = "請使用您剛剛取得的金鑰"
>>> msg = "Python 語言整合通訊軟體,恭喜您"
>>> response=lineTool.lineNotify(token,msg)
>>> if response == 200:
	    print("傳送成功")
	else:
	    print("傳送失敗")
```

![以上為程式碼畫面](image8.png) 
 
![以上為line的畫面](image9.png)




