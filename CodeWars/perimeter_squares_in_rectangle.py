def get_squares_sides(n):
    result = [1, 1]

    for i in range(n - 1):
        result.append(result[i] + result[i + 1])

    return result


def sum_squares_perimeters(n):
    return 4 * sum(get_squares_sides(n))


tests = [
    5,      # should return 80
    7,      # should return 216
    20,     # should return 114624
    30,     # should return 14098308
]

for n in tests:
    print(sum_squares_perimeters(n))