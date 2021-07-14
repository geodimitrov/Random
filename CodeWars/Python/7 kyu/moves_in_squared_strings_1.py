def vert_mirror(string):
    substrings = string.split('\n')
    return '\n'.join(substr[::-1] for substr in substrings)


def hor_mirror(string):
    substrings = string.split('\n')
    return '\n'.join(substrings[::-1])


def oper(func, s):
    return func(s)