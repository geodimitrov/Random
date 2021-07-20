def likes(names):
    result = None

    if not names:
        result = f'no one likes this'
    elif len(names) == 1:
        result = f'{names[0]} likes this'
    elif len(names) == 2:
        result = f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        result = f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        result = f'{names[0]}, {names[1]} and {len(names) - 2} others like this'

    return result
