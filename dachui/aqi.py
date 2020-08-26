import urllib3
import certifi

csv_url = "https://opendata.epa.gov.tw/api/v1/AQI?%24skip=0&%24top=1000&%24format=csv"
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
response=http.request('GET', csv_url)
file=open('空氣品質指標.csv', 'wb')
file.write(response.data)
file.close()
