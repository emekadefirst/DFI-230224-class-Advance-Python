import json
import requests

url = 'https://filmwharf.pythonanywhere.com/api'
response = requests.get(url)
print(response)

if response.status_code == 200:
    data = response.json()
    
    for x in data:
        name = x.fin_al[x.]
        print(name)
