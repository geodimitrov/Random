def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    return ((given_mass1 / molar_mass1 + given_mass2 / molar_mass2) * (temp + 273.15) * 0.082) / volume


# Tests
print(solution(44, 30, 3, 2, 5, 50))        # 0.7146511212121212
print(solution(60, 20, 10, 30, 10, 100))    # 5.099716666666667
