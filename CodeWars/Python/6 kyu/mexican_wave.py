def wave(people):
    result = []

    for i, char in enumerate(people):
        if not char == ' ':
            result.append(people[:i] + char.upper() + people[i+1:])

    return result
