def encode_string(string):
    result = ""

    for char in string:
        if string.count(char) > 1:
            result += ")"
        else:
            result += "("

    return result


tests = [
    "din", "recede", "Success", "(( @",
]

for test in tests:
    print(encode_string(test.lower()))