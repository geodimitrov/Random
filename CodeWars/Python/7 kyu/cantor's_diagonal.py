# Solution 1 - explicit
def cantor(matrix):
    result = []
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            result.append(1)
        else:
            result.append(0)

    return result


# Solution 1 - short and implicit
def cantor1(matrix):
    result = [1 if matrix[i][i] == 0 else 0 for i in range(len(matrix))]
    return result