# Solution 1 - long and descriptive
def solution(digits):
    max_value = '0'

    for i in range(len(digits) - 4):
        if ''.join(digits[i:i + 5]) > max_value:
            max_value = digits[i:i + 5]

    return int(max_value)


# Solution 2 - short and implicit
def solution1(digits):
    result = max([''.join(digits[i:i+5]) for i in range(len(digits) - 4)])
    return int(result)