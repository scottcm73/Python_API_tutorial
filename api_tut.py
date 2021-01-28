import requests
import json

people = requests.get('http://api.open-notify.org/astros.json')
# response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
print(people.status_code)
response_text=people.text

print(people.text)
people_json=people.json()
print(people_json)
print("Number of people in space: ", people_json['number'])
for p in people_json['people']:
    print(p['name'])
