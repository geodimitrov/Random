def compose(s1, s2):
    s1, s2 = (el.split() for el in (s1, s2))
    result = []

    for i in range(len(s1)):
        result.append(s1[i][:i+1] + s2[-i - 1][:len(s2) - i])

    return '\n'.join(result)