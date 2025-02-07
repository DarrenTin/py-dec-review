a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (values are equal)
print(a is b)  # False (different objects in memory)

values = [True, False, True]
if any(values):
    print("At least one is True")  # True if at least one condition is true

if all(values):
    print("All are True")  # True only if all conditions are true