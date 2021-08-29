# Solution 1 - detailed and explicit
def order(sentence):
    sentence = sentence.split()
    result = []

    for i in range(1, len(sentence) + 1):
        for el in sentence:
            if str(i) in el:
                result.append(el)

    return ' '.join(result)


# Solution 2 - short and implicit
def order1(sentence):
    return ' '.join(sorted(sentence.split(), key=lambda x: sorted(x)))
