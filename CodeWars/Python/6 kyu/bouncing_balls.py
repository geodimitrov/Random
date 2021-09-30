def bouncing_ball(h, bounce, window):
    if any((h <= 0, not 0 < bounce < 1, window >= h)):
        return -1

    ball_height = h
    counter = 0

    while ball_height > window:
        ball_height *= bounce
        counter += 2

    return counter - 1