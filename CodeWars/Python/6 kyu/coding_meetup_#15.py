def is_odd_name(name):
    return sum(map(ord, name)) % 2 != 0

def find_odd_names(lst):
    devs_odd_names = [el for el in lst if is_odd_name(el['firstName'])]
    return devs_odd_names