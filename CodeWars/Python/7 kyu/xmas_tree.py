def xmastree(n):
    stem = [(n - 1) * '_' + '#' + (n - 1) * '_'] * 2
    body = []

    for i in range(n):
        side = (n - 1 - i) * '_' + i * '#'
        line = side + '#' + side[::-1]
        body.append(line)

    return body + stem