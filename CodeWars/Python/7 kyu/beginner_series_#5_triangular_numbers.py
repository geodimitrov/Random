def is_triangular(t):
    # perfect square testing method: t is triangular if 8 * t + 1 is perfect square
    n = 8 * t + 1

    # get the square root of 8 * n + 1
    sq_root = n ** 0.5

    # check if it's perfect square
    return sq_root.is_integer()
