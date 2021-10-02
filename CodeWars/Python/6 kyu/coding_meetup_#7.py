def find_senior(lst):
    max_age = max(el['age'] for el in lst)
    return list(filter(lambda x: x['age'] == max_age, lst))