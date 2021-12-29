def meeting(s):
    names = [name.split(':') for name in s.upper().split(';')]
    sorted_names = sorted(names, key=lambda x: (x[1], x[0]))
    return ''.join(f"({name[1]}, {name[0]})" for name in sorted_names)
