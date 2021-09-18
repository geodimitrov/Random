def solution(arr_val, arr_unit) :
    units = {
        'm': 1, 'cm': 0.01, 'mm': 0.001, 'μm': 1E-6, 'ft': 0.3048,
        'kg': 1, 'g': 0.001, 'mg': 0.000001, 'μg': 1E-09, 'lb': 0.453592,
    }


    object1_mass = arr_val[0] * units[arr_unit[0]]
    object2_mass = arr_val[1] * units[arr_unit[1]]
    distance = arr_val[2] * units[arr_unit[2]]
    G = 6.67*10**-11

    return G * (object1_mass * object2_mass / distance ** 2)