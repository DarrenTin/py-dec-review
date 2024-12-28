# counter = 1
# while counter < 5:
#     print(counter)
#     counter += 1
# print('Last =', counter)

# choice = 'y'
# while choice == 'y':
#     print('Your balance:')
#     choice = input('Check balance (y/n):')
# print('Loop terminated')

while True:
    answer = input('Do you want to continue (y/n): ')
    if answer == 'n':
        break
    print('X' * 50)