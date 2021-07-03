# Solution 1: short (using comprehensions)
def sort_array(array):
    odds = sorted([num for num in array if not num % 2 == 0], reverse=True)
    return [odds.pop() if not array[i] % 2 == 0 else array[i] for i in range(len(array)) ]


# Solution 2: long (using functions)
def get_odd_nums(array):
    return [num for num in array if not num % 2 == 0]

def sort_odds_in_array(odds, array):
    sorted_odds = sorted(odds, reverse=True)

    for i in range(len(array)):
        if not array[i] % 2 == 0:
            array[i] = sorted_odds.pop()

    return array

def sort_array2(array):
    odds = get_odd_nums(array)
    sorted_array = sort_odds_in_array(odds, array)
    return sorted_array

print(sort_array([5, 8, 6, 3, 4]))
print(sort_array2([5, 8, 6, 3, 4]))