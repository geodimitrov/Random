# Solution 1 - explicit
def spin_words(sentence):
    result = []

    for word in sentence.split():
        if len(word) >= 5:
            word = word[::-1]
        result.append(word)

    return ' '.join(result)


# Solution 2 - concise
def spin_words1(sentence):
    return ' '.join(word[::-1] if len(word) >= 5 else word for word in sentence.split() )


tests = [
    "Hey fellow warriors",
    "This is a test",
    "This is another test"
]

for test in tests:
    print(spin_words(test))