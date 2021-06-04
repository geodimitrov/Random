def scale_horizontally(string, k):
    result = []

    for str in string.split("\n"):
        result.append("".join([char * k for char in str]))

    return result


def scale_vertically(strings, n):
    return "\n".join([str for str in strings for _ in range(n)])


def scale(string, k, n):
    if not string:
        return ""

    scaled_strings = scale_horizontally(string, k)
    scaled_strings = scale_vertically(scaled_strings, n)
    return scaled_strings


tests = [
    ("abcd\nefgh\nijkl\nmnop", 2, 3),
    ("", 1, 5),
]

for test in tests:
    print(scale(test[0], test[1], test[2]))