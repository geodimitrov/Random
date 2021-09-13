import re

def to_camel_case(text):
    EX = '[-_]'

    if not text:
        return ''

    words = re.split(EX, text)
    return words[0] + ''.join(w.capitalize() for w in words[1:])
