from flask import Blueprint,render_template
import requests

tableApp = Blueprint('table_page',__name__)
apikey = '84a024b0-1d85-460c-b330-d96b9ea12cb9'
url = 'https://data.epa.gov.tw/api/v1/aqx_p_137?format=csv&offset=0&limit=1000&api_key=84a024b0-1d85-460c-b330-d96b9ea12cb9'

@tableApp.route('/table')
def table():
    return render_template('table.html',name='table')