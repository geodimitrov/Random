def tribonacci(signature, n):
    result = signature[:n]

    for i in range(3, n):
        result.append(sum(result[i - 3: i]))

    return result