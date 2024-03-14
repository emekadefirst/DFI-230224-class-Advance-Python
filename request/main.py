import csv
import asyncio
import requests
from bs4 import BeautifulSoup
        
async def tech_news():
    base_url = "https://www.tvcnews.tv/category/tech"
    n = range(1, 17)
    data_list = []
    for i in n:
        num = i
        new_url = f"{base_url}/page/{num}/"
        response = requests.get(new_url)
        content = BeautifulSoup(response.text, 'html.parser')
        for x in content.find_all("h3", {"class": "jeg_post_title"}):
            data = x.text.strip()
            data_list.append([data])  # Append scraped data to the list
            # Write data to CSV file
            with open("data.csv", "w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data_list)
    
asyncio.run(tech_news())


print("Done")

