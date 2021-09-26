
# Solution 1
def mygcd(x, y):

    while not x == y:

        if x > y:
            x = x - y
        else:
            y = y - x

    return x


# Solution 2
def mygcd1(x, y):

    while y:
        x, y = y, x % y

    return x



tests = [
    (30, 12),   # 6
    (8, 9),     # 1
    (1, 1),     # 1
]

for t in tests:
    print(mygcd(t[0], t[1]))