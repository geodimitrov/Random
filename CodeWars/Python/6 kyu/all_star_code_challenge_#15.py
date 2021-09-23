def rotate(strng):
    result = []

    for i in range(len(strng)):
        strng = strng[1:] + strng[0]
        result.append(strng)

    return result