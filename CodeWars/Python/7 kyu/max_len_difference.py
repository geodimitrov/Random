def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1

    result = []

    for x in a1:
        for y in a2:
            result.append(abs(len(x) - len(y)))

    return max(result)
