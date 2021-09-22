def to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f'{hours} hour(s) and {minutes} minute(s)'

tests = [
    3600, 3601, 3500, 0
]

for test in tests:
    print(to_time(test))