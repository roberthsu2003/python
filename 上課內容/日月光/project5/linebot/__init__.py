import requests
token = "KDkQLircjHImzJKTPcXKChQo0LlC5W1s3UVl9V3R9K6"
def sendLineNotify( msg, picURI):
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization":"Bearer " + token}
    payload= {"message":msg}
    files = {"imageFile":open(picURI,'rb')}
    response=requests.post(url, headers = headers, params = payload,files = files)
    return response.status_code