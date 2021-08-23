def rgb(r, g, b):
    numeric_values = []

    for el in (r, g, b):
        if el < 0:
            numeric_values.append(0)
        elif el > 255:
            numeric_values.append(255)
        else:
            numeric_values.append(el)

    return ''.join([hex(el).replace("0x", "").upper() if el > 9 else hex(el).replace("x", "") for el in numeric_values])