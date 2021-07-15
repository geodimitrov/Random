def diag_2_sym(string):
    substrs = string.split()[::-1]
    result = []

    for i in range(len(substrs) - 1, -1, -1):
        new_substr = ''
        for substr in substrs:
            new_substr += substr[i]
        result.append(new_substr)

    return '\n'.join(result)

def rot_90_counter(string):
    substrs = diag_2_sym(string).split()
    return '\n'.join(substr[::-1] for substr in substrs)

def selfie_diag2_counterclock(string):
    init_substrs = string.split()
    diag_substrs = diag_2_sym(string).split()
    rot_90_substrs = rot_90_counter(string).split()

    return '\n'.join([init_substrs[i] + '|' + diag_substrs[i] + '|' + rot_90_substrs[i] for i in range(len(init_substrs))])

def oper(func, s):
    return func(s)