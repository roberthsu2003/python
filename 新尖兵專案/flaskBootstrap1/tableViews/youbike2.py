from flask import Blueprint,render_template,abort
import requests,json
from requests import ConnectionError,ConnectTimeout,HTTPError,TooManyRedirects

youbikeApp = Blueprint('youbike',__name__)
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
@youbikeApp.errorhandler(500)
def internal_server_error(error):
    return render_template('error404.html'), 500

@youbikeApp.route('/table/youbike',defaults={'region':None})
@youbikeApp.route('/table/youbike/<region>')
def youbike(region):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except ConnectionError as e:
        abort(500)
    except ConnectTimeout as e:
        abort(500)
    except HTTPError as e:
        abort(500)
    except TooManyRedirects as e:
        abort(500)
    except:
        abort(500)

    jsonObject = response.json()
    sareas = list({siteDict['sarea'] for siteDict in jsonObject})

    if region is None:
        dataDict = dict()
        for key in sareas:
            regionList = [item for item in jsonObject if item['sarea'] == key]
            dataDict[key] = regionList

        for key,value in dataDict.items():
            print(key)
            print(value)
            print("=========")

        return render_template('youbike.html', data=dataDict, regions=sareas)
    else:
        areaList=[item for item in jsonObject if item['sarea'] == region]
        return render_template('youbike1.html', data=areaList, regions=sareas,region=region)

@youbikeApp.route('/table/youbike/api/regions')
def regions_api():
    try:
        response = requests.get(url)
        response.raise_for_status()
    except ConnectionError as e:
        abort(500)
    except ConnectTimeout as e:
        abort(500)
    except HTTPError as e:
        abort(500)
    except TooManyRedirects as e:
        abort(500)
    except:
        abort(500)

    jsonObject = response.json()
    sareas = list({siteDict['sarea'] for siteDict in jsonObject})
    return json.dumps(sareas,ensure_ascii=False)

@youbikeApp.route('/table/youbike/api')
def youbike_api():
    try:
        response = requests.get(url)
        response.raise_for_status()
    except ConnectionError as e:
        abort(500)
    except ConnectTimeout as e:
        abort(500)
    except HTTPError as e:
        abort(500)
    except TooManyRedirects as e:
        abort(500)
    except:
        abort(500)

    jsonObject = response.json()
    sareas = list({siteDict['sarea'] for siteDict in jsonObject})
    dataDict = dict()
    for key in sareas:
        regionList = [item for item in jsonObject if item['sarea'] == key]
        dataDict[key] = regionList

    return json.dumps(dataDict,ensure_ascii=False)

@youbikeApp.route('/table/youbike/api/<region>')
def youbike_api1(region):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except ConnectionError as e:
        abort(500)
    except ConnectTimeout as e:
        abort(500)
    except HTTPError as e:
        abort(500)
    except TooManyRedirects as e:
        abort(500)
    except:
        abort(500)

    jsonObject = response.json()
    sareas = list({siteDict['sarea'] for siteDict in jsonObject})
    dataDict = dict()
    for key in sareas:
        regionList = [item for item in jsonObject if item['sarea'] == key]
        dataDict[key] = regionList

    dataList = dataDict[region]

    return json.dumps(dataList,ensure_ascii=False)
