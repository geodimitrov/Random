# Change all chars but the last 4 of a string to #, i.e "mask" the string

def maskify(string):
    for i in range(len(string) - 4):
        string = string.replace(string[i], "#", 1)

    return string

strings = [
    "4556364607935616",
    "64607935616",
    "1",
]

for str in strings:
    print(maskify(str))