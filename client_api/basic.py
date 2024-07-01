import requests

endpoint = " http://127.0.0.1:8000/product/"
response = requests.post(endpoint, json={'name': 'pasteque', 'content':'just pasteque', 'price':20})
 
print(response.json())
print(response.status_code)
#HTTP request --> HTML
#REST API HTTP --> JSON Javascript objet  notation