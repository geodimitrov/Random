# Will use the divmod func to simply calculate the seconds, minutes & hours.
# For more info on the divmod func, go to https://www.w3schools.com/python/ref_func_divmod.asp

def make_readable(secs):
    minutes, seconds = divmod(secs, 60)
    hours, minutes = divmod(minutes, 60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


tests = [
    0,          # "00:00:00"
    5,          # "00:00:05"
    60,         # "00:01:00"
    86399,      # "23:59:59"
    359999,     # "99:59:59"
]

for test in tests:
    print(make_readable(test))

