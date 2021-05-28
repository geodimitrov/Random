
def add_binary(a, b):
    return format(a + b, 'b')


tests = [
    (1, 1),
    (5, 9),
]

for test in tests:
    a, b = test
    print(add_binary(a, b))