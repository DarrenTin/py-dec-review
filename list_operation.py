# names = ['zhu Yu Tong', 'Lim Jia Lei', 'Hsiao Tsin Tzi', 'Xie Zi Tong', 'To Khei Kit', 'Zhang Bo Han', '123', '.,.;']
# names.append('Teo Cheng You')
# print(names)
# names.insert(2, 'Lim Wei Ping') # directly become names[2], while original push to names[3]
# print(names)
# print('Xie Zi Tong' in names) # True
# print('Chai Chang Rong' in names) # False
# names.sort() # symbol, then 1-9, then A-Z, then a-z
# print(names)
# names.sort(reverse=True) # sort reversely
# print(names)

numbers = [1, 3, 5, 7]
numbers.append([2, 4, 6]) # append as single list (2-dimentional)
numbers.extend([2, 4, 6]) # append each content in list
print(numbers)