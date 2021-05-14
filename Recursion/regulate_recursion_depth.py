# For some reason, we might want to regulate (increase or decrease) the recursion depth

# 1) we need to import the sys module
import sys

# 2) let's define a func that calculates factorial of a num
def get_factorial(n):

    if n == 0:
        return 1

    for i in range(n):
        return n * get_factorial(n - 1)


# 3) set the recursion limit to 500 and print the rec limit
sys.setrecursionlimit(500)
print(sys.getrecursionlimit())

# 4) try to call the func with an arg > 500, expect an exception
get_factorial(550)