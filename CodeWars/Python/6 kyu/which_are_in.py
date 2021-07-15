def in_array(array1, array2):
    result = {substr for substr in array1 for str in array2 if substr in str}
    return sorted(list(result))