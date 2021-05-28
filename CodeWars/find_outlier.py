# Find the outlier in a collection of ints: it's either odd or even

def find_outlier(integers):
    odds = 0
    evens = 0
    outlier = None

    for i in range(len(integers)):
        if integers[i] % 2 == 0:
            evens += 1
            even_num_index = i
        else:
            odds += 1
            odd_num_index = i

        if evens > 1 and odds:
            outlier = integers[odd_num_index]
        elif odds > 1 and evens:
            outlier = integers[even_num_index]

    return outlier


tests = [
    [2, 4, 0, 100, 4, 11, 2602, 36],  # the outlier is 11
    [160, 3, 1719, 19, 11, 13, -21],  # the outlier is 160
]

for ints in tests:
    print(find_outlier(ints))