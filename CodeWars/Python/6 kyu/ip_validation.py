def is_valid_IP(strng):
    result = []

    for el in strng.split('.'):

        if el.isdigit():
            if int(el) == 0 or \
                    (int(el) in range(1, 256) and not el.startswith('0')):
                result.append(el)

    return len(result) == 4