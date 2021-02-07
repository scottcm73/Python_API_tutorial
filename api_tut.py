
import json
from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd
import http.client
import os
GNews_API_Key=os.environ.get('GNews_API_KEY')

print(GNews_API_Key)
conn = http.client.HTTPSConnection("google-news.p.rapidapi.com")
headers = {
    'x-rapidapi-host': "google-news.p.rapidapi.com",
    'x-rapidapi-key': GNews_API_Key,
    }

conn.request("GET", "/v1/search?country=US&lang=en&q=Elon%20Musk", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

