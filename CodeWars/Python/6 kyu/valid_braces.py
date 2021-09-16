def validBraces(string):
    brace_checker = {
        ']': '[',
        ')': '(',
        '}': '{'
    }

    result = []

    for char in string:
        if char in '[({':
            result.append(char)

        else:
            if not result or brace_checker[char] != result[-1]:
                return False

            result.pop()

    return True if not result else False