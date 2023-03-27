import requests
url = 'https://udn.com/news/story/7324/7059404'
r = requests.get(url)
print(type(r))



r.status_code



r.text
