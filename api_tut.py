import requests
import json
import http.client
from datetime import datetime 
import os


url = "https://google-news.p.rapidapi.com/v1/topic_headlines"

querystring = {"lang":"en","country":"US","topic":"technology"}
API_KEY = os.environ.get('API_KEY')
headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "google-news.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)