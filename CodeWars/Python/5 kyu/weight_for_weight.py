def order_weight(string):
    weights = string.strip().split()
    sorted_weights = sorted(sorted(weights), key=lambda x: sum(int(d) for d in x))
    return ' ' .join(sorted_weights)