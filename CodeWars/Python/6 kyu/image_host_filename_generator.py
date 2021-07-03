from string import ascii_lowercase
from random import choice
STRING_LEN = 6

def generate_name():
    string = "".join([choice(ascii_lowercase) for _ in range(STRING_LEN)])
    return string


for i in range(10):
    print(generate_name())