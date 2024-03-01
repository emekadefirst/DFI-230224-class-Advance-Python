# class Myclass:
#     def __init__(self, attribute1, attribute2):
#         self.attribute1 = attribute1
#         self.attribute2 = attribute2
        
#     def method(self):
#         result = self.attribute1 + self.attribute2
#         return f"Thank you here is {result}"
    
    
# obj = Myclass(10, 20)
# print(obj.method())

# class EncapsulationExample:
#         def __init__(self):
#             self.__private_attribute = 10

#         def get_private_attribute(self):
#             return self.__private_attribute
        
# obj = EncapsulationExample()
# print(obj.get_private_attribute())

class Parent:
    def method(self):
        print("Parent Method")
        

class Child(Parent):
    def method(self):
        print("Child Method")

obj = Child()
obj.method()
