def unique_in_order(iter):
    if not iter:
        result = []
    else:
        result = [iter[i] for i in range(len(iter) - 1) if iter[i] != iter[i+1]]
        result.append(iter[-1])
    return result