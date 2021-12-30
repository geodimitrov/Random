def max_sequence(arr):
    if not arr or all(el < 0 for el in arr):
        return 0

    max_sum = 0

    for x in range(len(arr)):
        for y in range(x, len(arr)):
            subarr_sum = sum(arr[x:y + 1])

            if subarr_sum > max_sum:
                max_sum = subarr_sum
    
    return max_sum
