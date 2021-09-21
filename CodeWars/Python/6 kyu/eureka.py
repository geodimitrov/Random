def sum_dig_pow(a, b):
    result = []

    for i in range(a, b + 1):
        num = str(i)
        modifuied_num = sum(int(num[x]) ** (x + 1) for x in range(0, len(str(i))))

        if modifuied_num == i:
            result.append(i)

    return result