import csv
import threading
import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch_content(session, url):
    async with session.get(url) as response:
        return await response.text()
    
async def write_to_csv(news):
    with open("news.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([news])

async def tech_news():
    base_url = "https://www.tvcnews.tv/category/tech"
    n = range(1, 17)
    async with aiohttp.ClientSession() as session:
        for i in n:
            num = i
            new_url = f"{base_url}/page/{num}/"
            html_content = await fetch_content(session, new_url)
            content = BeautifulSoup(html_content, 'html.parser')
            for x in content.find_all("h3", {"class": "jeg_post_title"}):
                news_title = x.text.strip()
                await write_to_csv(news_title)

async def sport_news():
    base_url = "https://www.tvcnews.tv/category/sport"
    n = range(1, 17)
    async with aiohttp.ClientSession() as session:
        for i in n:
            num = i
            new_url = f"{base_url}/page/{num}/"
            html_content = await fetch_content(session, new_url)
            content = BeautifulSoup(html_content, 'html.parser')
            for x in content.find_all("h3", {"class": "jeg_post_title"}):
                news_title = x.text.strip()
                await write_to_csv(news_title)

async def politics_news():
    base_url = "https://www.tvcnews.tv/category/politics"
    n = range(1, 17)
    async with aiohttp.ClientSession() as session:
        for i in n:
            num = i
            new_url = f"{base_url}/page/{num}/"
            html_content = await fetch_content(session, new_url)
            content = BeautifulSoup(html_content, 'html.parser')
            for x in content.find_all("h3", {"class": "jeg_post_title"}):
                news_title = x.text.strip()
                await write_to_csv(news_title)

asyncio.run(tech_news())
asyncio.run(sport_news())
asyncio.run(politics_news())

# Create threads for each asyncio function
thread1 = threading.Thread(target=tech_news)
thread2 = threading.Thread(target=sport_news)
thread3 = threading.Thread(target=politics_news)

# Start threads
thread1.start()
thread2.start()
thread3.start()

print("Done")
