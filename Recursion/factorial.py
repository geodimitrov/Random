'''
Create a recursive function to calculate the factorial of a number.
You can use the factorial func from math but the purpose here is to practice recursion
'''
# For more info, go to https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/the-factorial-function


def get_factorial(n):

    #base case
    if n == 0:
        return 1

    #body
    for i in range(n):
        return n * get_factorial(n - 1)


#Test code
print(get_factorial(4))
print(get_factorial(10))
print(get_factorial(0))
print(get_factorial(1))