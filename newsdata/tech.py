import requests
from bs4 import BeautifulSoup

def politics():
    base_url = "https://www.tvcnews.tv/tech/"
    for num in range(1, 20):
        url = f"{base_url}page/{num}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for new in soup.find_all('article'):
            headlines = new.find('h3').text.strip()
            print(headlines)
            img = new.find('img')
            if img:
                image = img.get('src')
                print(image)
            else:
                print("N/A")
            li = new.find('a')
            link = li.get('href')
            print(link)
            print("\n")
    return {"Title" : headlines, "url": link, "image": image}
    