def strip_comments(text, signs):
    strings = text.split("\n")

    for i in range(len(strings)):
        string = strings[i]

        for sign in signs:
            if sign in string:
                sign_index = string.index(sign)
                string = string[:sign_index]

        strings[i] = string.strip()

    return "\n".join(strings)


tests = [
    ("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]),
    ("a #b\nc\nd $e f g", ["#", "$"]),
]

for test in tests:
    print(strip_comments(test[0], test[1]))