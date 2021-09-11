# Solution 1 - explicit & descriptive
def magical_well(a, b, n):
    result = 0

    for _ in range(n):
        result += a * b
        a += 1
        b += 1

    return result


# Solution 2 - implicit
def magical_well1(a, b, n):
    return sum([(a + i) * (b + i) for i in range(n)])

