import sys

class Wifi:
    def __init__(self, name, network, password, type):
        self.name = name
        self.network = network
        self.password = password
        self.type = type
    
    # Write a function create wifi according the the declared attribute
    def create_wifi(self): 
        print(f"Your wifi {self.name} has been created ")
        
    def connect(self):
        print("Do you want to connect?\n(a.) Yes\n(b.) No")
        response = str(input(">> ")).lower()
        if response == "a" or response == "yes":
            max_entry = 5
            entry = 0
            while entry < max_entry:
                password = str(input("Enter password: "))
                if password != self.password:
                    print("Connection not successful. Please try again.")
                else:
                    print("Connection successful.")
                    break  # Exit loop if connection is successful
                entry += 1
            else:
                print("Maximum number of attempts reached. Connection failed.")
           
        elif response == "b" or response == "no":
            print("Ok... Enjoy the rest of our service")
        else:
            print("Invalid request!")
            
        return "Connection mode!!!"

# print("You can now create your own wifi")

class MTN(Wifi):
    def create(self):
        return f"You've just created MTN wifi named {self.name} and your password is {self.password}"

wifi = MTN("vera", "syhbdf", "3456", "broadband")
# wifi.create_wifi()

print(wifi.create())

