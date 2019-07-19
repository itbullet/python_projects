import requests

#print(requests.get('https://api.github.com'))

if requests.get('https://api.github.com').status_code == 200:
    print("Success!")
elif requests.get('https://api.github.com').status_code == 404:
    print("Not found.")