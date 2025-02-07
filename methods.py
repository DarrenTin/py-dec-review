# class Book:
#     count = 0
#     def __init__(self, title):
#         self.title = title
#         Book.count += 1
    
#     @classmethod
#     def get_book_count(cls):
#         return cls.count
    
# class Fiction(Book):
#     def __init__(self, title, author):
#         super().__init__(title)
#         self.author = author
    
#     def get_author(self):
#         return self.author

# book1 = Book("To Kill a Mockingbird")
# book2 = Book("Love of the Dog")
# book3 = Fiction("Harry Potter", "Martin")

# print(Book.get_book_count())  # Output: 3


# class Builder:
#     def __init__(self):
#         self.result = []

#     def add(self, item):
#         self.result.append(item)
#         return self  # Return the instance for chaining

#     def build(self):
#         return self.result

# builder = Builder()
# final_result = builder.add("a").add("b").add("c")
# print(final_result)  # Output: ['a', 'b', 'c']

