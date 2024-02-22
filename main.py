# import requests

# url = "https://dummyjson.com/products"
# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     products = data['products']  
#     # product_data = []
#     for product in products:
#         title = product['title']
#         price = product['price']
#         print(f"{title} is worth ${price}")

from app import Case        
        
def activities():
    case = Case.objects.all()
        


