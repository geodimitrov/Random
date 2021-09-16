def is_triangle(a, b, c):
    # check if sum of any two sides > len of 3rd side
    return a + b > c and a + c > b and b + c > a