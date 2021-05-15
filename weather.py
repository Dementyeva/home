import requests
import pprint
import datetime

city = 'Kyiv'
API_KEY = 'e4f214a152c372e95b3e78e0547b1e0c'
days = 5

url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}'
response = requests.get(url)

data = response.json()

print("temp:",data['list'][0]['main'])
print("conditions:",data['list'][0]['weather'])
print("time:",data['list'][0]['dt_txt'])
print("wind:",data['list'][0]['wind'])



pprint.pprint(response.json())
print(datetime.datetime.utcfromtimestamp(1620440457))



