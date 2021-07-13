import requests

res = requests.get('https://flask-robert.herokuapp.com/youbike')
jsonObj = res.json()
print(type(jsonObj))
areas=jsonObj['areas']
for area in areas:
    print(area)