def sq_in_rect(l, w):
    min_side, max_side = sorted((l, w))
    result = []

    while min_side != max_side and min_side > 0:
        sides_diff = max_side // min_side
        result += [min_side] * sides_diff
        max_side, min_side = min_side, max_side % min_side,

    return result or None



tests = [
    (5, 5),     # None
    (5, 3),     # [3, 2, 1, 1]
    (20, 14),   # [14, 6, 6, 2, 2, 2]
    (37, 14),   # [14, 14, 9, 5, 4, 1, 1, 1, 1]
]

for t in tests:
    print(sq_in_rect(*t))