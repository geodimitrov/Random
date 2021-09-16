def delete_nth(order, max_e):
    result = []

    for el in order:
        if result.count(el) < max_e:
            result.append(el)

    return result
