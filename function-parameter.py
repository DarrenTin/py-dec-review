# def summarize(*args):
#     print(sum(args))

# summarize(1, 2, 3, 4, 5, 6, 7, 8)
# summarize(123, 999, 248)

# def printinfo(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')

# printinfo(name='John', age=30, city='New York')

# def pos_only(a, b, /, c, d):
#     print(a, b, c, d)

# pos_only(1, 2, c=3, d=4)   # Valid
# pos_only(a=1, b=2, c=3, d=4)  # Error: a and b must be positional

def add(a, b):
    return a + b

# numbers = (3, 4)
# print(add(*numbers))  # Output: 7

# params = {'a': 5, 'b': 6}
# print(add(*params))  # Output: ab
# print(add(**params))  # Output: 11

# params = {'a': {'c': 5}, 'b': {'d': 6}}
# print(add(*params))  # Output: ab
# print(add(params['a']['c'], params['b']['d']))  # Output: 11

def append_value(val, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(val)
    return my_list

print(append_value(1))  # Output: [1]
print(append_value(2))  # Output: [2]
