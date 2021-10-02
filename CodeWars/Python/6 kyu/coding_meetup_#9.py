def is_age_diverse(lst):
    ages = [el['age'] // 10 for el in lst]
    return all(i in ages for i in range(1, 10)) and \
            any(a >= 10 for a in ages)