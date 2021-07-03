def find_squares(num):
    square_a_side = num // 2
    square_b_side = num - square_a_side
    squares = sorted([square_a_side ** 2, square_b_side ** 2], reverse=True)
    return f"{squares[0]}-{squares[1]}"


tests = [
    9,      #should return '25-16'
    5,      #should return '9-4'
]

for test in tests:
    print(find_squares(test))