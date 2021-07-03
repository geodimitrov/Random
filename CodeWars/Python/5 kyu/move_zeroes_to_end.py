def move_zeros(nums, i=0):

    for el in nums:
        if el == 0:
            nums.append(el)
            nums.remove(el)

    return nums

tests = [
    [1, 0, 1, 2, 0, 1, 3],
    [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
]

for test in tests:
    print(move_zeros(test))