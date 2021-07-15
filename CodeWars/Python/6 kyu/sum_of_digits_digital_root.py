def digital_root(n):

    while n > 9:
        n = sum(int(d) for d in str(n))

    return n