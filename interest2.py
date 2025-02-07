house = 514500
loan_percentage = 0.9
loan = house * loan_percentage
self = house - loan

rate = 0.044
year = 35

simple_ir = loan * rate * year  # I = PRT
print(f"{simple_ir:.2f}")

culmulative = 0
# for i in range(35):
#     repay = loan * rate
#     loan -= repay
#     culmulative += repay
#     print(f'{repay: .0f} -{culmulative: .0f}')

