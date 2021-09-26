def connotation(strng):
    pos_words = sum(1 for w in strng.lower().split() if w[0] in 'abcdefghijklm')
    neg_words = sum(1 for w in strng.lower().split() if w[0] in 'nopqrstuvwxyz')
    return pos_words >= neg_words


tests = [
    "A big brown fox caught a bad bunny",
    "Xylophones can obtain Xenon."
]

for t in tests:
    print(connotation(t))