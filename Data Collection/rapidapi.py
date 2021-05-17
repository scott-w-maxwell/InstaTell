# VIA RAPID API
import requests
import json

username = ''
RAPID_API_KEY = '' 
url = "https://instagramdimashirokovv1.p.rapidapi.com/search/{username}"

headers = {
    'x-rapidapi-key': RAPID_API_KEY,
    'x-rapidapi-host': "InstagramdimashirokovV1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

data = json.loads(response.text)
print(data)
