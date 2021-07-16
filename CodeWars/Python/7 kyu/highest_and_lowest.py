def high_and_low(numbers):
    high = max(map(int, numbers.split()))
    low = min(map(int, numbers.split()))
    return f'{high} {low}'