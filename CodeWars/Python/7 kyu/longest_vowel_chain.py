import re

def solve(s):
    EX = '[aeiou]+'
    vowels = re.findall(EX, s)
