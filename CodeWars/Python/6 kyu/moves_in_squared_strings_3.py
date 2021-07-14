def diag_1_sym(string):
    substrings = string.split('\n')
    substr_size = len(substrings[0])
    result = []

    for i in range(substr_size):
        word = ''
        for substr in substrings:
            word += substr[i]
        result.append(word)

    return '\n'.join(result)


def rot_90_clock(string):
    substrings = diag_1_sym(string).split('\n')
    return '\n'.join(substr[::-1] for substr in substrings)


def selfie_and_diag1(string):
    substrings = string.split('\n')
    diagonal_substrings = diag_1_sym(string).split('\n')
    result = [f'{substrings[i]}|{diagonal_substrings[i]}' for i in range(len(substrings))]
    return '\n'.join(result)


def oper(func, s):
    return func(s)