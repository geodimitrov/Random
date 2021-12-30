def sc(s):
    screws_to_be_removed = len(s)
    screwdriver_switches = s.count('+-') + s.count('-+')
    return screws_to_be_removed * 2 - 1 + screwdriver_switches * 5
