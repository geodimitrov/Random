def some_but_not_all(seq, predicate):
    counter = sum([1 for el in seq if predicate(el)])
    return counter < len(seq) and counter != 0


tests = [
    ('abcdefg&%$', str.isalpha),  # >>> True
    ('&%$=', str.isalpha),        # >>> False
    ('abcdefg', str.isalpha),     # >>> False
    ([4, 1], lambda x: x > 3),      # >>> True
    ([1, 1], lambda x: x > 3),      # >>> False
    ([4, 4], lambda x: x > 3),      # >>> False
]

for test in tests:
    print(some_but_not_all(test[0], test[1]))