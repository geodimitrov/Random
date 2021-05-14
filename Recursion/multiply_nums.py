# Create recursive function to multiply numbers

def multiply_nums(nums, n):

    # base case
    if n == 1:
        return nums[0]

    for i in range(n):
        num = nums[i]
        return num * multiply_nums(nums[i + 1:], n -1)

#Test input
nums = [1, 2, 2]
print(multiply_nums(nums, len(nums)))

nums = [0, 0, 0]
print(multiply_nums(nums, len(nums)))

nums = [5, 5, 5]
print(multiply_nums(nums, len(nums)))