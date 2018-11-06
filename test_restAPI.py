import requests
from flask import Flask, json

response = requests.get('http://localhost:5000/')

data = json.loads(response.text)

try:
    for item in data['Domains']:
        print(item['name'], item['resolution_url'])
except:
    print("Error")

print(data['Searches'])
