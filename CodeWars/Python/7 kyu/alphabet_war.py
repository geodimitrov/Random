def alphabet_war(fight):
    l_side_power_pts = {
        'w': 4, 'p': 3, 'b': 2, 's': 1,
    }
    r_side_power_pts = {
        'm': 4, 'q': 3, 'd': 2, 'z': 1,
    }

    l_side_total_pts = 0
    r_side_total_pts = 0

    for char in fight:
        if char in l_side_power_pts:
            l_side_total_pts += l_side_power_pts[char]
        elif char in r_side_power_pts:
            r_side_total_pts += r_side_power_pts[char]

    if l_side_total_pts > r_side_total_pts:
        return 'Left side wins!'
    elif l_side_total_pts < r_side_total_pts:
        return 'Right side wins!'
    else:
        return 'Let\'s fight again!'