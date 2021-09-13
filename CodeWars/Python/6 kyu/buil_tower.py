def tower_builder(n_floors):
    result = []

    for i in range(0, n_floors):
        side = (n_floors - 1 - i) * ' ' + i * '*'
        line = side + '*' + side[::-1]
        result.append(line)

    return result