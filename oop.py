# Defining a class
class Dog:
    def __init__(self, name, breed):
        self.name = name  # Attribute
        self.breed = breed

    def bark(self):  # Method
        return f"{self.name} says Woof!"

# Creating objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

print(dog1.bark())  # Buddy says Woof!
print(dog2.name)    # Max
