import requests

genderapi = 'https://api.genderize.io?name='

a=requests.get(genderapi+'peter')
print(a.json())