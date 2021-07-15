def accum(string):
    new_string = '-'.join(f'{string[i].upper()}{string[i].lower() * i}' for i in range(len(string)))
    return new_string

print(accum("abcd"))
print(accum("RqaEzty"))

