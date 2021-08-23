# Solution 1 - explicit & descriptive
def wrap(height, width, length):
    width_total = width * 2
    height_total = height * 2
    length_total = length * 2

    if height <= length and height <= width:
        height_total = height * 4

    elif length < height and length < width:
        length_total = length * 4
    else:
        width_total = width * 4

    return width_total + height_total + length_total + 20


# Solution 2 - implicit & concise
def wrap1(height, width, length):
    params = sorted((height, width, length))
    return params[0] * 4 + params[1] * 2 + params[2] * 2 + 20


tests = (
    (17, 32, 11),
    (13, 13, 13),
    (1, 3, 1),
)

for test in tests:
    print(wrap(test[0], test[1], test[2]))
