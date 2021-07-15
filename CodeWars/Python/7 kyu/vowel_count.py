def get_count(input_str):
    return sum(1 for char in input_str if char in 'aeiou')