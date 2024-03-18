import requests
from bs4 import BeautifulSoup

base_url = "https://www.tvcnews.tv/category/tech"
response = requests.get(base_url)

content = BeautifulSoup(response.text, 'html.parser')
for new in content.find_all('article', {'class': 'jeg_post jeg_pl_md_2 format-standard'}):
    link_element = new.find('a')
    link = link_element.get('href')
    print(link)
    
    headline = new.find("h3", {"class": "jeg_post_title"})
    print(headline.text.strip())
    
    image_element = new.find("img", {"class" : "attachment-jnews-350x250 size-jnews-350x250 wp-post-image lazyautosizes lazyloaded"})
    jpg = new.get('src')
    print(jpg)
    
    

    
print("Done ✅")
    
    
    
    
    
    
    
    
    
    
# for img_tag in content.find_all("img", {"class": "attachment-jnews-350x250 size-jnews-350x250 wp-post-image lazyautosizes lazyloaded"}):
#     src = img_tag.get("src")
#     print(src)
# for y in content.find_all("h3", {"class": "jeg_post_title"}):
#     print(y.text.strip())
#     link = y.find("a")
#     if link:
#         print(link.get('href'))
# for x in content.find_all("img", {"class": "attachment-jnews-350x250 size-jnews-350x250 wp-post-image lazyautosizes lazyloaded"}):
#     print(x.text.strip())

    
