def find_index(array):
    for i in range(len(array)):

        if sum(array[:i]) == sum(array[i+1:]):
            return i

    return -1


tests = [
    [1, 2, 3, 4, 3, 2, 1],           # should return 3
    [20, 10, -80, 10, 10, 15, 35],   # should return 0
    [1, 100, 50, -51, 1, 1],         # should return 1
    [-1, -2, -3, -4, -3, -2, -1],    # should return 3
    list(range(-100, -1)),           # should return -1
]

for test in tests:
    print(find_index(test))