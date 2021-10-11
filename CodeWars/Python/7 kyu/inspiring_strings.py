def sum_consecutives(s):
    result = []
    sum_consec = s[0]

    for i in range(1, len(s)):

        if s[i] != s[i-1]:
            result.append(sum_consec)
            sum_consec = 0

        sum_consec += s[i]
    result.append(sum_consec)

    return result



tests = [
[1,4,4,4,0,4,3,3,1],  #[1,12,0,4,6,1],
[1,1,7,7,3],        # [2,14,3]
[-5,-5,7,7,12,0],   # [-10,14,12,0]
[3,3,3,3,1],        # [12, 1]
]

for t in tests:
    print(sum_consecutives(t))