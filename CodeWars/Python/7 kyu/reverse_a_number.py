def reverse_number(n):
    if n < 0:
        return -int(str(n)[:0:-1])

    return int(str(n)[::-1])


tests = [
    123,
    -456,
    1000,
]

for t in tests:
    print(reverse_number(t))