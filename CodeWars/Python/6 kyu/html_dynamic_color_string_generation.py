import random

def generate_color_rgb():
    chars = "0123456789ABCDEFabcdef"
    color = '#' + ''.join(str(random.choice(chars)) for i in range(6))
    return color