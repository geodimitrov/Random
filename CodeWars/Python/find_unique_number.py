# Solution 1 - slower
def find_unique_num(nums):
    for num in nums:
        if nums.count(num) == 1:
            return num

#Solution 2 - faster (using a set)
def find_unique_num(nums):
    unique_nums = set(nums)
    for el in unique_nums:
        if nums.count(el) == 1:
            return el

tests = [
    [1, 1, 1, 2, 1, 1],  # the unique num should be 2
    [0, 0, 0.55, 0, 0]   # the unique num should be 0.55
]

for test in tests:
    print(find_unique_num(test))