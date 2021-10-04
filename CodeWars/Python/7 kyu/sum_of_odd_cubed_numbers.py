def cube_odd(arr):
    if not all(type(el) == int for el in arr):
        return None
    
    return sum(filter(lambda x: x % 2 != 0, map(lambda x: x ** 3, arr)))