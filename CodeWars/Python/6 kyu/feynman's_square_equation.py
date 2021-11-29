def count_squares(n):
    return sum(el * el for el in range(1, n + 1))


tests = (
    3, 5, 8, 15
)

for t in tests:
    print(count_squares(t))