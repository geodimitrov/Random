def to_weird_case(string):
    result = []

    for w in string.split():
        w = ''.join(w[i].upper() if i % 2 == 0 else w[i].lower() for i in range(len(w)))
        result.append(w)

    return ' '.join(result)