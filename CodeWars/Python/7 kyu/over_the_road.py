def over_the_road(address, n):
    opposite_address = (n * 2 + 1) - address
    return opposite_address


tests = [
    (1, 3),  # should return 6
    (3, 3),  # should return 4
    (2, 3),  # should return 5
]

for test in tests:
    print(over_the_road(test[0], test[1]))
