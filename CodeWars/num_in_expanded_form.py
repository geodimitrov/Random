def get_expanded_form(num):
    counter = 0
    components = []

    while True:
        if num < 11:
            components.insert(0, str(num) + counter * "0")
            break

        remainder = num % 10

        if remainder != 0:
            components.insert(0, str(remainder) + counter * "0")

        num = num // 10
        counter += 1

    return ' + '.join(components)


tests = [
    12,         # should return "10 + 2"
    42,         # should return "40 + 2"
    70304,      # should return "70000 + 300 + 4"
    10,         # should return "10"
]

for test in tests:
    print(get_expanded_form(test))