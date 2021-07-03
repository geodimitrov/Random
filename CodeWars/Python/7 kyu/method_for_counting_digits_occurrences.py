class List:
    def count_spec_digits(self, integers_list, digits_list):
        digits = "".join(map(str, integers_list))
        result = [(digit, digits.count(str(digit))) for digit in digits_list]
        return result


tests = [
    (
        [1, 1, 2, 3, 1, 2, 3, 4],
        [1, 3]
    ),
    (
        [-18, -31, 81, -19, 111, -888],
        [1, 8, 4]),
    (
        [-77, -65, 56, -79, 6666, 222],
        [1, 8, 4]
    ),
]

for test in tests:
    print(List().count_spec_digits(test[0], test[1]))