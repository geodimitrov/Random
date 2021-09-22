def different_squares(matrix):
    size = len(matrix)
    squares = []

    for r in range(size - 1):
        for c in range(len(matrix[r]) - 1):
            square = (matrix[r][c], matrix[r][c+1], matrix[r+1][c], matrix[r+1][c+1])
            squares.append(square)

    return len(set(squares))


tests = [
[
 [1,2,1],
 [2,2,2],
 [2,2,2],
 [1,2,3],
 [2,2,1]
    ],
[
 [9,9,9,9,9],
 [9,9,9,9,9],
 [9,9,9,9,9],
 [9,9,9,9,9],
 [9,9,9,9,9],
 [9,9,9,9,9]
]
]

for test in tests:
    print(different_squares(test))