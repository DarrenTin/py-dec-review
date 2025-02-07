# loop dict
# person = {"name": "Alice", "age": 25}
# for key, value in person.items():
#     print(f"{key}: {value}")

# loop enum
# colors = ["red", "blue", "green"]
# for index, color in enumerate(colors):
#     print(f"Index {index+1}: {color}")

# Multiplication table
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} x {j} = {i * j}")

# for i in range(24, 25):
#     for j in range(1, 13):
#         print(f"{j} x {i} = {i * j}")
#     print()

# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 90, 95]
# for name, score in zip(names, scores):
#     print(f"{name}: {score}")

# Map example
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)

# Filter example
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
