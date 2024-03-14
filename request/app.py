# import requests
# from bs4 import BeautifulSoup

# def tech_news():
#     base_url = "https://www.tvcnews.tv/category/tech"
#     n = range(1, 17)
#     data_list = []
#     for i in n:
#         num = i
#         new_url = f"{base_url}/page/{num}/"
#         response = requests.get(new_url)
#         content = BeautifulSoup(response.text, 'html.parser')
#         for x in content.find_all("h3", {"class": "jeg_post_title"}):
#             data = x.text.strip()
#             data_list.append([data])  # Append scraped data to the list
#                 # Open the file outside the loop
#     with open("data.txt", "w", newline='') as file:
#         for item in data_list:
#             file.write("%s\n" % item)
#     return "Tech news on TVC successfully scrapped"
                
# tech_news()
# print("Done ✅")


import requests
from bs4 import BeautifulSoup

def tech_news():
    base_url = "https://www.tvcnews.tv/category/tech"
    n = range(1, 3)
    data_list = []
    for i in n:
        num = i
        new_url = f"{base_url}/page/{num}/"
        response = requests.get(new_url)
        content = BeautifulSoup(response.text, 'html.parser')
        for x in content.find_all("h3", {"class": "jeg_post_title"}):
            data = x.text.strip()
            data_list.append(data)  # Append scraped data to the list

    # Open the file outside the loop
    with open("data.txt", "w", newline='') as file:
        for item in data_list:
            # Remove brackets and write to file
            file.write("%s\n" % item)

    return "Tech news on TVC successfully scraped"

print(tech_news())
print("Done ✅")
