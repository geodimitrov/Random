import math

def sum_or_product(array, n):
    sum_largest_nums = sum(sorted(array, reverse=True)[:n])
    prod_smallest_nums = math.prod(sorted(array)[:n])
    
    if sum_largest_nums > prod_smallest_nums:
        return 'sum'
    elif sum_largest_nums < prod_smallest_nums:
        return 'product'
    
