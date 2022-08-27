import json
import requests
people = requests.get('http://api.open-notify.org/astros.json')
json = people.json()
print(json)
print('the people currently in sace are:')
for p in json['people']:
    print(p['name'])
