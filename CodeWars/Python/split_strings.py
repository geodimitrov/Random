def len_is_odd(string):
    return len(string) % 2 != 0


def split_string(string):
    res = []

    if len_is_odd(string):
        string += "_"

    for i in range(0, len(string), 2):
        res.append(string[i:i+2])

    return res

tests = [
    "abc",
    "abdjss"
]

for test in tests:
    print(split_string(test))