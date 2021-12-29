from itertools import groupby

def triple_double(num1, num2):
    num1_groups = groupby(str(num1))
    num2_groups = groupby(str(num2))
    num = None


    for el, g in num1_groups:

        if len(list(g)) == 3:
            num = el

    result = list(filter(lambda x: num in x and len(list(x[1])) == 2, num2_groups))
    return 1 if result else 0
