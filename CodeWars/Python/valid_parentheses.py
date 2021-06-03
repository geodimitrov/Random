def validate_parentheses(string):
    result = []

    for char in string:

        if char == "(":
            result.append(char)

        elif char == ")":
            if result and result[-1] == "(":
                result.pop()
            else:
                result.append(char)
                break

    if result:
        return False

    return True


tests = [
    "()",              # =>  true
    ")(()))",          # =>  false
    "(",               # =>  false
    "(())((()())())",  # =>  true
]

for test in tests:
    print(validate_parentheses(list(test)))