money = 30,000,000
print(money)
print(type(money))

money = 30_000_000
print(money)
print(type(money))

money = 15E10
print(money)
print(type(money))

money = 15E-10
print(money)
print(type(money))

print('='*50)

x = 0b1010 # base 2
print(x)
print(type(x))

x = 0o12 # base 8
print(x) 
print(type(x))

x = 0xAF # base 16
print(x)
print(type(x))

x = 10
print(bin(x))
print(oct(x))
print(hex(x))

print('='*50)

print(6 / 3.1) # always float
print(6 // 3.1) # floor
print(6 % 3.1) # remainder
print(6 ** 3.1) # exponetial