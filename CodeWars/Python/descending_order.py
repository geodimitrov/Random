def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))

tests = [
    42145,
    145263,
    123456789,
]

for test in tests:
    print(descending_order(test))