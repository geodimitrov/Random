def create_phone_number(n):
    number = ''.join(str(el) for el in n)
    phone_number = f'({number[:3]}) {number[3:6]}-{number[6:]}'
    return phone_number

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))