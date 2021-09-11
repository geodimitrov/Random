def build_palindrome(s):
    for i in range(len(s)):
        if s[i:] == s[i:][::-1]:
            return s + s[:i][::-1]


tests = (
    'abcdc',    # should return 'abcdcba'
    'ababab',   # should return "abababa"
)

for test in tests:
    print(build_palindrome(test))