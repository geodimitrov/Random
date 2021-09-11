# Solution 1 - explicit
def paint_letterboxes(start, finish):
    letterboxes = ''.join(str(i) for i in range(start, finish + 1))
    result = []

    for i in range(10):
        result.append(letterboxes.count(str(i)))

    return result


# Solution 2 - implicit
def paint_letterboxes1(start, finish):
    letterboxes = ''.join(str(i) for i in range(start, finish + 1))
    return [letterboxes.count(str(i)) for i in range(10)]