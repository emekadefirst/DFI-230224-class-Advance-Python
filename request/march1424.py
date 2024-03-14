import requests
from bs4 import BeautifulSoup

base_url = "https://www.tvcnews.tv/category/tech"
response = requests.get(base_url)

content = BeautifulSoup(response.text, 'html.parser')
for y in content.find_all("h3", {"class": "jeg_post_title"}):
    print(y.text.strip())
    link = y.find("a")
    if link:
        print(link.get('href'))

    
