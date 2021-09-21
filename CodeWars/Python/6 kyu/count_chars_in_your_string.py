def count(string):
    if not string:
        return {}

    return {el: string.count(el) for el in set(string)}