from flask import Blueprint,render_template
import requests
import os
import csv

tableApp = Blueprint('table_page',__name__)
apikey = '84a024b0-1d85-460c-b330-d96b9ea12cb9'
url = 'https://data.epa.gov.tw/api/v1/aqx_p_137?format=csv&offset=0&limit=200&api_key=84a024b0-1d85-460c-b330-d96b9ea12cb9'

@tableApp.route('/table')
def table():
    if not os.path.exists('./csv/新北市.csv'):
        print("下載中")
        response = requests.get(url)
        if response.status_code == 200:
            print("下載成功")
            with open('./csv/新北市.csv',mode='w',encoding='utf-8') as file:
                file.write(response.text)
            print('存檔完成')

    with open('./csv/新北市.csv',mode='r',encoding='utf-8') as file:
        next(file)
        csvReader = csv.reader(file)
        datalist = list(csvReader)
    print(len(datalist))

    return render_template('table.html',name='table',datalist=datalist)