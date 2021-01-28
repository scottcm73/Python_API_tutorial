import requests
import json

# quotes = requests.get('https://zenquotes.io/api/random')
# # response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
# print(quotes.status_code)
# response_text=quotes.text
# print(quotes.text)
# quotes_json=quotes.json()
# print(quotes_json)



url = ('http://newsapi.org/v2/everything?'
       'q=Elon+Musk&'
       'from=2021-01-27&'
       'sortBy=popularity&'
       'apiKey=d205f0b691144bc0b08de0f03d89b894')

response = requests.get(url)

response_text= response.text

articles_json=response.json()


print(articles_json)