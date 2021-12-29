def parse(data):
    value = 0
    result = []

    for c in data:
        if c == 'i':
            value += 1
        elif c == 'd':
            value -= 1
        elif c == 's':
            value **= 2
        elif c == 'o':
            result.append(value)

    return result
