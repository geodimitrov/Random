def find_e(s):
    if not s:
        return s
    elif 'e' not in s.lower():
        return 'There is no "e".'

    return str(s.lower().count('e'))