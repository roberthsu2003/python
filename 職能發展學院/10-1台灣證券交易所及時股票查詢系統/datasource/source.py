# 範例採用台灣證券交易所
from selenium import webdriver
from .stockInfo import StockInfo
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/roberthsu2003/Downloads/chromedriver')
driver.set_window_position(-10000,0) #讓chrome視窗遠離
def getData(stock_number):
    stockInfo = StockInfo()
    stockInfo.id = stock_number
    url = "https://mis.twse.com.tw/stock/fibest.jsp?stock=" + stock_number
    try:
        #檢查driver的網址是否正確
        if driver.current_url == url: #如果現在chrome正在顯示的網址和輸入的網址是一樣的，要求chrome重新整理
            driver.refresh()
        else:
            print("新的網址")
            driver.get(url) #前往新網址
    except Exception as e:
        stockInfo.error = f"伺服器發生錯誤:{e}"
        return stockInfo


    driver.find_element_by_id("btnChangeToOdd").click() #程式模擬，按下網頁內的切換為盤中零股行情按鈕
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    title = soup.find(id=stock_number + "_n", class_="title").string
    #t_odd = soup.find(id=stock_number + "_t_odd").string #日期無法出現
    odd = soup.find(id=stock_number + "_z_odd").string
    diff_odd = soup.find(id=stock_number + "_diff_odd").string
    percent_odd = soup.find(id=stock_number + "_pre_odd").string
    tv_odd = soup.find(id=stock_number + "_tv_odd").string
    v_odd = soup.find(id=stock_number + "_v").string
    o_odd = soup.find(id=stock_number + "_o").string
    h_odd = soup.find(id=stock_number + "_h").string
    l_odd = soup.find(id=stock_number + "_l").string
    '''
    print("股票名稱",title)
    #print("成交時間", t_odd)
    print("成交價", odd)
    print("目前狀況", diff_odd)
    print("漲跌價差(百分比)", percent_odd)
    print("當盤_成交量", tv_odd)
    print("累積_成交量", v_odd)
    print("開盤價", o_odd)
    print("最高", h_odd)
    print("最低", l_odd)
    '''
    stockInfo.name = title
    stockInfo.open = o_odd
    stockInfo.close = odd
    stockInfo.high = h_odd
    stockInfo.low = l_odd
    stockInfo.diff = diff_odd
    stockInfo.percent = percent_odd
    stockInfo.tv_odd = tv_odd
    stockInfo.v_odd = v_odd
    return stockInfo

