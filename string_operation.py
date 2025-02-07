# name = 'Xie Zi Tong'
# print(name[4::-1])  # [start:end:direction]
# print(f"her name is {name}") # formatted string
# print(len(name)) # 11 (including whitespace)
# print(len(name.replace(" ", ""))) # 9 (excluding whitespace)
# print("".join(name.split())) # XieZiTong
# print(len("".join(name.split()))) # 9
# # tip: strip() only remove the leading whitespace
# print(name.find('i')) # 1
# print(name.find('i', 2)) # 5 (second 'i', count afterward from index '2' which is 'e')

# paragraph = 'Happy dully dog is jumping across the stunning radioactived river'
# task 1: find all indexes of a specific character
# specific_char = 'a'
# count = 0
# for i in range(len(paragraph)):
#     now_char = paragraph[i]
#     if(now_char == specific_char):
#         count += 1
#         print(f'count {count}: {i}')

# task 2: count number of occurance of each character from a to z
# alphabets = 'abcdefghijklmnopqrstuvwxyz'
# paragraph = paragraph.lower()
# for a in alphabets:
#     print(f'{a}: {paragraph.count(a)}')

