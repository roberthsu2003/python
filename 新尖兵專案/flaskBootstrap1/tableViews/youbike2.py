from flask import Blueprint,render_template
import requests
from requests import ConnectionError,ConnectTimeout,HTTPError,TooManyRedirects

youbikeApp = Blueprint('youbike',__name__)
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v3/youbike_immediate.json'

@youbikeApp.route('/table/youbike')
@youbikeApp.route('/table/youbike/<region>')
def youbike(region):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except ConnectionError as e:
        print(e)
    except ConnectTimeout as e:
        print(e)
    except HTTPError as e:
        print(e)
    except TooManyRedirects as e:
        print(e)
    except:
        print('error')
    return render_template('youbike.html')