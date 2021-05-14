# Create recursive function to calc sum of numbers

def calc_nums(nums, n):

    # introduce base case
    if n == 1:
        return nums[0]

    #introduce body
    for i in range(n):
        num = nums[i]
        return num + calc_nums(nums[i + 1:], n-1)


#Test inputs
nums = [1, 2, 3]
print(calc_nums(nums, len(nums)))

nums = [4, 4, 4]
print(calc_nums(nums, len(nums)))

nums = [5.5, 1, 1]
print(calc_nums(nums, len(nums)))