def special_number(number):
    if all((int(d) in range(1, 6) for d in str(number))):
        return 'Special!!'
    return 'NOT!!'

print(special_number(7))

