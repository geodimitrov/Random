def get_price_points(prices):
    result = []
    start_i = 0

    for i in range(len(prices) - 1):
        if prices[i] > prices[i + 1]:
            result.append(prices[start_i:i + 1])
            start_i = i + 1

        elif i + 2 == len(prices):
            result.append(prices[start_i:])

    return result


def ideal_trader(prices):
    price_points = get_price_points(prices)
    investment = 1

    for p in price_points:
        investment *= max(p) / min(p)

    return investment