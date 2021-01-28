import requests
import json

quotes = requests.get('https://zenquotes.io/api/random')
# response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
print(quotes.status_code)
response_text=quotes.text
print(quotes.text)
quotes_json=quotes.json()
print(quotes_json)

for q in quotes_json:
    print(q['q'])
    print(q['a'])
