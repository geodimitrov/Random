def matrix(array):
    for i in range(len(array)):

        if array[i][i] >= 0:
            array[i][i] = 1
        else:
            array[i][i] = 0

    return array