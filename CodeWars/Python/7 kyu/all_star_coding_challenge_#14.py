def median(array):
    median_value_index = len(array) // 2


    if len(array) % 2 == 0:
        median_value = sum(sorted(array)[median_value_index - 1: median_value_index + 1]) / 2

    else:
        median_value = sorted(array)[median_value_index]

