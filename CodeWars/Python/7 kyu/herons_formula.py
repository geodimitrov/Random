def heron(a, b, c):
    s = (a + b + c) / 2
    return round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)
