# Solution 1 - using permutations
from itertools import permutations

def validate_anagrams(word, words):
    perms = ["".join(p) for p in permutations(word)]
    result = [w for w in words if w in perms]
    return result

# Solution 2 - using sorted()
def validate_anagrams(word, words):
    word = sorted(word)
    return [w for w in words if word == sorted(w)]

tests = [
    ('abba', ['aabb', 'abcd', 'bbaa', 'dada']), #should return ['aabb', 'bbaa']
('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), # should return ['carer', 'racer']
]

for test in tests:
    print(validate_anagrams(test[0], test[1]))