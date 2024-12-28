a = 0b1011
b = 0b0111
print(bin(a & b)) # and
print(bin(a | b)) # or
print(bin(a ^ b)) # xor

# ~ = -(n + 1)
c = 3
print(~3)

# << 0010      -> 0100
print(bin(0b0010 << 1))
print(bin(0b0010 << 2))
print(bin(0b0010 >> 1))