"""In a Shop, they sell only one brand of drink"""

class Shop:
    def __init__(self, name, brand, quantity):
        self.name = name
        self.brand = brand
        self.quantity = quantity
        
        
        
        
    def sell(self):
        print(f"We sell only {self.brand}, and we have {self.quantity}")
        
    def buy(self):
        amt = int(input("How many are you buying "))
        print(f"I want to buy {amt} {self.brand}")
        rem = self.quantity - amt
        print(f"We now have {rem} {self.name} left")
        
class Mall(Shop):
    print("Done!!!!!")
        
pepsi = Shop("Joyce drinks", "Pepsi", 20)
print()
pepsi.sell()
pepsi.buy()