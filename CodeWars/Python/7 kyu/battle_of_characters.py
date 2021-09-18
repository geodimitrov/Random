# explicit is better than implicit
def battle(x, y):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    power_x = sum(alphabet.index(char) + 1 for char in x)
    power_y = sum(alphabet.index(char) + 1 for char in y)

    if power_x > power_y:
        return x
    elif power_x < power_y:
        return y
    else:
        return 'Tie!'