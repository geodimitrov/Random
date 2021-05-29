def modify_strings(strings, k):
    modified_strings = []
    max_length = 0

    for i in range(len(strings) - k + 1):
        modified_string = "".join(strings[i:i+k])
        modified_strings.append(modified_string)

        if len(modified_string) > max_length:
            max_length = len(modified_string)

    return modified_strings, max_length


def get_longest_consec_str(strings, k):
    if strings and k <= len(strings) and k > 0:
        modified_strings, max_length = modify_strings(strings, k)
        for str in modified_strings:
            if len(str) == max_length:
                return str

    return ""


tests = [
    (["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2),
    (["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2),
]

for test in tests:
    print(get_longest_consec_str(test[0], test[1]))
