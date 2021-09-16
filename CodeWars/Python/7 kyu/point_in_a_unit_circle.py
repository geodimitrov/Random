from math import dist

def point_in_circle(x, y):
    distance = dist((x, y), (0, 0))
    return distance < 1