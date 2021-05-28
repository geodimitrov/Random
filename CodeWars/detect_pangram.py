from string import ascii_lowercase

def is_pangram(text):
    alphabet = tuple(ascii_lowercase)

    for el in alphabet:
        if el not in text.lower():
            return False

    return True


tests = [
    "The quick brown fox jumps over the lazy dog",
    "This is not pangram",
]

for text in tests:

    if is_pangram(text):
        print("Yes")
    else:
        print("No")