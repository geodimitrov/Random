
def hex_string_to_rgb(hex_string):
    rgb = {'r': 0, 'g': 0, 'b': 0}
    i = 1

    for key in rgb:
        rgb[key] = int(hex_string[i:i + 2], 16)
        i += 2

    return rgb
