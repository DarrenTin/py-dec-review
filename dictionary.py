digit_mapping = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
}
for digit in '6588547993':
    # if digit in digit_mapping:
    print(digit_mapping.get(digit, '?'), end=' ')