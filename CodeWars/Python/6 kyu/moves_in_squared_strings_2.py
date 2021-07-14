def rot(string):
    substrings = string.split('\n')[::-1]
    return '\n'.join(substr[::-1] for substr in substrings)


def selfie_and_rot(string):
    substrings = [substr + len(substr) * '.' for substr in string.split('\n')]
    return '\n'.join(substrings) + '\n' + rot('\n'.join(substrings))


def oper(func, s):
    return func(s)