vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

def sort_vowels(string):
    if not isinstance(string, str):
        return ""
    else:
        result = ["|" + char if char in vowels else char + "|" for char in string]

    return "\n".join(result)


tests = [
    'Codewars',
    'Rnd Te5T',
    1337,
    None,

]

for test in tests:
    print(sort_vowels(test))