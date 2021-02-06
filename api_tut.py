import requests
import json
import http.client
from datetime import datetime 
import os


url = "https://google-news.p.rapidapi.com/v1/topic_headlines"

qugerystrin = {"lang":"en","country":"US","topic":"technology"}
GNews_API_KEY = os.getenv('GNews_API_KEY')
headers = {
    'x-rapidapi-key': GNews_API_KEY,
    'x-rapidapi-host': "google-news.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)