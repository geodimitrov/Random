def get_sum_of_cubes_of_digits(str_num):
    return sum([int(d) ** 3 for d in str_num])


def cut_string_into_substrings(string, size):
    return [string[i:i+size] for i in range(0, len(string), size)]


def is_divisible_by_two(sum):
    return sum % 2 == 0


def revrot(string, size):

    if size == 0 or size > len(string) or not string:
        return ''

    substrings = cut_string_into_substrings(string, size)
    modified_str = ''

    for substr in substrings:

        if len(substr) >= size:
            substring_sum = get_sum_of_cubes_of_digits(substr)

            if is_divisible_by_two(substring_sum):
                modified_str += substr[::-1]
            else:
                modified_str += substr[1:] + substr[0]

    return modified_str


tests = [
    ('123456987654', 6),  # --> "234561876549"
    ("123456987653", 6),  # --> "234561356789"
    ("66443875", 4),      # --> "44668753"
    ("66443875", 8),      # --> "64438756"
    ("123456779", 0),     # --> ""
]

for test in tests:
    print(revrot(test[0], test[1]))

# If
# sz is <= 0 or if str is empty return ""
# sz is greater (>) than the length of str it is
# impossible to take a chunk of size sz hence return "".