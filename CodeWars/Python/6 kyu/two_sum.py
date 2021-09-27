def two_sum(numbers, target):
    for x in range(len(numbers) - 1):
        for y in range(x + 1, len(numbers)):
            if numbers[x] + numbers[y] == target:
                return [x, y]