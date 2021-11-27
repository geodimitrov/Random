# Solution 1 - loops (explicit)
def finance(n):
    result = 0

    for x in range(1, n + 1):
    	result += sum(range(x, x*2 + 1))
    
    return result

# Solution 2 - use formula (for speed and performance)
def finance1(n):
    # multiply n to the sum of triangular(n) + n + 1
    return n * sum(range(1, n + 2))
