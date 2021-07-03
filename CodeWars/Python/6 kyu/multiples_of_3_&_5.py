# Find all multiples of 3 & 5 in the range (1, number); 0 is not a natural number!
# Sum the multiples

def get_multiples(num):
    result = []

    for n in range(1, num):
        if n % 3 == 0 or n % 5 == 0:
            result.append(n)

    return result

def sum_multiples(num):
    return sum(get_multiples(num))


tests = [
    10,
]

for num in tests:
    print(sum_multiples(num))