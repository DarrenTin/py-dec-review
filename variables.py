# name = "Alice"
# income = 123.45

# various ways to format variables when printing
# print("Name: {}, Income: {},".format(name, income))
# print(f"Name: {name}, income: {income}")
# print(f"Name: %s, income: %.1f" % (name, income))
# print(29, 1, 2025, sep="-")

# print dict
# data = {"name": name, "income": income}
# print("Name: {name}, Income: {income}".format(**data))

# global variable and function type
# def f():
#     global income
#     income = 789.12

# print(type(f))
# f()
# print(income)


# del f
# f()

# a, b = (1, 2, 3, 4), (5, 6, 7, 8)
# a, b = b, a
# print(a, b)

# x = 10
# y = x
# print(id(x), id(y))  # Same memory location for immutable types

# args
# def greet(first_name, *args):
#     print(f"Hello, {first_name}!")
#     print("Other greetings:", args)

# greet("Alice", "Hi", "Bonjour", "Hola", "Konichiwa")

# coordinates = (10, 20)
# print(coordinates)

# unique_numbers = {1, 2, 3, 3, 4, 4}
# print(unique_numbers) # {1, 2, 3, 4}

# set_a = {2, 4}
# set_b = {4, 8, 9}
# print(set_a.union(set_b)) # {2, 4, 8, 9}
# print(set_a | set_b) # {2, 4, 8, 9}
# print(set_a.intersection(set_b)) # {4}
# print(set_a & set_b) # {4}
# print(set_b - set_a) # {8, 9}

# text = "amor fati"
# print(len(text)) # 9
# print(text[5:9]) # fati

# cubes = [x**3 for x in range(3, 7)]
# print(cubes) # [27, 64, 125, 216]

# person = {"name": "Alice", "age": 30}
# print(person.keys()) # dict_keys(['name', 'age'])
# print(person.values()) # dict_values(['Alice', 30])

# dict1 = {"name": "Alice"}
# dict2 = {"age": 30}
# merged = {**dict1, **dict2}
# print(merged)

# numbers = [i for i in range(1, 6)]
# squares = list(map(lambda x: x**2, numbers)) # [1, 4, 9, 16, 25]
# print(squares)

# from collections import namedtuple
# Person = namedtuple("Person", ["name", "age"])
# p = Person(name="Alice", age=30)
# print(p.name)

