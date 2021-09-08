def count_squares(cuts):
    return ((1 + cuts) ** 3) - ((cuts - 1) **3)


print(count_squares(1))
print(count_squares(2)) # 26    -1
print(count_squares(3))
print(count_squares(4)) # 98   -27
print(count_squares(5)) # 152   -64
print(count_squares(16))